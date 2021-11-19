import json
from Elevator import *

class Building:
    def __init__(self, minFloor, maxFloor):
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._elevators = []

    def readFromJson(self, fileName):
        with open(fileName, "r") as filePointer:
            buffer = json.load(filePointer)
            self._minFloor = buffer["_minFloor"]
            self._maxFloor = buffer["_maxFloor"]
            for i in buffer["_elevators"]:
                
		id = int(i["_id"])
                speed = float(i["_speed"])
                minFloor = int(i["_minFloor"])
                maxFloor = int(i["_maxFloor"])
                closeTime = float(i["_closeTime"])
                openTime = float(i["_openTime"])
                startTime = float(i["_startTime"])
                stopTime = float(i["_stopTime"])
                
		self._elevators.append(Elevator(id, speed, minFloor, maxFloor, closeTime, openTime, startTime, stopTime))

    def toString(self):
        return f"Building's min floor: {self.minFloor} Max floor: {self.maxFloor} Elevators number: {len(self.elevators)}"