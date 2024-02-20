import fasttext
import numpy as np
import pandas as pd


class NameDistance():
    def __init__(self, ft_model_path: str = 'data/cc.en.50.bin'):
        self.ft_model = fasttext.load_model(ft_model_path)