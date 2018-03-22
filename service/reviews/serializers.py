from flask_restplus import fields
from reviews.api import api

review_body = api.model('ProductReviewBody', {
    'product_id': fields.String(required=True,  description='Product ID'),
    'text':       fields.String(required=False, description='Review text'),
    'rating':     fields.Integer(required=True, description='Star rating')
})

review_whole = api.clone('ProductReview', review_body, {
    'review_id':  fields.String(required=False, description='Review ID')
})

review_patch = api.model('Patch a review', {
    'flagging':   fields.Integer(required=False, description='None, 0 - not flagged, 1 - user flagged, 2 - absolved, 3 - concurred')
})

ratings_agg = api.model('Star ratings aggregate', {
    '1': fields.Integer(required=True, description='Number of 1 star ratings'),
    '2': fields.Integer(required=True, description='Number of 2 star ratings'),
    '3': fields.Integer(required=True, description='Number of 3 star ratings'),
    '4': fields.Integer(required=True, description='Number of 4 star ratings'),
    '5': fields.Integer(required=True, description='Number of 5 star ratings')
})

product_body = api.model('Ratings associated with a product', {
    'product_id': fields.String(required=True, description='Product ID'),
    'ratings': fields.Nested(ratings_agg)
})
