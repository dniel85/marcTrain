from datetime import date
from datetime import timedelta
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from weather import Weather
import random, calendar, datetime, simplejson, urllib2, requests

weather = Weather()
'''Calling weahter API'''
def weatherConditions():
    location = weather.lookup_by_location('baltimore')
    condition = location.condition()
    currentCondition = condition.text()

    if currentCondition == "Scattered Showers":
        return 3
    if currentCondition == "Rain And Snow":
        return 10
    if currentCondition == "Snow":
        return 10
    if currentCondition == "Rain":
        return 6
    if currentCondition == "Ice":
        return 7
    else:
        return 0

def Leave_home():
    return random.randint(35,40)

def add_Minutes(addMin):
    addtime = (datetime.datetime.now() + datetime.timedelta(minutes=addMin)).strftime("%H:%M:%S")
    return addtime

def timeTuple():
    ToD = datetime.datetime.time(datetime.datetime.now())
    return datetime.time(ToD.hour,ToD.minute,ToD.second)





def walk_to_Platform_AM():
    get_To_station = add_Minutes(AM_Traffic()) + str(Leave_home())

    
    if day_of_week() == "Monday":
        if get_To_station <= str(datetime.time(5,0,0)):
            return 1
        if get_To_station <= str(datetime.time(6,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,0,0)):
            return 2
        if get_To_station <= str(datetime.time(7,30,0)):
            return 3
        if get_To_station <= str(datetime.time(8,0,0)):
            return 6
        if get_To_station <= str(datetime.time(8,30,0)):
            return 7
        if get_To_station <= str(datetime.time(9,0,0)):
            return 9
        else:
            return 10
        
    if day_of_week() == "Tuesday":
        if get_To_station <= str(datetime.time(5,0,0)):
            return 1
        if get_To_station <= str(datetime.time(6,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,0,0)):
            return 2
        if get_To_station <= str(datetime.time(7,30,0)):
            return 5
        if get_To_station <= str(datetime.time(8,0,0)):
            return 7
        if get_To_station <= str(datetime.time(8,30,0)):
            return 8
        if get_To_station <= str(datetime.time(9,0,0)):
            return 10
        else:
            return 12


    if day_of_week() == "Wednesday":
        if get_To_station <= str(datetime.time(5,0,0)):
            return 1
        if get_To_station <= str(datetime.time(6,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,0,0)):
            return 2
        if get_To_station <= str(datetime.time(7,30,0)):
            return 5
        if get_To_station <= str(datetime.time(8,0,0)):
            return 7
        if get_To_station <= str(datetime.time(8,30,0)):
            return 8
        if get_To_station <= str(datetime.time(9,0,0)):
            return 10
        else:
            return 12


    if day_of_week() == "Thursday":
        if get_To_station <= str(datetime.time(5,0,0)):
            return 1
        if get_To_station <= str(datetime.time(6,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,0,0)):
            return 2
        if get_To_station <= str(datetime.time(7,30,0)):
            return 5
        if get_To_station <= str(datetime.time(8,0,0)):
            return 7
        if get_To_station <= str(datetime.time(8,30,0)):
            return 8
        if get_To_station <= str(datetime.time(9,0,0)):
            return 10
        else:
            return 12


    if day_of_week() == "Friday":
        if get_To_station <= str(datetime.time(5,0,0)):
            return 1
        if get_To_station <= str(datetime.time(6,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,0,0)):
            return 1
        if get_To_station <= str(datetime.time(7,30,0)):
            return 2
        if get_To_station <= str(datetime.time(8,0,0)):
            return 3
        if get_To_station <= str(datetime.time(8,30,0)):
            return 3
        if get_To_station <= str(datetime.time(9,0,0)):
            return 4
        else:
            return 5




def AM_Traffic():
        
    url = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=Bulman+Harbour,+Pasadena,+MD+21122-6525&destination=1400+Odenton+Rd,+Odenton,+MD+211134&departure_time=now&&traffic_model=best_guess&key=AIzaSyBi96_WS6zuNp5rRz2fmFRMSz5_FKB9ckA")
    j_obj = simplejson.load(url)
    morning_traffic =  j_obj['routes'][0]['legs'][0]['duration_in_traffic'].get('text')
    morningAMtraffic = int(morning_traffic.strip(' mins'))
    return morningAMtraffic
    
    
def PM_Traffic():

    url = urllib2.urlopen("https://maps.googleapis.com/maps/api/directions/json?origin=1400+Odenton+Rd,+Odenton,+MD+211134&destination=Bulman+Harbour,+Pasadena,+MD+21122-6525&departure_time=now&&traffic_model=best_guess&key=AIzaSyBi96_WS6zuNp5rRz2fmFRMSz5_FKB9ckA")
    j_obj = simplejson.load(url)
    afternoon_traffic =  j_obj['routes'][0]['legs'][0]['duration_in_traffic'].get('text')
    afternoonPMtraffic = int(afternoon_traffic.strip(' mins'))
    return afternoonPMtraffic

