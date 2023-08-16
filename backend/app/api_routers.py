from flask import jsonify

from . import app

@app.route('/api' , methods=['GET'])
def get_data():
    data = {'message': 'Here is some data from api'}
    return jsonify(data)