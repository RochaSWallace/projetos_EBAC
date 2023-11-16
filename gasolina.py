import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

gasolina_df = pd.read_csv("gasolina.csv", sep=",")
with sns.axes_style("whitegrid"):

    grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda")
    grafico.set(title="A linha mostra o numeros vendas por dia", xlabel="dia", ylabel="venda")
    grafico.figure.set_size_inches(w=20/2.54, h=10/2.54)
    plt.savefig("gasolina.png")
