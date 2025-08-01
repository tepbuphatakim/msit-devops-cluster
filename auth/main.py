from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    import socket
    return f'Auth service. v1.0.3 - Public IP: {socket.gethostbyname("8.8.8.8")}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    