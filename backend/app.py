
from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flasgger import Swagger
from api.route.home import home_enpoint


def create_app():
    app = Flask(__name__)
    app.config['SWAGGER']= {
        'title': 'Flask API Starter Kit'
    }

    swagger = Swagger(app)
    app.register_blueprint(home_enpoint, url_prefix='/api')


    return app



if __name__ == '__main__':
    app = create_app()
    app.run(host='localhost', port=5000, debug=True)






