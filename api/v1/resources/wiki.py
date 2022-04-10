import json
from flask import abort
from flask_restx import Namespace, Resource
from api.v1.database.models import Wiki
from mongoengine import DoesNotExist

wikis = Namespace('v1/wiki', description='wiki namespace')


@wikis.route('/')
class WikisApi(Resource):
    def get(self):
        '''List all Todos'''
        todos = Todo.objects.all()
        return json.loads(todos.to_json()), 200


@wikis.route('/<id>')
@wikis.response(404, 'Todo not found')
@wikis.param('id', 'The task identifier')
class WikisApi(Resource):
    def get(self, id):
        '''Fetch a given Todo'''
        try:
            todo = Todo.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except(DoesNotExist):
            abort(404)
        except:
            abort(500)
