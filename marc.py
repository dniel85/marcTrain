from datetime import date, datetime,timedelta
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
from weather import Weather
import random, calendar, datetime, simplejson, urllib2, requests

DepartOdenton_ArrivePenn = [[401,datetime.time(4,44),datetime.time(5,19)],[403,datetime.time(5,14),datetime.time(5,49)],[505,datetime.time(5,49),datetime.time(6,21)],
                            [407,datetime.time(6,17),datetime.time(6,50)],[409,datetime.time(6,39),datetime.time(7,7)],[511,datetime.time(6,57),datetime.time(7,30)],
                            [413,datetime.time(7,12),datetime.time(7,44)],[415,datetime.time(7,26),datetime.time(7,59)],[517,datetime.time(7,41),datetime.time(8,6)],
                            [419,datetime.time(8,4),datetime.time(8,36)],[421,datetime.time(8,34),datetime.time(9,7)],[523,datetime.time(9,25),datetime.time(10,00)],
                            [425,datetime.time(9,49),datetime.time(10,26)],[427,datetime.time(10,47),datetime.time(11,24)],[429,datetime.time(11,57),datetime.time(12,35)],
                            [431,datetime.time(12,57),datetime.time(13,35)],[433,datetime.time(13,57),datetime.time(14,33)],[435,datetime.time(14,57),datetime.time(15,35)],
                            [439,datetime.time(16,07),datetime.time(16,45)],[641,datetime.time(16,39),datetime.time(17,8)],[443,datetime.time(17,8),datetime.time(17,47)],
                            [445,datetime.time(17,48),datetime.time(18,20)],[449,datetime.time(18,45),datetime.time(19,15)],[451,datetime.time(19,56),datetime.time(20,27)],
                            [453,datetime.time(21,56),datetime.time(22,30)]]

DepartPenn_ArriveOdenton = [[400,datetime.time(5,50),datetime.time(06,19)],[502,datetime.time(6,10),datetime.time(6,37)],[404,datetime.time(6,35),datetime.time(7,00)],
                            [406,datetime.time(7,10),datetime.time( 7,38)],[610,datetime.time(7,50),datetime.time(8,22)],[612,datetime.time(8,20),datetime.time(8,47)],
                            [412,datetime.time(9,05),datetime.time(9,33)],[414,datetime.time(9,30),datetime.time(9,57)],[416,datetime.time(10,30),datetime.time(10,57)],
                            [418,datetime.time(11,20),datetime.time(11,47)],[520,datetime.time(12,20),datetime.time(12,47)],[422,datetime.time(13,20),datetime.time(13,47)],
                            [424,datetime.time(14,20),datetime.time(14,47)],[426,datetime.time(15,23),datetime.time(15,51)],[428,datetime.time(16,10),datetime.time(16,39)],
                            [532,datetime.time(16,22),datetime.time(16,53)],[634,datetime.time(16,45),datetime.time(17,15)],[536,datetime.time(17,10),datetime.time(17,35)],
                            [440,datetime.time(17,24),datetime.time(17,56)],[642,datetime.time(17,50),datetime.time(18,19)],[544,datetime.time(18,23),datetime.time(18,51)],
                            [446,datetime.time(18,45),datetime.time(19,14)],[448,datetime.time(19,40),datetime.time(20,8)],[548,datetime.time(21,00),datetime.time(21,28)],
                            [452,datetime.time(22,40),datetime.time(23,07)]]

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

def timeTuple():
    ToD = datetime.datetime.time(datetime.datetime.now())
    return datetime.time(ToD.hour,ToD.minute,ToD.second)

def timeCompare(startTime, endTime, currentTime):
    if startTime <= endTime:
        return startTime <= currentTime <= endTime 
    else:
        return startTime <= currentTime or currentTime <= endTime
    
def AM_or_PM():
    morning = "AM"
    afternoon = "PM"
    if timeCompare(datetime.time(0,0,1), datetime.time(13,0,0), timeTuple()):
        return morning
    else:
        return afternoon

def add_Minutes(addMin):
    addtime = (datetime.datetime.now() + datetime.timedelta(minutes=addMin)).strftime("%H,%M,%S")
    return int(addtime)

def walk_Lot_to_Platform():
    walk = random.randrange(4,6)
    if AM_or_PM() == "PM":
        walk = walk + 5    
    dtg = date.today()
    DOW = calendar.day_name[dtg.weekday()]

    if DOW != "Monday" or "Friday":
        return int(walk +2)
    else:
        return int(walk)

def Traffic():
    AM_Drive_Url = "https://maps.googleapis.com/maps/api/directions/json?origin=Bulman+Harbour,+Pasadena,+MD+21122-6525&destination=1400+Odenton+Rd,+Odenton,+MD+211134&departure_time=now&&traffic_model=best_guess&key=AIzaSyBi96_WS6zuNp5rRz2fmFRMSz5_FKB9ckA"
    PM_Drive_Url = "https://maps.googleapis.com/maps/api/directions/json?origin=1400+Odenton+Rd,+Odenton,+MD+211134&destination=Bulman+Harbour,+Pasadena,+MD+21122-6525&departure_time=now&&traffic_model=best_guess&key=AIzaSyBi96_WS6zuNp5rRz2fmFRMSz5_FKB9ckA"

    if AM_or_PM() == "AM":
        commute = AM_Drive_Url
        url = urllib2.urlopen(commute)
        j_obj = simplejson.load(url)
        commute_traffic =  j_obj['routes'][0]['legs'][0]['duration_in_traffic'].get('text')
        traffic = int(commute_traffic.strip(' mins'))
        return traffic

    else:
        commute = PM_Drive_Url
        url = urllib2.urlopen(commute)
        j_obj = simplejson.load(url)
        commute_traffic =  j_obj['routes'][0]['legs'][0]['duration_in_traffic'].get('text')
        traffic = int(commute_traffic.strip(' mins'))
        return traffic

