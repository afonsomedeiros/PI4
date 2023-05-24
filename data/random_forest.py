import pandas as pd
import pickle


class RandomForest:
    
    def __init__(self, model_file_path: str, data_file_path: str):
        self.file_data_name = data_file_path
        with open(model_file_path, "rb") as self.file:
            self.model = pickle.load(self.file)
            self.data = self.__load_data(data_file_path)

    def __load_data(self, data_file_path: str) -> pd.DataFrame:
        if data_file_path.lower().endswith(".xlsx"):
            return pd.read_excel(data_file_path)
        elif data_file_path.lower().endswith(".csv"):
            return pd.read_csv(data_file_path)
        
    def extract_result(self):
        data = self.model.predict(self.data)
        return pd.DataFrame({'Predido': data})
    
    def extract_data(self):
        result = self.__load_data(self.file_data_name)
        return result.to_json()
