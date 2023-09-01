import json
import datetime
import yfinance as yf

TODAY = str(datetime.date.today())

def update_dataset(company="TSLA"):

    data = yf.download(company, period="1y")

    data.to_csv(f'datasets/{company}.csv')

    dictionary = {
    	"last_updated": TODAY,
    }

    json_object = json.dumps(dictionary, indent=4)

    with open("config/config.json", "w") as f:
	    f.write(json_object)

def check_dataset_update():

    with open("config/config.json", "r") as f:
        data = json.load(f)
        print(data['last_updated'])

        if data['last_updated'] != TODAY:
            update_dataset()
        
