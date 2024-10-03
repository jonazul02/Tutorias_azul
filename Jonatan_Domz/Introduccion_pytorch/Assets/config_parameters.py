import yaml
from yaml.loader import SafeLoader
import pandas as pd
import json
import numpy as np
import os


class InitConfigLoader:

    @staticmethod
    def get_config(file_path='../Jonatan_Domz/Introduccion_pytorch/Paths/paths.yml'):
        with open(file_path, "r", encoding='utf-8') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=SafeLoader)
        return cfg


    @staticmethod
    def get_a_yml(file_path):
        with open(file_path, "r", encoding='utf-8') as ymlfile:
            cfg = yaml.load(ymlfile, Loader=SafeLoader)
        return cfg
    
    @staticmethod
    def get_a_pd_df(file_path):
        return pd.read_csv(file_path)
    
    @staticmethod
    def get_a_json(file_path):

        json_file = open(file_path, encoding='utf-8')
        json_data = json.load(json_file, strict=False)
        return json_data

    @staticmethod
    def write_df_to_csv(df, file_path):
        df.to_csv(file_path, index=False)

