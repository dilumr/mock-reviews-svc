# API-wide conventions and definitions

import logging
import traceback

from flask_restplus import Api
from reviews import settings

log = logging.getLogger(__name__)

api = Api(version='1.0', title='Mock Reviews API',
          description='Post reviews and get rating aggregates')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500

@api.errorhandler(LookupError)
def mem_lookup_failed_handler(e):
    log.warning(traceback.format_exc())
    return {'message': f'Resource not found: {e}'}, 404
