import sys


sys.path.insert(1, './')
from api.v1.resources.wiki import wikis
from api.v1.resources.news import news
from api.v1.resources.model_preview import preview_model
from api.v1.resources.Diabetic_Retinopathy import prognosis
from api.v1.resources.x_ray import x_ray



def initialize_routes(apis):
    apis.add_namespace(wikis)
    apis.add_namespace(preview_model)
    apis.add_namespace(x_ray)
    apis.add_namespace(news)
    apis.add_namespace(prognosis)
