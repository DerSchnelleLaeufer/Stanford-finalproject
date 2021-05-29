# Author: Louis Renner
# Version: 0.1
# COVID-19/ SARS-CoV-2 Dashboard for my travel
# This program shall give me an overview of the current cases in my most frequented cities in Germany
# The purpose of this program is to make my life easier and make it much harder for me to miss out on the current
# measures to be applied, when travelling to a particular places (parents, friends, work, etc.)

"""
Data Sources JHU: COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at
Johns Hopkins University (JHU CSSE COVID-19 Data)
available at https://github.com/CSSEGISandData/COVID-19

Data Sources RKI: ArcGIS Dashboard Information from
https://npgeo-corona-npgeo-de.hub.arcgis.com/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/about
"""

# import csv
# import requests
from datetime import date
import pandas as pd
from urllib import request

# Data from JHU on Github available.
# Need a way to parse the current data with ".csv" at the end
BASE_URL_DATASOURCE_JHU = "https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_daily_reports/"
BASE_URL_DATASOURCE_RKI = "https://opendata.arcgis.com/api/v3/datasets/dd4580c810204019a7b8eb3e0b329dd6_0/downloads/data?format=csv&spatialRefId=4326"
BASE_DATA_JHU = "data/JHU_COVID19.csv"
BASE_DATA_RKI = "data/RKI_COVID19.csv"


def main():
    # TODO: Find a suitable sequence for executing the file
    # Main function of my program
    print(f"\nThis program gives you an COVID-19 indication of the current state at given locations in Germany\n")

    # TODO: Take out the initial prompt, if the user wishes to continue.
    # A test to ask user, whether he wishes to continue
    """# While loop for input validation, nothing except "y" or "n" is allowed
    user_input = input("Are you ready? (y/n) : ")
    while user_input == "y" or "n":
        if user_input == "y":
            #print(f"Today is the {current_date}")
            print(f"Today is the {current_day}-{current_month}-{current_year} OR in short {today}")
            print(f"\nThis is a test")
            print(f"{full_url_jhu}")
            #return full_url_jhu
            #break
        if user_input == "n":
            print("OK LOL")
            break
        else:
            print("That did not work. It seems you did not answer (y)es or (n)o.")
            user_input = input("Are you ready? (y/n) : ")"""

    # Get a viable date for the latest COVID-19 data (from previous day, as data of current day is still being polled)
    today, current_day, current_month, current_year = find_current_date()
    print(f"Base URL: {BASE_URL_DATASOURCE_JHU}")

    # Put together the relevant data as strings to allow for downloading the relevant COVID-19 data
    # Return the variable "full_url_jhu" now, else the function get_new_data() will not work
    full_url_jhu = BASE_URL_DATASOURCE_JHU + str(current_month) + "-" + str(current_day) + "-" + str(current_year) + ".csv"
    full_url_rki = BASE_URL_DATASOURCE_RKI
    print(f"Full JHU URL: {full_url_jhu}\n")
    print(f"Full RKI URL: {full_url_rki}\n")

    # Get the current data from JHU based on the full url listed above
    # get_new_data(full_url_jhu, full_url_rki)
    # get_new_data(full_url_jhu)

    # Setup a variable containing the dataframe for further analysis/ visualization
    # parse_new_data()
    df_jhu_covid19 = pd.read_csv(full_url_jhu)
    df_rki_covid19 = pd.read_csv(full_url_rki)

    # Print to allow check for function
    print("### Info from JHU ###")
    print(f"{df_jhu_covid19}\n")

    # Export the df to local
    df_jhu_covid19.to_csv("data/JHU_COVID19.csv")


    print("### Info from RKI ###")
    print(f"{df_rki_covid19}\n")

    # Export the df to local
    df_rki_covid19.to_csv("data/RKI_COVID19.csv")

    # Finish program and say bye, bye
    print("Ok, bye for now")


def find_current_date():
    # Define an object for today's date
    today = date.today()
    # current_date = today.strftime("%d") - 1
    # Function to generate current date in correct format (01-02-2021 --> mm-dd-yyyy --> datetime-format %m-%d-%Y)
    current_day = int(today.strftime("%d")) - 1
    current_month = today.strftime("%m")
    current_year = today.strftime("%Y")
    return today, current_day, current_month, current_year


# Try Nr. 2 for retrieving the CSV file --> Works for JHU
def get_new_data(url1):
    # JHU DATA
    # Retrieve the CSV from Github as a webpage
    response_url1 = request.urlopen(url1)
    csv = response_url1.read()

    # Save the string to a file
    csvstr = str(csv).strip("b'")

    lines = csvstr.split("\\n")
    f = open("data/JHU_COVID19.csv", "w", encoding="utf-8")
    for line in lines:
        f.write(line + "\n")
    f.close()


"""
# TODO: Investigate the structure of the different data sources (RKI, WHO, JHU)
def parse_new_data():
    # Read CSV file into a dataframe so it becomes available to pandas
    df_jhu_covid19 = pd.read_csv(BASE_DATA_JHU)
    df_rki_covid19 = pd.read_csv(BASE_DATA_RKI)

    # Make the dataframe available to other functions of this program
    return df_jhu_covid19, df_rki_covid19
"""

# TODO: Find a solution on how to extract the correct data.


# TODO: Use pandas to create basic visualizations of the data
"""def visualization_of_data(state):
    pass
    # logic for warning of rising numbers
    # if the cases have been rising for hte previous 4 days, create a warning
    if cases_day_five < cases_day_four and cases_day_four < cases_day_t-three < cases_day_two and cases_day_t-two < cases_day_t-one and cases_day_t-one < cases_day_today:
        print("Warning, the cases for {location} have been rising continuously for the previous 4 days")
"""


# Python stuff to let the interpreter know what to do :-)
if __name__ == '__main__':
    main()

# Placeholder for "older" stuff, i.e. unused code

"""
    # RKI DATA
    # Retrieve the CSV from arcgis RKI repo
    response_url2 = request.urlopen(url2)
    csv = response_url2.read()

    # Save the string to a file
    csvstr = str(csv).strip("b'")

    lines = csvstr.split("\\n")
    f = open("data/RKI_COVID19.csv", "w", encoding="UTF-8")
    for line in lines:
        f.write(line + "\n")
    f.close()
"""

"""
def get_new_data(url1):
    # TODO: Build a function that downloads the latest .csv file from Github
    # TODO: Use requests to download the data from RKI ()

    # JHU Data retrieval by using the full url of the "current" data for COVID-19 - set it as an url for requests
    # use r to shorten the function because lazy
    r1 = requests.get(url1)

    # This solution with csv and requests works like a charm for JHU data
    # Apart from adding empty lines to the csv file
    # with open('data/JHU_COVID19.csv', 'w') as f:
    with open('data/JHU_COVID19.csv', 'w') as f:
        writer = csv.writer(f)
        for line in r1.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))

    if url2 != 0:
        # with open('data/RKI_COVID19.csv', 'w') as f: --> TODO: What does 'w' do?
        with open('data/RKI_COVID19.csv') as f:
            writer = csv.writer(f)
            for line in r1.iter_lines():
                writer.writerow(line.decode('utf-8').split(','))


second - modular part of the data receiver
    r2 = requests.get(url2)
    with open('data/RKI_COVID19.csv', 'w') as f:
        writer = csv.writer(f)
        for line in r2.iter_lines():
            writer.writerow(line.decode('utf-8').split(','))
"""

