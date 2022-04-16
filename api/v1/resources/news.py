import json
import os
import sys

import werkzeug
from flask import abort
from flask_restx import Namespace, Resource, fields
from api.v1.database.models import New
from mongoengine import DoesNotExist
import datetime
from werkzeug.datastructures import FileStorage
from api.v1.helpers.responses import remove_oid

news = Namespace('v1/news', description='news namespace')

newsModel = news.model('news', {
    'title': fields.String(required=True, description='title of the news'),
    'body': fields.String(required=True, description='content of the news'),
    'date': fields.DateTime(required=True, description='date of the news'),
    'sybTitle': fields.String(required=True, description='author of the news'),
    'image': fields.String(required=True, description='image of the news'),
})


@news.marshal_with(newsModel)
@news.route('/get_all')
class NewsApi(Resource):
    newsGetAll = news.model('List all news', {
        'title': fields.String(required=True, description='title of the news'),
        'date': fields.DateTime(required=True, description='date of the news'),
        'sybTitle': fields.String(required=True, description='author of the news'),
        'image': fields.String(required=True, description='image of the news'),
        'id': fields.String(required=True, description='id of the news')
    })

    @news.response(200, 'Success', [newsGetAll])
    def get(self):
        """List all news"""
        todos = New.objects.all().only('title', 'date', 'sybTitle', 'image')
        return remove_oid(json.loads(todos.to_json())), 200


@news.route('/<id>')
@news.response(404, 'new not found')
@news.param('id', 'The new identifier')
class NewsApi(Resource):
    newsGetOne = news.model('Fetch a given new', {
        'title': fields.String(required=True, description='title of the news'),
        'body': fields.String(required=True, description='content of the news'),
        'date': fields.DateTime(required=True, description='date of the news'),
        'sybTitle': fields.String(required=True, description='author of the news'),
        'image': fields.String(required=True, description='image of the news'),
        'id': fields.String(required=True, description='id of the news')
    })

    @news.marshal_with(newsGetOne)
    def get(self, id):
        """Fetch a given new"""
        try:
            todo = New.objects.get(id=id)
            return remove_oid(json.loads(todo.to_json())), 200
        except DoesNotExist:
            abort(404)
        except:
            abort(500)

    def delete(self, id):
        """Delete a given new"""
        try:
            todo = New.objects.get(id=id)
            todo.delete()
            return '', 204
        except DoesNotExist:
            abort(404)
        except:
            abort(500)


@news.route('/add_new')
@news.response(201, 'new successfully created')
class NewsApi(Resource):
    my_resource_parser = news.parser()
    my_resource_parser.add_argument('body', type=str, required=True, help='Body of the new', location='form')
    my_resource_parser.add_argument('title', type=str, required=True, help='Title of the new', location='form')
    my_resource_parser.add_argument('sybTitle', type=str, required=True, help='Subtitle of the new', location='form')
    my_resource_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True,
                                    help='Image of the wiki', location='files')

    @news.expect(my_resource_parser)
    def post(self):
        """Add a new new"""
        args = self.my_resource_parser.parse_args()
        print(args)

        fileOfImage = args['image']
        os.chdir(os.getcwd()+"/uploads/")

        fileOfImage.stream.seek(0)

        fileOfImage.save("./uploads/"+fileOfImage.filename)
        fileOfImage.stream.seek(0)
        isoDate = datetime.datetime.now().isoformat()
        model = New(
            title=args['title'],
            image=fileOfImage.filename,
            body=args['body'],
            sybTitle=args['sybTitle'],
            date=isoDate,
        )
        model.save()
        return 201
