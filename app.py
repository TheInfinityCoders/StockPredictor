from flask import Flask, render_template
import pandas as pd
from updater import check_dataset_update

# Updates DataSet each and every day
check_dataset_update()

app = Flask(__name__)

DATASET = pd.read_csv(r"datasets/TSLA.csv")

@app.route('/')
def home():

    dates = pd.to_datetime(DATASET['Date']).dt.strftime('%d %b %y').to_string(index=False)
    dates = dates.replace('\n', ',')

    close = DATASET['Close'].to_string(index=False)
    close = close.replace('\n', ',')

    company = "Tesla Inc."

    return render_template("index.html", company=company, labels=dates, close=close)

if __name__ == '__main__':
    app.run(debug=True)