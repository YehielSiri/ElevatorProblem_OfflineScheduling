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
        
	self._elevTimeStamp = []
        self._timeCheck = []
        for elevator in self.building._elevators:
            self._elevTimeStamp.append(0)
            self._timeCheck.append(0)
        
	self._allCalls = []
        openFile = open(inputInCsv)
        readFile = reader(openFile)
        csvCalls = list(readFile)
        for i in csvCalls:
            time = i[1]
            src = i[2]
            dest = i[3]
            status = i[4]
            allocatedTo = i[5]
            self._allCalls.append(CallForElevator(time, src, dest, status, allocatedElevator))
        
	self.output = outputInCsv        


    def schedule(self):
        for call in self._allCalls:
            for j in range(0,len(self.building._elevators)):
                self._timeCheck[j] = self._elevTimeStamp[j]
            for i in range(0,len(self.building._elevators)):
                executionTime = self.executionTime(self.building._elevators[i], call)
                self._timeCheck[i] += executionTime
            minTime = min(self._timeCheck)
            elevIndex = self._timeCheck.index(minTime)
            call._allocatedElevator = elevIndex
            self._elevTimeStamp[elevIndex] = minTime


    def executionTime(self, e:Elevator, c:CallForElevator):
        return e._doorClosingTime + e._accelerationTime + c._length/e._speed + e._stopTime + e._doorOpenningTime

    def writeTocsv(self):
        with open(self.output, "w", newline='') as filePointer:
            writer = csv.writer(filePointer)
            for j in range(0, len(self._allCalls)):
                row_to_add = self._allCalls[j].toRow()
                writer.writerow(row_to_add)
            filePointer.close()