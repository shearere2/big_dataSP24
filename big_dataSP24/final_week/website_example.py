import flask

app = flask.Flask('API')


@app.route('/')
def heartbeat():
    return flask.jsonify({'alive':True})

@app.route('/math', methods=['GET'])
def compute_math():
    number = flask.request.args.get('number')
    return flask.jsonify({'status':True,'number':int(number)*10})

@app.route('/thesaurus',methods=['GET'])
def etim():
    return flask.render_template('etim.html')


if __name__ == "__main__":
    app.run(port=8000)
