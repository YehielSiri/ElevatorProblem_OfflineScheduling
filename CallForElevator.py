class CallForElevator:
    def __init__(self, time, src, dest, status, allocatedElevator):
        self._time = time
        self._src = src
        self._dest = dest
        self._status = status
        self._allocatedTo = allocatedTo
	self._length = abs(int(src) - int(dest))



    def toString(self):
        return f"Call received at {self.time} to service from {self.source}'th floor to {self.destination}'th floor. {self.allocatedElevator}'th elevator has allocated."

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


    def __str__(self):
        return f"Call was made at {self._time}, from {self._src} to {self._dest} and it was allocated to {self._allocatedTo}"

    def __repr__(self):
        return f"Call was made at {self._time}, from {self._src} to {self._dest} and it was allocated to {self._allocatedTo}"

if __name__== '__main__':
    c1 = CallForElevator(0,1,2,-1,-1)
    print(c1)
    c1.from_csv("Calls_a.csv")
    print(c1._allCalls)