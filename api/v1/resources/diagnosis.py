import werkzeug
from flask_restx import Namespace, fields, Resource
from werkzeug.datastructures import FileStorage

diagnosis = Namespace('v1/diagnosis', description='X-Ray')


@diagnosis.route('/test')
@diagnosis.response(200, 'Success')
class Test(Resource):
    my_resource_parser = diagnosis.parser()
    my_resource_parser.add_argument('data', location='json', help='provide list of questions '
                                                                  'and answers',
                                    required=True, default='{'
                                                           '"questions": [{'
                                                           '"question": "What is your age?",'
                                                           '"answer": "25"'
                                                           '}]}')
    my_resource_parser.add_argument('data', type=list, location='json', help='provide list of questions '
                                                                             'and answers',
                                    required=True, default='{'
                                                           '"questions": [{'
                                                           '"question": "What is your age?",'
                                                           '"answer": "25"'
                                                           '}]}')

    @diagnosis.expect(my_resource_parser)
    def post(self):
        return {'message': 'Hello World'}
