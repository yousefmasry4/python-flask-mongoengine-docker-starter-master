import sys


sys.path.insert(0, '/code')
from api.v1.resources.wiki import wikis
from api.v1.resources.news import news
from api.v1.resources.x_ray import x_ray


def initialize_routes(apis):
    apis.add_namespace(wikis)
    apis.add_namespace(x_ray)
    apis.add_namespace(news)
