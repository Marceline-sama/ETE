from flask import Flask, render_template
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

def get_base64_image():
    # Tamanho dos elementos
    size = [2, 1]

    # Rótulos para os elementos
    labels = ['Agua de reuso', 'Espaço disponível']

    # Cores para os elementos
    colors = ['b', 'y']

    # Gráfico em pizza
    fig = plt.figure(figsize=(6, 6))
    ax = fig.add_subplot(111)
    ax.pie(size, labels=labels, colors=colors, autopct='%1.1f%%')
    ax.axis('equal') # Define um aspecto igual para o gráfico

    # Salva o gráfico em um buffer para exibição
    buf = io.BytesIO()
    fig.savefig(buf, format='png')
    buf.seek(0)

    # Converte o buffer em base64
    image_base64 = base64.b64encode(buf.read()).decode('utf-8')
    return image_base64


@app.route('/')
def home():
    return render_template('armazenamento-de-agua.html', image_base64=get_base64_image())


if __name__ == '__main__':
    app.run(debug=True)