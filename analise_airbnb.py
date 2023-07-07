import pandas as pd
import matplotlib.pyplot as plt

dados = {
    'bairro': ['Bairro A', 'Bairro B', 'Bairro C', 'Bairro D', 'Bairro E'],
    'preco': [100, 150, 120, 80, 200],
    'numero_quartos': [2, 3, 1, 2, 4],
    'avaliacao': [4.5, 4.8, 3.9, 4.2, 4.7]
}

data = pd.DataFrame(dados)

media_precos = data['preco'].mean()
print("Média de preços dos aluguéis:", media_precos)

bairros_populares = data['bairro'].value_counts().head(5)
print("Bairros mais populares:")
print(bairros_populares)

data.groupby('bairro')['preco'].mean().plot(kind='bar', figsize=(10, 6))
plt.xlabel('Bairro')
plt.ylabel('Preço Médio')
plt.title('Preços Médios dos Aluguéis por Bairro')
plt.xticks(rotation=45)
plt.show()
