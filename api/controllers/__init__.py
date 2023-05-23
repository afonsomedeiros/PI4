import os
from bottle import Bottle, response
from data.random_forest import RandomForest
from CONST import ROOT_PATH


def create_previsao_route(app: Bottle):

    @app.get("/previsao")
    def previsao():
        model_path = os.path.join(ROOT_PATH, "data/modelo_random_forest.pkl")
        data_path = os.path.join(ROOT_PATH, "data/Realizar_Predicao.xlsx")
        rf = RandomForest(model_path, data_path)
        return rf.extract_result().to_json()
        