import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
hh_data = pd.read_csv('dst-3.0_16_1_hh_database.csv', sep=';', engine ='python')
print(hh_data.info())