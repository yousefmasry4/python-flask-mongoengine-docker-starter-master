import json
from flask import abort
from flask_restx import Namespace, Resource
from api.v1.database.models import Wiki
from mongoengine import DoesNotExist

wikis = Namespace('v1/wiki', description='wiki namespace')


@wikis.route('/get_all/<page>')
@wikis.param('page', 'page number')
class WikisApi(Resource):
    def get(self, page):
        """List all news"""
        todos = Wiki.objects.skip((page - 1) * 10).limit(10)
        return json.loads(todos.to_json()), 200


@wikis.route('/<id>')
@wikis.response(404, 'Wiki not found')
@wikis.param('id', 'The Wiki identifier')
class WikisApi(Resource):
    def get(self, id):
        """Fetch a given Wiki"""
        try:
            todo = Wiki.objects.get(id=id)
            return json.loads(todo.to_json()), 200
        except DoesNotExist:
            abort(404)
        except:
            abort(500)
