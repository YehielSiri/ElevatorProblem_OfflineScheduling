import csv
import math
from Building import *
from CallForElevator import *
from Elevator import *
from csv import *


class LookUpgradedAlgo:
    def __init__(self,b_json,csv_in,csv_out):
        self.csvout = csv_out
        self.b = Building(0,0)
        self.b.from_json(b_json)
        self._elevTimeStamp=[]
        self._timeCheck=[]
        for elev in self.b._elevList:
            self._elevTimeStamp.append(0)
            self._timeCheck.append(0)
        self._allCalls =[]
        openFile = open(csv_in)
        readFile = reader(openFile)
        csvCalls = list(readFile)
        for i in csvCalls:
            time = i[1]
            src = i[2]
            dest = i[3]
            status = i[4]
            allocatedTo = i[5]
            self._allCalls.append(CallForElevator(time, src, dest, status, allocatedTo))

    def schedule(self):
        for call in self._allCalls:
            for j in range(0,len(self.b._elevList)):
                self._timeCheck[j] = self._elevTimeStamp[j]
            for i in range(0,len(self.b._elevList)):
                travelTime = self.travelTime(call,self.b._elevList[i])
                self._timeCheck[i]+=travelTime
            minTime = min(self._timeCheck)
            elevIndex = self._timeCheck.index(minTime)
            call._allocatedTo = elevIndex
            self._elevTimeStamp[elevIndex] = minTime


    def travelTime(self,call:CallForElevator,elev:Elevator):
        return elev._startTime + elev._openTime + math.fabs(int(call._dest) - int(call._src))/elev._speed + elev._closeTime + elev._stopTime

    def turnCalltoRow(self,call:CallForElevator):
        return ["Elevator call",call._time,call._src,call._dest,call._status,call._allocatedTo]

    def writeTocsv(self):
        with open(self.csvout, "w", newline='') as f:
            writer = csv.writer(f)
            for j in range(0, len(self._allCalls)):
                row_to_add = self.turnCalltoRow(self._allCalls[j])
                writer.writerow(row_to_add)
            f.close()