import werkzeug
from flask_restx import Namespace, fields, Resource
from werkzeug.datastructures import FileStorage


x_ray = Namespace('v1/x_ray', description='X-Ray')

@x_ray.route('/test')
@x_ray.response(200, 'Success')
class XRayTest(Resource):
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
        image = args['image']
        '''This is where the magic happens'''
        '''TO DO: CALL THE X-RAY model'''
        modelOutput = 'output of the model'
        return {'message': modelOutput}, 200

