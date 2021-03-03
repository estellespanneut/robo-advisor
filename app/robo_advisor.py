# this is the "app/robo_advisor.py" file

#this function takes the stock ticker


#this function takes the stock IDs

import requests
import csv
import json
import os

#function to convert to prices
def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    Param: my_price (int or float) like 4000.444444
    Example: to_usd(4000.444444)
    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

request_url = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo"
stock_response = requests.get(request_url)

parsed_response = json.loads(stock_response.text)

date_list = list(parsed_response["Time Series (Daily)"].keys())
recent_date = date_list[0]

print("todays date: ", recent_date)


latest_day = parsed_response["Meta Data"]["3. Last Refreshed"]
latest_close = to_usd(float(parsed_response["Time Series (Daily)"][latest_day]["4. close"]))

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

recent_low = to_usd(min(low_price_list))

#print(price_list)


print("-------------------------")
print("SELECTED SYMBOL: XYZ")
print("-------------------------")
print("REQUESTING STOCK MARKET DATA...")
print("REQUEST AT: 2018-02-20 02:00pm") #LOOK AT DATETIME FROM SHOPPING CART PROJECT
print("-------------------------")
print("LATEST DAY: ", latest_day)
print("LATEST CLOSE: ", latest_close)
print("RECENT HIGH: ", recent_high)
print("RECENT LOW: ", recent_low)
print("-------------------------")
print("RECOMMENDATION: BUY!")
print("RECOMMENDATION REASON: TODO")
print("-------------------------")
print("HAPPY INVESTING!")
print("-------------------------")


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

        
quit()





count = 0

def input_id():
    identifier = input("Please input your desired stock or cryptocurrency symbols, and type 'DONE' when you are done: ")
    if identifier == "DONE":
        #exit the for loop
        count = count - 1
    elif identifier:
        #validate
        stock_list.append(identifier)
        count = count + 1
        input_id()
    else:
        print("This is not a valid identifier. Please try again!")
        input_id()

input_id()
