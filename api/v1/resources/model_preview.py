import json
from flask import abort
from flask_restx import Namespace, fields, Resource

from api.v1.database.models import Wiki
from mongoengine import DoesNotExist
from api.v1.helpers.responses import remove_oid

preview_model = Namespace('v1/preview_model', description='Preview 3D model')

preview_3d_Model = preview_model.model('preview_model', {
    'id': fields.String(required=True, description='Wiki ID'),
    'model': fields.String(required=True, description='3D model file'),
    'title': fields.String(required=True, description='Title of the wiki'),
    'cat': fields.String(required=True, description='Category of the wiki'),
    'body': fields.String(required=True, description='Body of the wiki'),
})


@preview_model.route('/<title>')
@preview_model.response(404, 'model not found')
@preview_model.param('title', 'Title of the model')
class preview_modelApi(Resource):
    @preview_model.response(200, 'Success', preview_3d_Model)
    def get(self, title):
        """Fetch a given model"""
        try:
            todo = Wiki.objects(title=title).first()
            return remove_oid(json.loads(todo.to_json())), 200
        except DoesNotExist:
            abort(404)
        except Exception as e:
            print(e)
            abort(500)
