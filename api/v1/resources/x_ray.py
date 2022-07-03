from datetime import datetime

import werkzeug
from flask_restx import Namespace, fields, Resource
from werkzeug.datastructures import FileStorage
from api.v1.ai.diagnosis import diagnosisAi

x_ray = Namespace('v1/x_ray', description='X-Ray')
model = diagnosisAi()

@x_ray.route('/chest')
@x_ray.response(200, 'Success')
class XRayTest1(Resource):
    my_resource_parser = x_ray.parser()
    my_resource_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True,
                                    help='Image of the wiki', location='files')

    x_ray_output = x_ray.model('Wiki', {
        'message': fields.String(required=True, description='model output'),
    })

    @x_ray.response(200, 'Success',x_ray_output)
    @x_ray.expect(my_resource_parser)
    def post(self):
        args = self.my_resource_parser.parse_args()
        fileOfImage = args['image']

        img_path=f"{datetime.now().isoformat()}{fileOfImage.filename}"
        fileOfImage.save(img_path)
        '''This is where the magic happens'''
        '''TO DO: CALL THE X-RAY model'''
        modelOutput = model.chest(img_path)
        return {'message': modelOutput}, 200


@x_ray.route('/brain')
@x_ray.response(200, 'Success')
class XRayTest2(Resource):
    my_resource_parser = x_ray.parser()
    my_resource_parser.add_argument('image', type=werkzeug.datastructures.FileStorage, required=True,
                                    help='Image of the wiki', location='files')

    x_ray_output = x_ray.model('Wiki', {
        'message': fields.String(required=True, description='model output'),
    })

    @x_ray.response(200, 'Success',x_ray_output)
    @x_ray.expect(my_resource_parser)
    def post(self):
        args = self.my_resource_parser.parse_args()
        fileOfImage = args['image']

        img_path=f"{datetime.now().isoformat()}{fileOfImage.filename}"
        fileOfImage.save(img_path)
        '''This is where the magic happens'''
        '''TO DO: CALL THE X-RAY model'''
        modelOutput = model.brain(img_path)
        return {'message': modelOutput}, 200

