#!/usr/bin/python3
import requests
NASAAPI = "https://api.nasa.gov/planetary/apod?"

# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds
#def inquirerange():
    
# this is our main function
def main():
    startdate= ''
    enddate= ''
    dateRange= ''
    difdate= input('would you like to use a date other than today? (y/n)\n').lower()
    if difdate.lower() == 'y':
        askrange= input('Would you like to use a range of dates? (y/n)\n').lower()
        if askrange == 'y':
            rangedateone= input('enter the start date (yyyy-mm-dd)\n').lower()
            rangedatetwo=input('enter the end date (yyyy-mm-dd)\n').lower()
            startdate= '&start_date=' + rangedateone  #delete and change the above 2?
            enddate= '&end_date=' + rangedatetwo      ##########################
            dateRange= startdate + enddate
    ##askmultiple= input('Would you like multiple dates outside of a range? (y/n)\n').lower
        elif askrange == 'n':
            dateRange= '&date=' + input('please enter the one date you would like to see(yyyy-mm-dd)\n').lower()
        else: 
            print('please use y or n to answer')
    ## first grab credentials
    nasacreds = returncreds()
    print(NASAAPI + nasacreds + dateRange)
    ## make a call to NASAAPI with our key
    if difdate == 'y':
        apodresp = requests.get(NASAAPI + nasacreds + dateRange)
        apod = apodresp.json()
    else:
        apodresp = requests.get(NASAAPI + nasacreds)
        apod = apodresp.json()
    ## strip off json
    #print()
    if isinstance(apod, list):
        for x in apod: 
            print('---------------------------------------------------------------------------------------------------------------------------------')
            print(x['title'])
            print('----------------------------------------')
            print(x['date'])
            print('----------------------------------------')
            print(x['explanation'])
            print('----------------------------------------')
            print(x['url'])
            print('---------------------------------------------------------------------------------------------------------------------------------')
    else:
        print(apod["title"] + "\n" + apod["date"] + "\n" + apod["explanation"] + "/n" + apod["url"])

if __name__ == "__main__":
    main()


