from flask import Flask, request , jsonify
from flask_restful import Resource, Api

from main import track_v2

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}
    

class PriceData(Resource):

    @app.route('/pricetracker', methods=['POST'])
    def  get_url_data():
        data = request.form.to_dict()
        print('form ', data)
        # print(dir(request))
        # print('data ',request.data)
        print(data['url'])
        print(data['trackprice'])
        price_data = PriceData.process_url(data['url'],int(data['trackprice']))    
        return jsonify(price_data)
        # return data
    def process_url(url,price):
        return track_v2(url,price,False)

    

api.add_resource(PriceData, '/pricetracker')

if __name__ == '__main__':
    app.run(debug=True)







