import json
from pip._vendor import requests
from datetime import date
from datetime import timedelta



def main():
    choice = input("Enter 'Summary' for a daily summary or 'Date' to search by date: ")
    if choice == "Summary":
        summary()
    elif choice == "Date":
        by_date()

def by_date():
    country = input("Please enter the country that you want to look at: ")
    from_date,to_date = from_to_dates()
    endpoint_url = "https://api.covid19api.com/total/country/{coun}/status/confirmed".format(coun = country)
    params = {"from": from_date, "to": to_date}
    response = requests.get(endpoint_url, params=params)
    covid_data = response.json()
    for each_day in covid_data:
        print("Country: " + each_day.get("Country") + ", Cases: " + str(each_day.get("Cases")) + ", Status: " + each_day.get("Status") + ", Date " + each_day.get("Date"))
    
def summary():
    endpoint_url = "https://api.covid19api.com/summary"
    response = requests.get(endpoint_url)
    covid_data = response.json()
    print(covid_data["Global"])

def from_to_dates():
    from_date = input("Please enter the date you want to start from in YYYY-MM-DD format: ")
    to_date = input("Please enter the date you want to end from in YYYY-MM-DD format: ")
    return from_date,to_date

if __name__ == '__main__':
    main()
