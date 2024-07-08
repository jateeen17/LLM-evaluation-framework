import sys
import json

sys.path.append('/home/shodh/evaluation')

class Data:
    def __init__(self):
        self.models_file = '/home/shodh/evaluation/data/models.txt'
        self.datasets_file = '/home/shodh/evaluation/data/datasets.txt'
        self.config_file = '/home/shodh/evaluation/data/config.json'
    
    def load_models(self):
        with open(self.models_file, 'r') as f:
            models = f.read().splitlines()
        return models
    
    def load_datasets(self):
        with open(self.datasets_file, 'r') as f:
            datasets = f.read().splitlines()
        return datasets
    
    # def get_config(self):
    #     with open(self.config_file, 'r') as f:
    #         config = json.load(f)
    #     return config
