import io
import matplotlib.pyplot as plt

def create_chart(x, y):
    plt.bar(x, y)

    plt.title("Gráfico de RPK por data")
    plt.xlabel("Data")
    plt.ylabel("RPK")

    buffer = io.BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    
    return buffer.read()