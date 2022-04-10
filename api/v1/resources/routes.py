# some_file.py
import sys

sys.path.insert(0, '/code')
from api.v1.resources.wiki import wikis
from api.v1.resources.news import news


def initialize_routes(apis):
    apis.add_namespace(wikis)
    apis.add_namespace(news)
