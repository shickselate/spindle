from flask import Flask, send_from_directory
app = Flask(__name__)

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, ssl_context=('192.168.0.162.pem', '192.168.0.162-key.pem'))
