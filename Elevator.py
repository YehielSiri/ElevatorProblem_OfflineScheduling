class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, doorClosingTime, doorOpenningTime ,accelerationTime ,stopTime):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._doorClosingTime = doorClosingTime
        self._doorOpenningTime = doorOpenningTime
        self._accelerationTime = accelerationTime
        self._stopTime = stopTime

    def toString(self) -> str:
        return f"Elevator ID: {self._id} Speed: {self._speed} Min floor: {self._minFloor} Max floor: {self._maxFloor} Door closing time: {self._doorClosingTime} Door openning time: {self._doorOpenningTime} Acceleration time: {self._accelerationTime} Stop time: {self._stopTime}"
