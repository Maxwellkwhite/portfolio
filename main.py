from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
import os
from datetime import datetime

app = Flask(__name__)

# Initialize Bootstrap
bootstrap = Bootstrap5(app)

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=["GET", "POST"])
def home_page():
    year = datetime.now().year
    return render_template('index.html', year=year)

if __name__ == "__main__":
    app.run(debug=True, port=5002)




