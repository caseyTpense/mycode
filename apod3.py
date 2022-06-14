#!/usr/bin/python3
# sorry someone walked up with a question

import requests
NASAAPI = "https://api.nasa.gov/planetary/apod?"
#startdate= ''
#enddate= ''
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
    difdate= input('would you like to use a date other than today? (y/n)\n').lower()
    if difdate.lower() == 'y':
        askrange= input('Would you like to use a range of dates? (y/n)\n').lower()
        if askrange == 'y':
            rangedateone= input('enter the start date (yyyy-mm-dd)\n').lower()
            rangedatetwo=input('enter the end date (yyyy-mm-dd)\n').lower()
            startdate= '&start_date=' + rangedateone  #delete and change the above 2?
            enddate= '&end_date=' + rangedatetwo      ##########################
    ##askmultiple= input('Would you like multiple dates outside of a range? (y/n)\n').lower
        elif askrange == 'no':
            date= '&date=' + input('please enter the one date you would like to see')
        else: 
            print('please use y or n to answer')    
        #startdate= '&start_date=' + rangedateone
        #enddate= '&end_date=' + randedatetwo
        #if askrange== 'n':
        #    enddate= startdate= 'date='    
    if difdate.lower() == 'n':
        startdate= ''
    else: 
        print('please use y or n to answer')
    dateRange= startdate + enddate
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


    #print(apod)
    #print()
   
    # looks like the only issue is with the slicing! let's see here...
    if isinstance(apod, list):
        titleValues = [d['title']for d in apod if 'title' in d] # oh wow, this is a list comprehension.
        dateValues = [d['date'] for d in apod if 'date' in d]
        explanationValues = [d['explanation'] for d in apod if 'explanation' in d]
        urlValues = [d['url'] for d in apod if 'url' in d] 
        
    
        print(titleValues)
        print('-------------------------------------------')
        print(dateValues)
        print('-------------------------------------------')
        print(explanationValues)
        print('-------------------------------------------')
        print(urlValues)
        print('-------------------------------------------')
    else:
        print(apod["title"] + "\n" + apod["date"] + "\n" + apod["explanation"] + "/n" + apod["url"])

if __name__ == "__main__":
    main()


