import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
gasolina_df = pd.read_csv("gasolina.csv", sep=",")
with sns.axes_style("whitegrid"):

    grafico = sns.lineplot(data=gasolina_df, x="dia", y="venda")
    grafico.set(title="A linha mostra o numeros vendas por dia", xlabel="dia", ylabel="venda")
    plt.savefig("gasolina.png")
