import csv
import math
from Building import *
from CallForElevator import *
from Elevator import *
from csv import *


class LookUpgradedAlgo:
    def __init__(self, buildingInJson, inputInCsv, outputInCsv):
        self.building = Building(0,0)
        self.building.readFromJson(buildingInJson)
        
        self._calls = []
        openFile = open(inputInCsv)
        readFile = reader(openFile)
        callsToDecode = list(readFile)
        for i in callsToDecode:
            time = i[1]
            src = i[2]
            dest = i[3]
            status = i[4]
            allocatedElevator = i[5]
            self._calls.append(CallForElevator(time, src, dest, status, allocatedElevator))
        
        self._elevatorsTimeStamps = []
        self._workspace = []
        for elevator in self.building._elevators:
            self._elevatorsTimeStamps.append(0)
            self._workspace.append(0)
        
        self.output = outputInCsv        


    def schedule(self):
        for call in self._calls:
            for j in range(0,len(self.building._elevators)):
                self._workspace[j] = self._elevatorsTimeStamps[j]
            for i in range(0,len(self.building._elevators)):
                executionTime = self.executionTime(self.building._elevators[i], call)
                self._workspace[i] += executionTime
            shortestTime = min(self._workspace)
            elevatorID = self._workspace.index(shortestTime)
            call._allocatedElevator = elevatorID
            self._elevatorsTimeStamps[elevatorID] = shortestTime


    def executionTime(self, e:Elevator, c:CallForElevator):
        return e._doorClosingTime + e._accelerationTime + c._length/e._speed + e._stopTime + e._doorOpenningTime

    def writeToCsv(self):
        with open(self.output, "w", newline='') as filePointer:
            writer = csv.writer(filePointer)
            for i in range(0, len(self._calls)):
                nextCall = self._calls[i].toRow()
                writer.writerow(nextCall)
            filePointer.close()