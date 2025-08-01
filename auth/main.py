from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    import socket
    return f'Auth service. v1.0.2 - Server IP: {socket.gethostbyname(socket.gethostname())}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    