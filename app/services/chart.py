import io
import matplotlib.pyplot as plt

def criar_grafico(x, y):
    # Crie um gráfico de dispersão
    plt.bar(x, y)

    # Defina o título e os rótulos dos eixos
    plt.title("Gráfico de RPK por data")
    plt.xlabel("Data")
    plt.ylabel("RPK")

    # Mostre o gráfico (opcional)
    # plt.show()

    # Salve o gráfico em um arquivo (opcional)
    # plt.savefig("grafico.png")

    # Converter o gráfico em bytes
    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    # Retorna o gráfico como bytes
    return buffer.read()