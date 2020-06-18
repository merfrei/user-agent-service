"""
User Agents Handlers
"""

from api.handlers.base import get_base_get
from api.handlers.base import get_base_post
from api.handlers.base import get_base_put
from api.handlers.base import get_base_delete
from api.model.user_agent import UserAgentDB
from api.model.user_agent import UserAgentSchema


async def get_handler(request):
    '''GET requests'''
    where_query = []
    if 'string' in request.query:
        where_query.append(
            ('string', 'ilike', '%{}%'.format(request.query['string'])))
    if 'software' in request.query:
        where_query.append(
            ('software', 'ilike', '%{}%'.format(request.query['software'])))
    if 'os' in request.query:
        where_query.append(
            ('os', 'ilike', '%{}%'.format(request.query['os'])))
    if 'platform' in request.query:
        where_query.append(
            ('platform', '=', request.query['os']))
    result = await get_base_get(UserAgentDB, *where_query,
                                extra='ORDER BY string asc')(request)
    return result


async def post_handler(request):
    '''POST requests'''
    result = await get_base_post(UserAgentDB, UserAgentSchema)(request)
    return result


async def put_handler(request):
    '''PUT requests'''
    result = await get_base_put(UserAgentDB, UserAgentSchema)(request)
    return result


async def delete_handler(request):
    '''DELETE requests'''
    result = await get_base_delete(UserAgentDB)(request)
    return result
