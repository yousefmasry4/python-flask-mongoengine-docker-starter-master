import sys


sys.path.insert(1, './')
from api.v1.resources.wiki import wikis
from api.v1.resources.news import news
from api.v1.resources.x_ray import x_ray
from api.v1.resources.diagnosis import diagnosis


def initialize_routes(apis):
    apis.add_namespace(wikis)
    apis.add_namespace(diagnosis)
    apis.add_namespace(x_ray)
    apis.add_namespace(news)
