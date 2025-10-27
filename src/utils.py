import os
import sys

import pandas as pd
import numpy as np
import dill
from src.exceptions import CustomException


# Function to save the object to a file (pkl) from data transformation file.
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)