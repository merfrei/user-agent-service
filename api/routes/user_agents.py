"""
User Agent routes
"""

from api.handlers.user_agents import get_handler
from api.handlers.user_agents import post_handler
from api.handlers.user_agents import put_handler
from api.handlers.user_agents import delete_handler


def init_user_agents_routes(app):
    '''Init API routes for User Agents'''
    app.router.add_route('GET', r'/user_agents/{id:\d+}', get_handler)
    app.router.add_route('GET', r'/user_agents', get_handler)
    app.router.add_route('POST', r'/user_agents', post_handler)
    app.router.add_route('PUT', r'/user_agents/{id:\d+}', put_handler)
    app.router.add_route('DELETE', r'/user_agents/{id:\d+}', delete_handler)
