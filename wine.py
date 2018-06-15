import numpy as np
import matplotlib.pyplot as plt
import matplotlib as matplot
import seaborn as sns
import pandas as pd
df = pd.read_csv('../wine-reviews/winemag-data-130k-v2.csv', index_col=None)
print df.head()