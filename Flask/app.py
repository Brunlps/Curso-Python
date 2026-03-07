from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def home():
    end_time = int(time.time()) + 10  # 10 segundos de contagem
    return render_template("index.html", end_time=end_time)

if __name__ == "__main__":
    app.run(debug=True)
