import json
from flask import abort
from flask_restx import Namespace, Resource, fields
from api.v1.database.models import Wiki
from api.v1.database.utils.pagination import Pagination
from mongoengine import DoesNotExist

wikis = Namespace('v1/wiki', description='wiki namespace')



@wikis.route('/get_all')
class WikisApi(Resource):
    # @wikis.response(200, 'Success', [model])
    def get(self):
        # model = Wiki()
        # model.image="https://free3d.com/imgd/l67/595667.jpg"
        # model.model="https://free3d.com/imgd/l67/595667.jpg"
        # model.body="asddddddddddddddddddddddddddddddd"
        # model.title="ddd"
        # model.cat="sd"
        # model.save()
        """List all news"""
        todos = Wiki.objects.all()
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
