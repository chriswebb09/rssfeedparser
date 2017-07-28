from flask import Flask, jsonify
from flask import abort
from flask import make_response

app = Flask(__name__)

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

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 403)

if __name__ == '__main__':
    app.run(debug=True)
