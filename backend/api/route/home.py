from http import HTTPStatus
from flask import Blueprint, request
from flasgger import swag_from
from api.model.welcome import WelcomeModel

_welcomeModel = WelcomeModel()

home_enpoint = Blueprint('api', __name__)


@home_enpoint.route('/', methods=['GET', 'POST'])
@swag_from({
    'responses':{
        HTTPStatus.OK.value: {
            'description': 'Welcome to the Flask Stater Kit',
        }
    }

})
def welcome():
    if request.method == 'POST':
        return _welcomeModel.welcome_post(request)
    else:

        return _welcomeModel.welcome()


