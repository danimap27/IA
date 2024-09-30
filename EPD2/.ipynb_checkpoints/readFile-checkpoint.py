import pandas as pd

def readFile(file_name):
    df = pd.read_csv(file_name, names=["Poblacion","Beneficio"],delimiter=",")
    X = pd.DataFrame({"Poblacion": df["Poblacion"]})
    y = pd.DataFrame({"Beneficio": df["Beneficio"]})
    return X, y