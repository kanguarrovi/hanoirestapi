import re
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class HanoiRESTAPI(Resource):

    def __init__(self, *args, **kwargs):
        super(HanoiRESTAPI, self).__init__(*args, **kwargs)
        self.count = 1  # Index of the steps.
        self.steps = []  # List of steps

    def __hanoi_algorithm(self, disks, borigen="Borigen", bintermedio="Bintermedio", bdestino="Bdestino"):
        if disks > 0:
            self.__hanoi_algorithm(disks - 1, borigen, bdestino, bintermedio)
            self.steps.append(
                {self.count: "Move disk from {borigen} to {bdestino}".format(borigen=borigen, bdestino=bdestino)}
            )
            self.count += 1
            self.__hanoi_algorithm(disks - 1, bintermedio, borigen, bdestino)

    def post(self):

        parser = reqparse.RequestParser()
        parser.add_argument('disks')
        args = parser.parse_args()

        if not re.match(r'^\d*$', args['disks']):  # Accepts only positive numbers.
            return {'message': "Please assign to 'disks' a valid quantity"}

        disks = int(args['disks'])

        if disks >= 20:
            return {'message': "MAX disks quantity is 19"}

        self.__hanoi_algorithm(disks=disks)

        return {'steps': self.steps}


api.add_resource(HanoiRESTAPI, '/hanoirestapi')

if __name__ == '__main__':
    app.run(debug=True)

