#!/usr/bin/python3
import requests
import pyfiglet
# sets functions for format
def line():
    print('_____________________________________________________________________________________________________________________________________________________________')
def sline():
     print('----------------------------------------')
# this function grabs our credentials
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/mycode/finalproject/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds
    
# utilizes the apod feature of nasas API
def apod():
    startdate= '' #initial set of start date variable
    enddate= '' #initial set of enddate variable
    dateRange= ''#initial set of dateRange variable
    difdate= input('would you like to use a date other than today? (y/n)\n').lower() #asks users if they would like to use something other than the default of today
    if difdate.lower() == 'y':
        askrange= input('Would you like to use a range of dates? (y/n)\n').lower() #asks user if they would like to use a range of dates instead of just one date
        if askrange == 'y':
            rangedateone= input('enter the start date (yyyy-mm-dd)\n').lower() #requests start date from user
            rangedatetwo=input('enter the end date (yyyy-mm-dd)\n').lower() #requests end date from user
            startdate= '&start_date=' + rangedateone #sets input to startdate preceded by NASAAPI start date parameter
            enddate= '&end_date=' + rangedatetwo    #sets input to enddate preceded by NASAAPI end date parameter  
            dateRange= startdate + enddate
        else:
            specificdate= input('enter the date you would like to use(yyyy-mm-dd)\n').lower()
            dateRange= '&date=' + specificdate
    NASAAPI = "https://api.nasa.gov/planetary/apod?" #defines the API used
    ## first grab credentials
    nasacreds = returncreds()
    print(NASAAPI + nasacreds + dateRange) #displays the requested inputs
    if difdate == 'y':
        apodresp = requests.get(NASAAPI + nasacreds + dateRange) # makes call to NASAAPI with key and date range
        apodlist = apodresp.json() #strips jsom
    else:
        apodresp = requests.get(NASAAPI + nasacreds) #makes call to NASAAPI with our key
        apodlist = apodresp.json() #strips json
    #displays the data requested for range of daates or different date
    if isinstance(apodlist, list):
        for x in apodlist: 
            line()
            print(x['title'])
            sline()
            print(x['date'])
            sline()
            print(x['explanation'])
            sline()
            print(x['url'])
            line()
    #displays the data of today's entry
    else:
        print(apodlist["title"] + "\n" + apodlist["date"] + "\n" + apodlist["explanation"] + "/n" + apodlist["url"])

#defines near earth objects API
def neo():
    #defines variables used for formating utlizing pyfiglet
    feedfig= pyfiglet.figlet_format('FEED')
    lookupfig= pyfiglet.figlet_format('LOOKUP')
    browsefig= pyfiglet.figlet_format('BROWSE')
    print(feedfig, '\n Retrieve a list of Asteroids based on their closest approach date to Earth.\n', lookupfig, '\n Lookup a specific Asteroid based on its NASA JPL small body (SPK-ID) ID \n', browsefig, '\n Browse the overall Asteroid data-set.') #describes NEO use options to user
    line() #formatting 
    whichfunction = input('Choose a function:').lower() # requests a mode of use from user
    line() #formatting 
    if whichfunction == 'feed': #what happens if user chooses feed
        line() #formatting 
        line() #formatting 
        print(feedfig) #displays that the user chose feed
        line() #formatting 
        line() #formatting 
        while True: 
            rangedateone = input('type your start date (YYYY-MM-DD):\n').lower() # set first date
            rangedatetwo = input('type your end date (YYYY-MM-DD) (just press enter if you only want your start date):\n').lower() # sets second date or none
            startdate= 'start_date=' + rangedateone #formats input for use with API
            if rangedatetwo != '':
                enddate= '&end_date=' + rangedatetwo #formats input for use with API
                dateRange= startdate + enddate #formats input for use with API
                break
            elif rangedatetwo == '':
                dateRange= startdate #formats input for use with API
                break
            else:
                print('input was invalid please try again.')   
        NASAAPI= "https://api.nasa.gov/neo/rest/v1/feed?"    #defines the API used
        nasacreds = returncreds() #grabs creds
        neoresp = requests.get(NASAAPI + dateRange + '&' + nasacreds) #makes call to the nasa API with our creds and date range
        neolist = neoresp.json() #strip off json
        hazardouscount= 0
        nonhazardouscount= 0
        print('you entered start date:', rangedateone)
        if rangedatetwo != '':
            print('you entered enddate:', rangedatetwo)
        for x in neolist['near_earth_objects']:
            for y in neolist['near_earth_objects'][x]:
                if y['is_potentially_hazardous_asteroid'] == True:
                    hazardouscount += 1
                    line()
                    print('object ID --- ', y['id'])
                    print('object name --- ', y['name'])
                    sline()
                    if isinstance([y], list):
                        for z in y["close_approach_data"]:
                            print('close approach date and time:', z["close_approach_date_full"])
                            print('miss distance in kilometers:', z["miss_distance"]["kilometers"])
                            line()
                else:
                    nonhazardouscount += 1
        print(f"The number of potentially hazardous asteroids is {hazardouscount}.")
        print(f"The number of objects that are near earth objects but are not potentially hazerdous asteroids is {nonhazardouscount}")
def main():
    while True:
        askrange= ''
        difdate= ''
        rangedateone= ''
        rangedatetwo= ''
        whichfunction = ''
        apodfig= pyfiglet.figlet_format('ASTRONOMY PICTURE OF THE DAY') #uses pyfig to show apod option to user
        neofig= pyfiglet.figlet_format('NEAR EARTH OBJECTS') #uses pyfig to show apod option to user
        print(apodfig, '\n type apod') #gives instruction on what to type for apod
        line() #formatting
        print(neofig, '\n type neo') #gives instruction on what to type for apod
        sline() #formatting
        apichoice= input('which API would you like to work with?\n').lower() #asks for an input to choose which API the script uses
        line() #formatting
        line() #formatting
        line() #formatting
        if apichoice == 'apod': #run apod if chosen
            line()
            apod()
            line()
            line()
            input('press enter to continue')
        elif apichoice == 'neo': #run neo if chosen
            line()
            neo()
            line()
            line()
            input('press enter to continue')
        if difdate == 'exit' or askrange == 'exit' or rangedateone == 'exit' or rangedatetwo == 'exit' or whichfunction == 'exit' or apichoice == 'exit':
            break

if __name__ == "__main__":
    main()
