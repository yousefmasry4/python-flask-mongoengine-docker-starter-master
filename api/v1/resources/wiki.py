import argparse
import json
import os

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
})


@wikis.route('/get_all')
class WikisApi(Resource):
    def get(self):
        # model = Wiki()
        # model.image="https://free3d.com/imgd/l67/595667.jpg"
        # model.model="https://free3d.com/imgd/l67/595667.jpg"
        # model.body="asddddddddddddddddddddddddddddddd"
        # model.title="ddd"
        # model.cat="sd"
        # model.save()
        """List all news
        """
        todos = Wiki.objects.all()
        return remove_oid(json.loads(todos.to_json())), 200


@wikis.route('/<id>')
@wikis.response(404, 'Wiki not found')
@wikis.param('id', 'The Wiki identifier')
class WikisApi(Resource):
    def get(self, id):
        """Fetch a given Wiki"""
        try:
            todo = Wiki.objects.get(id=id)
            return remove_oid(json.loads(todo.to_json())), 200
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
    my_resource_parser.add_argument('image', type= werkzeug.datastructures.FileStorage , required=True, help='Image of the wiki', location='files')
    my_resource_parser.add_argument('model', type=werkzeug.datastructures.FileStorage, required=True, help='3D Model of the wiki', location='files')
    my_resource_parser.add_argument('body', type=str, required=True, help='Body of the wiki', location='form')

    @wikis.expect(my_resource_parser)
    def post(self):
        """Add a new Wiki"""
        args = self.my_resource_parser.parse_args()
        print(args)

        # if Wiki.objects(title=args['title']):
        #     return {"message": "Wiki already exists"}, 400

        fileOfImage = args['image']
        fileOf3D = args['image']
        print(os.getcwd())
        os.chdir("/home/youssef/PycharmProjects/python-flask-mongoengine-docker-starter-master/uploads")
        fileOfImage.save(fileOfImage.filename)
        fileOf3D.save(fileOf3D.filename)
        model = Wiki(
            title=args['title'],
            cat=args['cat'],
            image=fileOfImage.filename,
            model=fileOf3D.filename,
            body=args['body']
        )
        model.save()
        return 201


