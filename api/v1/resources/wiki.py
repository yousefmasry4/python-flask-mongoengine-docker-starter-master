import argparse
import json
import os
import sys

import werkzeug
from flask import abort
from flask_restx import Namespace, fields, Resource
from werkzeug.datastructures import FileStorage

from api.v1.database.models import Wiki
from mongoengine import DoesNotExist
from api.v1.helpers.responses import remove_oid

wikis = Namespace('v1/wiki', description='wiki namespace')

wikiModel = wikis.model('Wiki', {
    'title': fields.String(required=True, description='Title of the wiki'),
    'cat': fields.String(required=True, description='Category of the wiki'),
    'image': fields.String(required=True, description='Image of the wiki'),
    'model': fields.String(required=True, description='3D Model of the wiki'),
    'body': fields.String(required=True, description='Body of the wiki'),
    'id': fields.String(required=True, description='ID of the wiki')
})


@wikis.marshal_with(wikiModel)
@wikis.route('/get_all')
class WikisApi(Resource):
    wikiModelGetList = wikis.model('wikiModelGetList', {
        'title': fields.String(required=True, description='Title of the wiki'),
        'image': fields.String(required=True, description='Image of the wiki'),
        'id': fields.String(required=True, description='ID of the wiki')
    })

    @wikis.response(200, 'Success',[wikiModelGetList])
    def get(self):
        """List all news
        """
        todos = Wiki.objects.all().only('title', 'image', 'id')
        return remove_oid(json.loads(todos.to_json())), 200


@wikis.route('/<id>')
@wikis.response(404, 'Wiki not found')
@wikis.param('id', 'The Wiki identifier')
class WikisApi(Resource):
    @wikis.response(200, 'Success',wikiModel)
    def get(self, id):
        """Fetch a given Wiki"""
        try:
            todo = Wiki.objects.get(id=id)
            return remove_oid(json.loads(todo.to_json())), 200
        except DoesNotExist:
            abort(404)
        except Exception as e:
            print(e)
            abort(500)

    def delete(self, id):
        """Delete a given Wiki"""
        try:
            todo = Wiki.objects.get(id=id)
            try:
                os.remove("./uploads/"+todo.image)
            except:
                pass
            try:
                os.remove("./uploads/"+todo.model)
            except:
                pass
            todo.delete()
            return '', 204
        except DoesNotExist:
            abort(404)
        except:
            abort(500)



@wikis.route('/add_wiki')
@wikis.response(201, 'Wiki created')
class WikisApi(Resource):
    my_resource_parser = wikis.parser()
    my_resource_parser.add_argument('title', type=str, required=True, help='Title of the wiki', location='form')
    my_resource_parser.add_argument('cat', type=str, required=True, help='Category of the wiki', location='form')
    my_resource_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True,
                                    help='Image of the wiki', location='files')
    my_resource_parser.add_argument('model', type=werkzeug.datastructures.FileStorage, required=True,
                                    help='3D Model of the wiki', location='files')
    my_resource_parser.add_argument('body', type=str, required=True, help='Body of the wiki', location='form')

    @wikis.expect(my_resource_parser)
    def post(self):
        """Add a new Wiki"""
        args = self.my_resource_parser.parse_args()
        print(args)

        fileOfImage = args['image']
        fileOf3D = args['model']
        fileOfImage.stream.seek(0)
        fileOfImage.save("./uploads/"+fileOfImage.filename)
        fileOfImage.stream.seek(0)
        fileOf3D.save("./uploads/"+fileOf3D.filename, buffer_size=16384)
        model = Wiki(
            title=args['title'],
            cat=args['cat'],
            image=fileOfImage.filename,
            model=fileOf3D.filename,
            body=args['body']
        )
        model.save()
        return 201
