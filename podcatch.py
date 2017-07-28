from flask import jsonify
from flask import abort
from flask import Flask, request, make_response
from flask_restful import Resource, Api
from pymongo import MongoClient
from bson.objectid import ObjectId
from utils.mongo_json_encoder import JSONEncoder


app = Flask(__name__)
mongo = MongoClient('localhost', 27017)
app.db = mongo.develop_database
api = Api(app)

podcasts = [
    {
        'id': 510307,
        'title': u'Invisibilia',
        'link': u'http://www.npr.org/programs/invisibilia',
        'description': u'(Latin for invisible things) is about the invisible forces that control human behavior – ideas, beliefs, assumptions and emotions. Co-hosted by Lulu Miller, Hanna Rosin and Alix Spiegel, <em>Invisibilia</em> interweaves narrative storytelling with scientific research that will ultimately make you see your own life differently.',
        'done': False
    },
    {
        'id': 510308,
        'title': u'Invisibile',
        'link': u'http://www.npr.org/programs/invisibilia',
        'description': u'(Latin for invisible things) is about the invisible forces that control human behavior – ideas, beliefs, assumptions and emotions. Co-hosted by Lulu Miller, Hanna Rosin and Alix Spiegel, <em>Invisibilia</em> interweaves narrative storytelling with scientific research that will ultimately make you see your own life differently.',
        'done': False
    }
]

@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(JSONEncoder().encode(data), code)
    resp.headers.extend(headers or {})
    return resp

@app.route('/podcatch/api/v1.0/podcasts', methods=['GET'])
def get_podcasts():
    return jsonify({'podcasts': podcasts})

@app.route('/podcatch/api/v1.0/podcasts/<int:podcast_id>', methods=['GET'])
def get_task(podcast_id):
    podcast = [podcast for podcast in podcasts if podcast['id'] == podcast_id]
    if len(podcast) == 0:
        abort(404)
    return jsonify({'podcast': podcast[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)
