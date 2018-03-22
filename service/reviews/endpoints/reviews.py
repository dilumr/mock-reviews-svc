# The reviews endpoint

import logging

from flask import request
from flask.json import jsonify
from flask_restplus import Resource
from reviews.business import create_review, delete_review, recent_reviews, update_review
from reviews.serializers import review_body, review_whole
from reviews.api import api

log = logging.getLogger(__name__)

ns = api.namespace('reviews', description='Operations related to reviews')


@ns.route('/')
class ReviewCollection(Resource):

    @api.marshal_list_with(review_whole)
    def get(self):
        """
        Returns the reviews, ordered most recently updated first
        """
        return recent_reviews(20)

    @api.response(201, 'Review successfully created.')
    @api.expect(review_body)
    def post(self):
        """
        Creates a new product review.
        """
        data = request.json
        review_id = create_review(data)
        return {'id': review_id }, 201


@ns.route('/<string:id>')
@api.response(404, 'Review not found.')
class ReviewItem(Resource):

    @api.expect(review_body)
    @api.response(204, 'Review successfully updated.')
    def put(self, id):
        """
        Updates a review.
        Use this method to revise the rating for the product
        """
        data = request.json
        update_review(id, data)
        return None, 204

    # @api.expect(review_patch)
    # @api.response(204, 'Review successfully patched.')
    # def patch(self, id):
    #     """
    #     Patches a review.
    #     Use this method update the flagging status (0 - not flagged, 1 - user flagged, 2 - absolved, 3 - concurred)
    #     """
    #     # data = request.json
    #     # update_category(id, data)
    #     return None, 204

    @api.response(204, 'Review successfully deleted.')
    def delete(self, id):
        """
        Deletes a review.
        """
        delete_review(id)
        return None, 204