def day_of_week():
    dtg = date.today()
    return calendar.day_name[dtg.weekday()]

''' Use this function for later
def commuteRange(startTime, endTime, currentTime):
    if startTime <= endTime:
        return startTime <= currentTime <= endTime 
    else:
        return startTime <= currentTime or currentTime <= endTime
'''


def timeCompare(startTime, endTime, currentTime):
    if startTime <= endTime:
        return startTime <= currentTime <= endTime 
    else:
        return startTime <= currentTime or currentTime <= endTime


def AM_or_PMcommute():
    
    if timeCompare(datetime.time(0,0,1), datetime.time(13,0,0), now):
        return AM_Traffic() + AM_trainDelays()
        
    else:
        return PM_Traffic()+ PM_trainDelays()
        

def trainTable():
    
    southBound_table = [datetime.time(4,44,00),datetime.time(5,14,00),datetime.time(5,49,00),datetime.time(6,42,00),datetime.time(6,57,00),
                                datetime.time(7,17,00),datetime.time(7,31,00),datetime.time(7,46,00),datetime.time(8,9,00),datetime.time(8,54,00),
                                datetime.time(9,26,00),datetime.time(9,53,00),datetime.time(10,52,00),datetime.time(12,02,00),datetime.time(13,02,00),
                                datetime.time(14,02,00),datetime.time(15,02,00),datetime.time(16,12,00),datetime.time(16,43,00),datetime.time(17,13,00),
                                datetime.time(17,51,00),datetime.time(18,49,00),datetime.time(20,01,00),datetime.time(21,56,00)]
    
    




    northBound_table = [datetime.time(12,20,00),datetime.time(13,20,00),datetime.time(14,20,00),datetime.time(15,23,00),datetime.time(16,10,00),datetime.time(16,22,0),
                        datetime.time(16,45,00),datetime.time(17,10,00),datetime.time(17,24,0),datetime.time(17,50,00),datetime.time(18,23,00),datetime.time(18,45,00),
                        datetime.time(19,40,00),datetime.time(21,0,0),datetime.time(22,40,00)]

def AM_trainDelays():

    url_page = 'http://www.marctracker.com/PublicView/status.jsp?line=6'
    page = urllib2.urlopen(url_page)
    soup = BeautifulSoup(page, 'html.parser')

    To_DC = soup.findAll('tr', attrs={'class':'textStatusAll'})

    makeString = ''.join(map(str, To_DC))
    EOStr = int(makeString.find("Odenton"))

    OdentenStation = makeString[EOStr:]
    
    status = int(makeString.find("Delayed"))
    veryLate = int(makeString.find("VeryLate"))


    delay = int(makeString.find("Min"))
    delay_loc_start = delay - 2
    delay_loc_end = delay_loc_start +2
    delayTime = makeString[delay_loc_start:delay_loc_end]

    if status != -1 and EOStr != -1:
        return int(delayTime)
    else:
        return 0

def PM_trainDelays():

    url_page = 'http://www.marctracker.com/PublicView/status.jsp?line=5'
    page = urllib2.urlopen(url_page)
    soup = BeautifulSoup(page, 'html.parser')

    To_DC = soup.findAll('tr', attrs={'class':'textStatusAll'})

    makeString = ''.join(map(str, To_DC))
    EOStr = int(makeString.find("Odenton"))

    OdentenStation = makeString[EOStr:]
    status = int(makeString.find("Delayed"))

    next_train_leaving = int(makeString.find("PM"))
    hourHand = int(next_train_leaving - 5)
    hourValue = int(makeString[hourHand]) + 12
   
    minuteHandOne = int(next_train_leaving -3)
    minuteHandtwo = int(next_train_leaving -2)

    minValueOne = int(makeString[minuteHandOne])
    minValuetwo = int(makeString[minuteHandtwo])
    minutesValue =int(str(minValueOne) + str(minValuetwo))

    nextTrainTime = datetime.time(hourValue,minutesValue,0)
    

    delay = int(makeString.find("Min"))
    delay_loc_start = delay - 2
    delay_loc_end = delay_loc_start +2
    delayTime = makeString[delay_loc_start:delay_loc_end]

    if status != -1 and EOStr != -1:
        return int(delayTime)
    else:
        if EOStr != -1:
            return nextTrainTime
        else:
            return 0
def big_compute():
    Leave_home() + AM_Traffic()
    
    
def main():
    now = timeTuple()
    big_compute() 
    Leave_home()
    AM_trainDelays()
    print"DEBUG!! Leave_home = " + str(Leave_home())
    print"DEBUG!! weatherConditions= " + str(weatherConditions())
    print "DEBUG!! The current time is " + str(now)
    
if __name__ == "__main__":
    main()
