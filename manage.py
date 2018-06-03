from flask import Flask
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    print(app.url_map)
    app.run()