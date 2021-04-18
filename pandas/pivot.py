from google.colab import files
uploaded = files.upload()
import pandas as pd
import io
df = pd.read_csv(../'SupermarketSales.csv')
