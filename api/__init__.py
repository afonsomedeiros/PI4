from bottle import Bottle
from .controllers import create_previsao_route


def create_app():
    api = Bottle()

    create_previsao_route(api)

    return api