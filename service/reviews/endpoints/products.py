# The products endpoint

import logging

from flask import request
from flask.json import jsonify
from flask_restplus import Resource
from reviews.business import get_ratings
from reviews.serializers import product_body
from reviews.api import api

log = logging.getLogger(__name__)

ns = api.namespace('products', description='Operations related to products')


@ns.route('/<string:product_id>')
@api.response(404, 'Product not found.')
class ReviewItem(Resource):

    @api.marshal_with(product_body)
    def get(self, product_id):
        ratings = get_ratings(product_id)
        return { 'product_id': product_id, 'ratings': ratings }
