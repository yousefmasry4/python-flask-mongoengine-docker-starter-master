import json
from flask import abort
from flask_restx import Namespace, Resource
from api.v1.database.models import New
from mongoengine import DoesNotExist
import datetime

from api.v1.helpers.responses import remove_oid

news = Namespace('v1/news', description='news namespace')


@news.route('/get_all')
class NewsApi(Resource):
    def get(self):
        # model = New()
        # model.image="https://free3d.com/imgd/l67/595667.jpg"
        # model.body="asddddddddddddddddddddddddddddddd"
        # model.title="ddd"
        # model.sybTitle="ddd"
        # model.date=datetime.datetime.now()
        # model.save()
        """List all news"""
        todos = New.objects.all()
        return remove_oid(json.loads(todos.to_json())), 200


@news.route('/<id>')
@news.response(404, 'new not found')
@news.param('id', 'The new identifier')
class NewsApi(Resource):
    def get(self, id):
        """Fetch a given new"""
        try:
            todo = New.objects.get(id=id)
            return remove_oid(json.loads(todo.to_json())), 200
        except DoesNotExist:
            abort(404)
        except:
            abort(500)
