import csv

def direction(origin, destination):
    stops =["Washington","New Caoton","Seabook","Bowie State","Odenton","BWI","Haethope",
           "West Batimoe","Penn Station","Matin Airport","Egewood","Abdereen","Perryville"]

    for x in stops:

        if x == origin:

            origin = len(x)

            for y in stops:

                if y ==destination:

                    destination= len(y)

                    print origin - destination








def southBoundTrain(station):




    filename = 'Southbound.csv'
    # initializing the titles and rows list
    fields = []
    rows = []
    # reading csv file
    with open(filename, 'r') as csvfile:
        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=";")
        # extracting field names through first row
        fields = csvreader.next()
        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        for row in rows[:]:
            # parsing each column of a row
            for col in row:

                if station=="Perryville":
                    Perryville = rows[1][1:]
                    return Perryville

                if station=="Abdereen":
                    Abdereen = rows[2][1:]
                    return Abdereen

                if station=="Edgewood":
                    Edgewood = rows[3][1:]
                    return Edgewood

                if station=="Martin Airport":
                    MartinAirport = rows[4][1:]
                    return MartinAirport

                if station=="Baltimore Penn Station":
                    BaltimorePennStation = rows[5][1:]
                    return BaltimorePennStation

                if station=="West Baltimore":
                    WestBaltimore = rows[6][1:]
                    return WestBaltimore

                if station=="Haethrope":
                    Haethorpe = rows[7][1:]
                    return Haethorpe

                if station=="BWI Airport" or "Airport":
                    BWIairport = rows[8][1:]
                    return BWIairport

                if station=="Odenton":
                    Odenton = rows[9][1:]
                    return Odenton

                if station=="Bowie State":
                    BowieSt = rows[10][1:]
                    return BowieSt

                if station=="Seabrook":
                    Seabrook = rows[11][1:]
                    return Seabrook

                if station== "New Carrollton":
                    NewCarlton = rows[1][1:]
                    return NewCarlton

                if station=="PennStation" or "WashingtonDC":
                    PennStation = rows[13][1:]
                    return PennStation

            trainNo = int(len(station) + 1)


def northBoundTrain(station):
    filename = 'Northbound.csv'
    # initializing the titles and rows list
    fields = []
    rows = []
    # reading csv file

    with open(filename, 'r') as csvfile:

        # creating a csv reader object
        csvreader = csv.reader(csvfile, delimiter=";")

        # extracting field names through first row
        fields = csvreader.next()

        # extracting each data row one by one
        for row in csvreader:
            rows.append(row)

        for row in rows[:]:
            # parsing each column of a row
            for col in row:

                if station=="Washington DC" or "Washington Penn Station":
                    WashingtionPennStation = rows[1][1:]
                if station=="New Carrollton":
                    NewCaoton=rows[2][1:]
                if station=="Seabrook":
                    Seabook=rows[3][1:]
                if station=="Bowie State":
                    BowieState=rows[4][1:]
                if station=="Odenton":
                    Odenton=rows[]
                BWIAipot
                Haethope
                WestBatimoe
                BatimoePennStation
                MatinAipot
                Egewood
                Abeeen
                Perryville


    def TrainPicker():

        trainNo = [item[0] for item in DepartOdenton_ArrivePenn]
        depart = [item[1] for item in DepartOdenton_ArrivePenn]
        arrive = [item[2] for item in DepartOdenton_ArrivePenn]

        for x in departOdenton:
                 if x > timeToPlatform():
                     for sublist in DepartOdenton_ArrivePenn:
                         if sublist[1] == x:
                             return sublist




