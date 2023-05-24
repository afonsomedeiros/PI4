import os
import csv
from bottle import Bottle, response, request
from data.random_forest import RandomForest
from CONST import ROOT_PATH


def create_previsao_route(app: Bottle):

    @app.get("/previsao")
    def previsao():
        response.content_type = "application/json"
        response.status = 200

        model_path = os.path.join(ROOT_PATH, "data/modelo_random_forest.pkl")
        data_path = os.path.join(ROOT_PATH, "data/Realizar_Predicao.xlsx")
        rf = RandomForest(model_path, data_path)
        return rf.extract_result().to_json()
        
    @app.get("/dados")
    def dados():
        response.content_type = "application/json"
        response.status = 200

        model_path = os.path.join(ROOT_PATH, "data/modelo_random_forest.pkl")
        data_path = os.path.join(ROOT_PATH, "data/Realizar_Predicao.xlsx")
        rf = RandomForest(model_path, data_path)
        return rf.extract_data()
    

    @app.post("/enviar")
    def enviar():
        json = request.json
        try:
            json = dict(json)
            path = os.path.join(ROOT_PATH, "data")
            files = os.listdir(path)
            csv_count = 1
            for file in files:
                if file.endswith(".csv"):
                    csv_count += 1
            csv_path = os.path.join(path, f"csv_re_pred_{csv_count}.csv")
            with open(csv_path, "w") as infile:
                headers = json["data"][0].keys()
                writer = csv.DictWriter(infile, fieldnames=headers)
                writer.writeheader()
                writer.writerows(json["data"])

            response.content_type = "application/json"
            response.status = 200
            model_path = os.path.join(ROOT_PATH, "data/modelo_random_forest.pkl")
            rf = RandomForest(model_path, csv_path)
            return rf.extract_result().to_json()
        except Exception as e:
            raise e