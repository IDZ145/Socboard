from flask import Flask
from flask_restful import Resource, Api
import bus_test_data

app = Flask(__name__)
api = Api(app)

@app.route("/")
def index():
    return "Hello world."

class GetBusesHighSt(Resource):
    def get(self):
        return bus_test_data.getHighStTestData()

class GetBusesAnzacPde(Resource):
    def get(self):
        return {"Anzac": "Parade"}

class GetBusesExpress(Resource):
    def get(self):
        return {"UNSW": "Express"}

api.add_resource(GetBusesHighSt, '/getbuseshighst')
api.add_resource(GetBusesAnzacPde, '/getbusesanzacpde')
api.add_resource(GetBusesExpress, '/getbusesexpress')

if __name__ == '__main__':
    app.run()
