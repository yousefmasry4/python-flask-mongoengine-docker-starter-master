from flask_restx import Namespace, Resource, fields
from api.v1.ai.prognosis import prognosisAi
from flask import abort
a = prognosisAi()
prognosis = Namespace('v1/prognosis', description='Diabetic_Retinopathy')

def isArrayFloat(array):
    flag = False
    for i in array:
        try:
            float(i)
            flag = True
        except ValueError:
            flag= False
            break
    if flag == False:
        return  False
    else:
        return True

@prognosis.route('/ten_years_death')
@prognosis.response(200, 'Success')
class ten_years_death(Resource):
    resource_fields = prognosis.schema_model(
        'diagnosis', {
            'properties': {
                'array': {
                    'type': 'array',
                    'items': {

                    }
                }
            },
            'type': 'object'
        })

    my_resource_parser = prognosis.parser()
    my_resource_parser.add_argument('array', type=list, required=True, location='json')

    diagnosisResp = prognosis.model('ten_years_death Resp', {
        'message': fields.Float(description='from 0 to 1'),
    })

    @prognosis.expect('ten_years_death', resource_fields, validate=True, location='json', required=True)
    @prognosis.response(200, 'Success', diagnosisResp)
    def post(self):
        args = self.my_resource_parser.parse_args()
        if len(args["array"]) == 5 and isArrayFloat(args["array"]):
            ans= a.ten_years_death(args["array"])
            return {'message': ans}
        return abort(500,'array should be 5 elements and data type is positive float')



@prognosis.route('/Diabetic_Retinopathy')
@prognosis.response(200, 'Success')
class Diabetic_Retinopathy(Resource):
    resource_fields = prognosis.schema_model(
        'diagnosis', {
            'properties': {
                'array': {
                    'type': 'array',
                    'items': {

                    }
                }
            },
            'type': 'object'
        })
    my_resource_parser = prognosis.parser()
    my_resource_parser.add_argument('array', type=list, required=True, location='json')
    diagnosisResp = prognosis.model('ten_years_death Resp', {
        'message': fields.Float(description='from 0 to 1'),
    })

    @prognosis.expect('prognosisArgs', resource_fields, validate=True, location='json', required=True)
    @prognosis.response(200, 'Success', diagnosisResp)
    def post(self):
        args = self.my_resource_parser.parse_args()
        if len(args["array"]) == 10 and isArrayFloat(args["array"]):
            ans = a.Diabetic_Retinopathy(args["array"])
            return {'message': ans}
        return abort(500,'array should be 10 elements and data type is positive float')
