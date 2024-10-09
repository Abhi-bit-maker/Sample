import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
#from wordcloud import WordCloud, STOPWORDS
#from collections import Counter
import pandas as pd
#import warnings
#warnings.filterwarnings('ignore')

df = pd.read_csv("car_price_prediction_.csv")

print(df.head())

print(df.shape)

print(df.isnull().sum())

print(df.info())

print(df.isna().sum())

print(df.describe())

pc= df.describe().T.plot(kind="bar")

pc.set_title("Analytics")
pc.set_ylabel("Mileage")
pc.set_xlabel("Features")

plt.savefig("histogram.png", dpi=300, bbox_inches="tight")

