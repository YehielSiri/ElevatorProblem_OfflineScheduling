import json
from Elevator import *

class Building:
    def __init__(self, minFloor, maxFloor):
        self.minFloor = minFloor
        self.maxFloor = maxFloor
        self.elevators = []

    def readFromJson(self, fileName):
        with open(fileName, "r") as fp:
            buffer = json.load(fp)
            self.minFloor = buffer["minFloor"]
            self.maxFloor = buffer["maxFloor"]
            for i in buffer["elevators"]:
                id = int(i["_id"])
                speed = float(i["_speed"])
                minFloor = int(i["minFloor"])
                maxFloor = int(i["maxFloor"])
                closeTime = float(i["_closeTime"])
                openTime = float(i["_openTime"])
                startTime = float(i["_startTime"])
                stopTime = float(i["_stopTime"])
                self.elevators.append(Elevator(id,speed,minFloor,maxFloor,closeTime,openTime,startTime,stopTime))

    def __str__(self):
        return f"This building's min floor is {self.minFloor}, max floor is {self.maxFloor} and has {len(self.elevators)} elevators"

    def __repr__(self):
        return f"This building's min floor is {self.minFloor}, max floor is {self.maxFloor} and has {len(self.elevators)} elevators"