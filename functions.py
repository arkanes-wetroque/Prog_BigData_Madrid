import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#This file will be functions calc one and charts

def typeConso(dataframe):
    conso = dataframe.groupby('ENERG�A/COMBUSTIBLE')['N� MPAL'].nunique()
    return conso



