#!/usr/bin/python3
import requests
import pyfiglet
import pprint
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

def mrp():
    indate= input('Enter a date to see photos from the Curiosity Mars Rover on that date (yyyy-mm-dd)\n').lower() #requests start date from user
    date= '?earth_date=' + indate #sets input to startdate preceded by NASAAPI start date parameter
    NASAAPI= 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'    #defines the API used
    nasacreds = returncreds() #grabs creds
    mrpresp = requests.get(NASAAPI + date + '&' + nasacreds) #makes call to the nasa API with our creds and date range
    mrplist = mrpresp.json() #strip off json
    
    for x in mrplist['photos']: #for loop to find useful info within the api 
        line()
        print ('sol date:', x['sol']) 
        print ('id number:', x['id'])
        print ('camera:', x['camera']['full_name'])
        sline()
        print ('image:', x['img_src'])
        line()

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
        print(apodlist["title"] + "\n" + apodlist["date"] + "\n" + apodlist["explanation"] + "\n" + apodlist["url"])

#defines near earth objects API
def neo():
    #defines variables used for formating utlizing pyfiglet
    feedfig= pyfiglet.figlet_format('FEED')
    lookupfig= pyfiglet.figlet_format('LOOKUP')
    browsefig= pyfiglet.figlet_format('BROWSE')
    print(feedfig, '\n Retrieve a list of Asteroids based on their closest approach date to Earth.\n', lookupfig, '\n Lookup a specific Asteroid based on its NASA JPL small body (SPK-ID) ID \n') #describes NEO use options to user
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
        hazardouscount= 0  #starts hazard count
        nonhazardouscount= 0 #starts nonhazard count
        print('you entered start date:', rangedateone) #confirm date
        if rangedatetwo != '':  #if rangedatetwo is not blank
            print('you entered enddate:', rangedatetwo) # confirm the date entered
        for x in neolist['near_earth_objects']: #for loop picks through dictionary
            for y in neolist['near_earth_objects'][x]:#imbedded for loop to find if hazardous
                if y['is_potentially_hazardous_asteroid'] == True:  #confirms hazardous pontential is true
                    hazardouscount += 1  # counts the amount of hazardous
                    line()
                    print('object ID --- ', y['id']) 
                    print('object name --- ', y['name']) #prints info about the hazardous neos
                    sline()
                    if isinstance([y], list): #isinstance tells python its ok that this is a  list in a dictionary and not to panic 
                        for z in y["close_approach_data"]: 
                            print('close approach date and time:', z["close_approach_date_full"])
                            print('miss distance in kilometers:', z["miss_distance"]["kilometers"])  #prints info about the close approach data
                            line()
                else:
                    nonhazardouscount += 1  # counts nonhazardous 
        print(f"The number of potentially hazardous asteroids is {hazardouscount}.")  #gives hazardous count
        print(f"The number of objects that are near earth objects but are not potentially hazerdous asteroids is {nonhazardouscount}") #gives nonhazardous count
    if whichfunction == 'lookup':
        line()
        line()
        print(lookupfig)
        line()
        line()
        while True:
            asteroidinput = input ('type the asteroid id you would like to look up.') 
            break
        NASAAPI= "https://api.nasa.gov/neo/rest/v1/neo/"
        nasacreds = returncreds() #grabs creds
        neoresp = requests.get(NASAAPI + asteroidinput + '?' + nasacreds) #makes call to the nasa API with our creds and date range
        neolist = neoresp.json() #strip off json
        print(neolist)
        line()
        line()
        print('Link to use the raw json---', neolist['links'])
def main():
    while True:
        #initial definitions for exit to work at any point
        askrange= ''
        difdate= ''
        rangedateone= ''
        rangedatetwo= ''
        whichfunction = ''
        indate = ''
        apodfig= pyfiglet.figlet_format('ASTRONOMY PICTURE OF THE DAY') #uses pyfig to show apod option to user
        neofig= pyfiglet.figlet_format('NEAR EARTH OBJECTS') #uses pyfig to show apod option to user
        mrpfig= pyfiglet.figlet_format('MARS ROVER PHOTOS') #uses pyfig to show mrp option to user
        print(apodfig, '\n type apod') #gives instruction on what to type for apod
        line() #formatting
        print(neofig, '\n type neo') #gives instruction on what to type for apod
        line() #formatting
        print(mrpfig, '\n type mrp') #gives instruction on what to type for mrp 
        apichoice= input('which API would you like to work with?\n').lower() #asks for an input to choose which API the script uses
        line() #formatting
        line() #formatting
        line() #formatting
        if apichoice == 'apod': #run apod if chosen
            line()
            apod() #calls apod
            line()
            line()
            input('press enter to continue')
        elif apichoice == 'neo': #run neo if chosen
            line()
            neo() #calls neo
            line()
            line()
            input('press enter to continue')
        elif apichoice == 'mrp': #run mrp if chosen
            line()
            mrp()
            line()
            line()
            input('press enter to continue')
        

        #exit the program at any point
        if difdate == 'exit' or askrange == 'exit' or rangedateone == 'exit' or rangedatetwo == 'exit' or whichfunction == 'exit' or apichoice == 'exit' or indate== 'exit': 
            break

if __name__ == "__main__":
    main()

