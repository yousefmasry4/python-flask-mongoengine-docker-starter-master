from flask_restx import Namespace, Resource, fields

diagnosis = Namespace('v1/diagnosis', description='X-Ray')


@diagnosis.route('/test')
@diagnosis.response(200, 'Success')
class Test(Resource):
    resource_fields = diagnosis.schema_model(
        'diagnosis', {
            'properties': {
                'questions': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'question': {
                                'type': 'string'
                            },
                            'answer': {
                                'type': 'string'
                            }
                        }
                    }
                }
            },
            'type': 'object'
        })

    my_resource_parser = diagnosis.parser()
    my_resource_parser.add_argument('questions', type=list, required=True,
                                    help='Questions', location='json')

    diagnosisResp = diagnosis.model('diagnosis Resp', {
        'message': fields.String(description='Message'),
    })

    @diagnosis.expect('diagnosisArgs', resource_fields, validate=True, location='json', required=True)
    @diagnosis.response(200, 'Success', diagnosisResp)
    def post(self):
        args = self.my_resource_parser.parse_args()
        '''ToDo: Implement the diagnosis logic'''
        return {'message': args['questions']}
