from flask import Flask, render_template, request
import pandas as pd
from updater import check_dataset_update

# Updates DataSet each and every day
check_dataset_update()

app = Flask(__name__)

DATASET = pd.read_csv(r"datasets/TSLA.csv")

def set_default_values():

    N = len(DATASET['Date'])

    dates_lst = pd.to_datetime(DATASET['Date']).dt.strftime('%d %b %y').to_string(index=False)
    dates = dates_lst.replace('\n', ',')

    close = DATASET['Close'].to_string(index=False)
    close = close.replace('\n', ',')

    range = pd.to_datetime(DATASET['Date']).dt.strftime('%b %Y')[0]+ ' - ' + pd.to_datetime(DATASET['Date']).dt.strftime('%b %Y')[N-1]

    print(DATASET['Date'][N-1])

    company = "Tesla Inc."

    ticker = "TSLA"

    return {
        "dates": dates,
        "close": close,
        "company": company,
        "range": range,
        "ticker": ticker,
        "last_work_date": pd.to_datetime(DATASET['Date']).dt.strftime('%d %b %Y')[N-1],
        "last_open": DATASET['Open'][N-1].round(2),
        "last_close": DATASET['Close'][N-1].round(2),
        "last_high": DATASET['High'][N-1].round(2),
        "last_low": DATASET['Low'][N-1].round(2),
        "last_adj_close": DATASET['Adj Close'][N-1].round(2),
        "last_volume": DATASET['Volume'][N-1],
    }

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':

        values = set_default_values()

        # pred_data = unfe

        return render_template("index.html",
                                company=values['company'], 
                                ticker=values['ticker'],
                                labels=values['dates'], close=values['close'], 
                                range=values['range'], 
                                last_work_date=values['last_work_date'], 
                                last_open=values['last_open'], last_close=values['last_close'],last_high=values['last_high'], last_low=values['last_low'],last_adj_close=values['last_adj_close'], 
                                last_volume=values['last_volume'],
                                # pred_data=pred_data,
                                )
    
    if request.method == 'POST':

        values = set_default_values()
        
        date = request.form['pred_date']

        #?Predict Using Model Here

        # pred_data = "Got your request"+date

        pred_data = "245.01 USD"

        return render_template("index.html", 
                               company=values['company'], 
                               ticker=values['ticker'],
                               labels=values['dates'], close=values['close'], 
                               range=values['range'], 
                               last_work_date=values['last_work_date'], 
                               last_open=values['last_open'], last_close=values['last_close'],last_high=values['last_high'], last_low=values['last_low'],last_adj_close=values['last_adj_close'], 
                               last_volume=values['last_volume'],
                               pred_data=pred_data,
                               )

if __name__ == '__main__':
    app.run(debug=True)