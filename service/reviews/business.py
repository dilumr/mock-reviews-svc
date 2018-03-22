
from box import Box
from collections import Counter, defaultdict, OrderedDict
from itertools import islice
import threading
import uuid

_lock = threading.RLock()
_products_db = defaultdict(Counter)
_reviews_db = OrderedDict()

def unique_id():
    return str(uuid.uuid4())

def boxup(data):
    return data if isinstance(data, Box) else Box(data)

def change_count(counter, rating, delta):
    if 1 <= rating <= 5:
        counter[rating] += delta

def update_review(review_id, data):
    data = boxup(data)
    with _lock:
        previous = _reviews_db.pop(review_id, None)
        # missing key safe entry removal
        # remove and re-add will move the review in the OrderedDict's ordering
        if previous:
            # lookup counts twice, to handle case where product associated with review has changed.
            counts = _products_db[previous.product_id]
            change_count(counts, previous.rating, -1)
        if data:
            # allowing for None data means this function can be used for deletes of reviews, too.
            counts = _products_db[data.product_id]
            change_count(counts, data.rating, 1)
            data_copy = dict(data)
            data_copy['review_id'] = review_id
            _reviews_db[review_id] = data_copy
        # note -- if data is Null, the .pop has the effect of removing review of specified id.


def create_review(data):
    review_id = unique_id()
    update_review(review_id, data)
    return review_id


_MAXIMUM_REVIEWS_RETURNED = 100

def recent_reviews(limit = 10):
    actual_limit = max(1, min(limit, _MAXIMUM_REVIEWS_RETURNED))
    with _lock:
        # capture (bounded) generator values in list before escaping lock
        return list(islice(reversed(_reviews_db.values()), actual_limit))


def delete_review(review_id):
    update_review(review_id, None)


def get_ratings(product_id):
    with _lock:
        counts = _products_db.get(product_id) # get wont auto-allocate
        if not counts:
            raise LookupError(f'product id={product_id}')
        return { str(i): counts[i] for i in range(1, 6)}
