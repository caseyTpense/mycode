#!/usr/bin/python3

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

# this is our main function
def main():
    startdate= ''
    enddate= ''
    difdate= input('would you like to use a date other than today? (y/n)').lower()
    if difdate== 'y'.lower():
        startdate= '&start_date' + '=' + input('type the desired date in yyyy-mm-dd format')
        enddate= '&end_date' + '=' + input('If you would like an end date tpye it in yyy-mm-dd format otherwise type "n"')
        if enddate== 'n':
            enddate= ''
        else: print('please use yyy-mm-dd format')    
    if difdate== 'n':
        startdate= ''
    else: 
        print('please use y or n to answer')
    dateRange= startdate + enddate
    ## first grab credentials
    nasacreds = returncreds()

    ## make a call to NASAAPI with our key
    if difdate == 'y':
        apodresp = requests.get(NASAAPI + nasacreds + dateRange)
        apod = apodresp.json()
    else:
        apodresp = requests.get(NASAAPI + nasacreds)
        apod = apodresp.json()
    ## strip off json


    print(apod)

    print()
    
    #titlesKey= "title"
    #dateKey= "date"
    #explanationkey = "explanation"
    #urlKey="url"
    
    titleValues = [d['title'] for d in apod]
    dateValues = [d['date'] for d in apod]
    explanationValues = [d['explanation'] for d in apod]
    urlValues = [d['url'] for d in apod]
    fullValue = titleValues, "\n",  dateValues, "\n", explanationValues, "\n", urlValues
    
    print(fullValue)
            
if __name__ == "__main__":
    main()


