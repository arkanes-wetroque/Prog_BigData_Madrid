import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#This file will be the data getter and washer

file2017 = 'Datas/VEHICULOS_PARQUE_MOVIL_2017.csv'
d17 = pd.read_csv(file2017, delimiter=';')

# Give clean dataframe to
def getDataframeSimple():
  print(d17.shape)
  print(d17.duplicated())
  d17Clean = d17.drop_duplicates()
  return d17Clean




