import csv

csvfile = open("MagicMethods/astronauts.csv", "r")
astroCSV = csv.DictReader(csvfile)

astro = list(filter(lambda x: x["Name"] !="", astroCSV))

j = astro[0]
k = astro[1]

class Astronaut:
    
    def __init__(self,name,flightHR, status):
        self.name = name
        self.flightHR = flightHR
        self.status = status

    def __repr__(self):
        return "%s, %s" % (self.name, self.status)

    def __gt__(self,other):

        return self.flightHR > other.flightHR

    def __eq__(self, other):
        return self.flightHR == other.flightHR

    def __ge__ (self, other):
        return self.flightHR >= other.flightHR
            
   

    
ast1 = Astronaut(j["Name"],j["Space Flight (hr)"],j["Status"])
ast2 = Astronaut(k["Name"],k["Space Flight (hr)"],k["Status"])

print(ast1 > ast2)
print(ast1 >= ast2)
print(ast1 == ast2)
