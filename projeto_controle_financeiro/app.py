# Importando o Framework Flask

from flask import Flask

# 1️⃣ Criar a aplicação
app = Flask(__name__)

# 2️⃣ Criar as rotas
@app.route('/')
def home():
    return 'EndFinance está no ar 🚀'

# 3️⃣ Rodar a aplicação
if __name__ == '__main__':
    app.run(debug=True)