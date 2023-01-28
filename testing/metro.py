class Metro:
    def __init__(self) :
        self.stations = ['Saravali','Boisar Education','Bridge','yashwant Shrushti','Boisar','Ostwal','Bhim Nagar','Chitralaya','TAPS Gate','Militry School']
        self.map  = self.buildMap()

    
    def buildMap(self):
        map = ''
        for i in range(len(self.stations)):
            if i == len(self.stations)-1:
                print(f"[{i+1}]{self.stations[i]}")
                map += f'--[{i+1}]>'
            else:
                print(f"[{i+1}]{self.stations[i]}",end=" => ")
                map += f'--[{i+1}]>'
        return map

    

    def showMap(self):
        print("=== === === Welcome to Boisar Metro=== === ===")
        print("#Station Map: ")
        print(self.map)
        print('==============================================')
        print()

    def nextStation(self):
        return self.stations[self.currentStationNumber]

    def showCurrentStation(self,currentStationNumber):
        currentMap = self.map
        print("You are at : ",self.currentStation)
        print("Next Station : ",self.stations[self.currentStationNumber])
        print(currentMap.replace(str(currentStationNumber),"*",1))
        # print('+___'*len(self.stations))
        print("Source station   : ", self.stations[0])
        print("Destination      : ", self.stations[-1])

    def start(self):
        self.currentStationNumber = 0
        self.currentStation = self.stations[self.currentStationNumber]
        self.showCurrentStation(self.currentStationNumber)
       

    def next(self):
        self.currentStationNumber = self.currentStationNumber + 1
        self.currentStation = self.stations[self.currentStationNumber]
        if self.currentStationNumber== len(self.stations)-3:
            print("======XXX======")
            return
        else:
            self.showCurrentStation(self.currentStationNumber)

myMetro = Metro()
myMetro.showMap()
myMetro.start()
for i in range(len(myMetro.stations)):
    myMetro.next()
    print(i)
    print(len(myMetro.stations))



