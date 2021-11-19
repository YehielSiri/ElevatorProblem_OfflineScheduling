class CallForElevator:
    def __init__(self, time, src, dest, status, allocatedElevator):
        self._time = time
        self._src = src
        self._dest = dest
        self._status = status
        self._allocatedElevator = allocatedElevator
	self._length = abs(int(src) - int(dest))


    def calcTime(self, elevator):
        calc = elevator.openTime * 15 + elevator.closeTime * 15 + elevator.startTime * 10 + elevator.stopTime * 10 + elevator.speed * self.absFloor + abs(
            int(elevator.position) - int(self.source))
        calc = calc * (len(elevator.callsQueue) +5)
        return calc

    def calcTimeMedium(self, elevator):
        calc = elevator.openTime*2  + elevator.closeTime*2 + elevator.startTime*10  + elevator.stopTime*10  + elevator.speed * self.absFloor + abs(
            int(elevator.position) - int(self.source))
        calc = calc * (len(elevator.callsQueue)+15)
        return calc


    def toString(self):
        #the first option: return f"Call received at {self._time} to service from {self._src}'th floor to {self._dest}'th floor. {self._allocatedElevator}'th elevator has allocated."
	return f"Call receiving time: {self._time} Source: {self._src} Destination: {self._dest} Allocated to elevator: {self._allocatedElevator}"


    def toRow(self):
        return ["Elevator call", self._time, self._src, self._dest, self._status, self._allocatedElevator]


if __name__== '__main__':
    c1 = CallForElevator(0,0,1,-1,-1)
    print(c1)
    c1.from_csv("Calls_a.csv")
    print(c1._allCalls)