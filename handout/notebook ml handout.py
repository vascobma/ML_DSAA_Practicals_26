
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

train = train = pd.read_csv("../data/train.csv")
test = pd.read_csv("../data/test.csv")
clientes = pd.read_csv("../data/clientes.csv")

print("Train:", train.shape)
print("Test:", test.shape)
print("Clientes:", clientes.shape)

display(train.head())
display(train.sample(min(5, len(train)), random_state=42))