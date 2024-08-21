from flask import Flask, send_from_directory, abort

app = Flask(__name__)

@app.route('/<path:filename>')
def serve_front_app(filename):
    try:
        return send_from_directory("public", filename)
    except FileNotFoundError:
        abort(404)

#@app.route('/api/re')



if __name__ == '__main__':
    app.run(debug=True)