import json
from flask import abort
from flask_restx import Namespace, Resource
from api.v1.database.models import New
from mongoengine import DoesNotExist

news = Namespace('v1/news', description='news namespace')


@news.route('/get_all')
class NewsApi(Resource):
    def get(self):
        """List all news"""
        todos = New.objects.all()
        return json.loads(todos.to_json()), 200


@news.route('/<id>')
@news.response(404, 'new not found')
@news.param('id', 'The new identifier')
class NewsApi(Resource):
    def get(self, id):
        """Fetch a given new"""
        try:
            todo = New.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except DoesNotExist:
            abort(404)
        except:
            abort(500)
