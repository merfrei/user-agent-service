"""
API: init routes
"""

from api.routes.user_agents import init_user_agents_routes


def init_routes(app):
    '''Init some routes for the App'''
    init_user_agents_routes(app)
