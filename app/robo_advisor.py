# this is the "app/robo_advisor.py" file
#GENERAL ATTRIBUTIONS: a lot of this content was taken from class material, including lecture, class Github, slack, and more.

#import all packages
import requests
import csv
import json
import os
from dotenv import load_dotenv
load_dotenv()

#get the API key from the env
API_key = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

#this function will get the stock ticker from the user
id_list = []
def input_id():
    identifier = input("Please input your desired stock: ")
    #print("identifier", identifier)
    if identifier == "DONE":
        #exit the for loop
        count = 0
    elif 0 < len(identifier) <= 5 and identifier.isalpha():
        #validate
        #stock_list.append(identifier)
        #input_id()
        #print(identifier)
        #print("another identifier: ", identifier)
        id_list.append(identifier)
        #return identifier
    else:
        print("This is not a valid identifier. Please try again!")
        print("For most information about what is considered a valid identifier, please visit:")
        print("https://www.investopedia.com/terms/s/stocksymbol.asp")
        input_id()

input_id()
id1 = id_list[0]
#id1 = input_id(id)
#print("id1: ", id1)
#identifier = input("Please input your desired stock, and type 'DONE' when you are done: ")


#function to convert to USD
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

#request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"

#get the URL
def requesturl(request_url):
    request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=" + id1 + "&apikey=" + API_key
    return request_url

request_url = 0
request_url = requesturl(request_url)
#stock_response = requests.get(request_url)

#-------

#make sure the URL is valid, and if it isnt, send an error and close the code
try:
    stock_response = requests.get(request_url)
    parsed_response = json.loads(stock_response.text)
    date_list = list(parsed_response["Time Series (Daily)"].keys())
except KeyError as e: 
    print("The program was unable to process this stock symbol")
    print("The program is stopping. Try again soon!")
    quit()
 
#ATTRIBUTION: https://stackoverflow.com/questions/16154032/catch-keyerror-in-python
#This Stack Overflow page taught me how to catch a key error

#--------



#do calculations

parsed_response = json.loads(stock_response.text)

date_list = list(parsed_response["Time Series (Daily)"].keys())
recent_date = date_list[0]

#print("todays date: ", recent_date)

request_at = parsed_response["Meta Data"]["3. Last Refreshed"]
#latest_day = parsed_response["Meta Data"]["3. Last Refreshed"]

#latest_close = to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["4. close"]))
latest_close = float(parsed_response["Time Series (Daily)"][recent_date]["4. close"])
latest_close_usd = to_usd(latest_close)
high_price_list = []
high_price = 0

for dates in date_list: #["Time Series (Daily)"][recent_date]
    high_price = float((parsed_response["Time Series (Daily)"][dates]["2. high"]))
    #print(type(high_price))
    high_price_list.append(high_price)

recent_high = to_usd(max(high_price_list))

low_price_list = []
high_price = 0

for dates in date_list: #["Time Series (Daily)"][recent_date]
    high_price = float((parsed_response["Time Series (Daily)"][dates]["2. high"]))
    #print(type(high_price))
    low_price_list.append(high_price)

recent_low = min(low_price_list)
recent_low_usd = to_usd(recent_low)

#print(price_list)

#this formats dates and times to look nice 
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
#ATTRIBUTION: https://www.programiz.com/python-programming/datetime/current-datetime
# This website helped me format date and time for the receipt

#Recommendation decision
#If the stock's latest closing price is less than 15% above its recent low, "Buy", else "Don't Buy".
threshold = 1.15
threshold2 = float(threshold)*float(recent_low)
recommendation = "Null"
recommendation_reason = "Null"

if latest_close < threshold2:
    #print(to_usd(threshold2))
    recommendation = "Buy"
    recommendation_reason = "The stock's latest closing price is less than 15 percent above its recent low"
    #print("invest!")
else:
    #print(to_usd(threshold2))
    recommendation = "Don't Buy"
    recommendation_reason = "The stock's latest closing price is NOT less than 15 percent above its recent low"
    #print("Do not invest!")

#print responses and recommendatino

print("-------------------------")
print("SELECTED SYMBOL: ", id1)
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: ", dt_string) #LOOK AT DATETIME FROM SHOPPING CART PROJECT !!!!!!!!!!!!!!!!!!!!!!!
print("-------------------------")
print("LATEST DAY: ", recent_date)
print("LATEST CLOSE: ", latest_close_usd)
print("RECENT HIGH: ", recent_high)
print("RECENT LOW: ", recent_low_usd)
print("-------------------------")
print("RECOMMENDATION: ", recommendation)
print("RECOMMENDATION REASON: ", recommendation_reason)
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")

#upload to CSV
#csv_file_path = "data/stocks.csv"
csv_file_path = os.path.join(os.path.dirname(__file__), "..", "data", "stocks.csv")
csv_headers = ["timestamp", "open", "high", "low", "close", "volume"]

with open(csv_file_path, "w") as csv_file:
    writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
    writer.writeheader()
    #looping
    for dates in date_list:
        writer.writerow({
            "timestamp": dates,
            "open": parsed_response["Time Series (Daily)"][dates]["1. open"],
            "high": parsed_response["Time Series (Daily)"][dates]["2. high"],
            "low" : parsed_response["Time Series (Daily)"][dates]["3. low"],
            "close": parsed_response["Time Series (Daily)"][dates]["4. close"],
            "volume": parsed_response["Time Series (Daily)"][dates]["5. volume"]
        })

#+++++++++++++++++++++

import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt


csv_filename = "data/stocks.csv"
stocks_df = pd.read_csv(csv_filename)
import seaborn as sns
ax = sns.lineplot(data=stocks_df, x="timestamp", y="close", legend='full')
plt.xlabel("Time - most recent to least")
plt.ylabel("Closing Price (USD)")
plt.title("Stock price over time", size=24)

plt.show()

#ATTRIBUTION: https://stackoverflow.com/questions/26597116/seaborn-plots-not-showing-up
#This website showed me how to display my line plot after I already set it up

        






