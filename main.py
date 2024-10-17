from flask import Flask, render_template

# Configura Flask para usar o diretório 'assets' para arquivos estáticos
app = Flask(__name__, static_folder='assets')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