def timeToPlatform():
    if AM_or_PM() == "AM":
        TimeToOdenton = int(weatherConditions()+ Traffic()+ walk_Lot_to_Platform())
        DTG = datetime.datetime.now()
        dtg = DTG + datetime.timedelta(minutes = TimeToOdenton)
        dt = datetime.time(dtg.hour, dtg.minute, dtg.second)
        return dt
    else:
        
        DTG = datetime.datetime.now()
        dtg = DTG + datetime.timedelta(minutes = random.randrange(18,22))
        dt = datetime.time(dtg.hour, dtg.minute, dtg.second)
        return dt
    
def computeHome():
    if AM_or_PM() == "PM":
        DTG = Evening_Depart()[2]
        today = date.today()
        test = datetime.datetime.combine(today, DTG)
        td = test + datetime.timedelta(minutes= walk_Lot_to_Platform())
        timeToCar = long(td.strftime("%Y%m%d%H%M"))
        return timeToCar, td
    else:
        DTG = Morning_Depart()[2]
        today = date.today()
        test = datetime.datetime.combine(today, DTG)
        td = test + datetime.timedelta(minutes= walk_Lot_to_Platform())
        timeToCar = long(td.strftime("%Y%m%d%H%M"))
        return timeToCar, td
        


def TrafficHome():
        
        x = long(computeHome()[0])
        PM_Drive_Url = "https://maps.googleapis.com/maps/api/directions/json?origin=1400+Odenton+Rd,+Odenton,+MD+211134&destination=Bulman+Harbour,+Pasadena,+MD+21122-6525&departure_time="+str(x)+"&&traffic_model=best_guess&key=AIzaSyBi96_WS6zuNp5rRz2fmFRMSz5_FKB9ckA"
        commute = PM_Drive_Url
        url = urllib2.urlopen(commute)
        j_obj = simplejson.load(url)
        commute_traffic =  j_obj['routes'][0]['legs'][0]['duration_in_traffic'].get('text')
        traffic = int(commute_traffic.strip(' mins'))
        return traffic

def arriveHome():
    if AM_or_PM() == "PM":
        getHome = computeHome()[1] + datetime.timedelta(minutes=TrafficHome())
        home = getHome.strftime("%H:%M PM")
        return home
    else:
        getHome = computeHome()[1] + datetime.timedelta(minutes=Traffic())
        home = getHome.strftime("%H:%M PM")
        return home
        
    
def Morning_Depart():

    trainNo = [item[0] for item in DepartOdenton_ArrivePenn]
    departOdenton = [item[1] for item in DepartOdenton_ArrivePenn]
    arrivePenn = [item[2] for item in DepartOdenton_ArrivePenn]

    for x in departOdenton:
             if x > timeToPlatform():
                 for sublist in DepartOdenton_ArrivePenn:
                     if sublist[1] == x:
                         return sublist
def Evening_Depart():          
                            
    trainNo = [item[0] for item in DepartPenn_ArriveOdenton]
    departPenn = [item[1] for item in DepartPenn_ArriveOdenton]
    arriveOdenton = [item[2] for item in DepartPenn_ArriveOdenton]
    noTrains = "No trains"

    for x in departPenn:
             if x > timeToPlatform():
                 for sublist in DepartPenn_ArriveOdenton:
                     if sublist[1] == x:
                         return sublist
            
def main():
      
    if AM_or_PM()=="AM":
        
        if timeCompare(datetime.time(0,0,0),datetime.time(3,30),timeTuple())==True:
            print "Good Morning, The first avaliable Train departing Odenton Station is the "+str(DepartOdenton_ArrivePenn[0][0])+" Leaving at "+str(DepartOdenton_ArrivePenn[0][1])

        else:
            print "Good Morning, If you leave home now your morning commute to Odenton Station is "+str(Traffic())+" minutes,\n The next Train leaving Odenton is the "+ str(Morning_Depart()[0])+", departing at "+str(Morning_Depart()[1])+" and arrive at Penn Station at "+str(Morning_Depart()[2])+ "\n you will arive at the office " + str(arriveHome())

    if AM_or_PM()=="PM":
        
        if timeCompare(datetime.time(22,30),datetime.time(3,30),timeTuple())==True:
            print "Sorry, There are no more NorthBound trains the next train Leaving Penn station is the "+str(DepartPenn_ArriveOdenton[0][0])+" Leaving at "+str(DepartPenn_ArriveOdenton[0][1])
        
        else:
            print "Good Evening, If you leave your office now The next Train leaving Penn Station to Odenton is the "+ str(Evening_Depart()[0])+" You will depart Penn station at "+str(Evening_Depart()[1])+" and arrive in Odenton at "+str(Evening_Depart()[2])+ "\n your Evening commute is around "+str(TrafficHome())+" minutes and you will arive home around " + str(arriveHome())
        
        
if __name__ == "__main__":
    main()






    
    
