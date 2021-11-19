class Elevator:
    def __init__(self, id, speed, minFloor, maxFloor, closeTime, openTime ,startTime ,stopTime):
        self._id = id
        self._speed = speed
        self._minFloor = minFloor
        self._maxFloor = maxFloor
        self._closeTime = closeTime
        self._openTime = openTime
        self._startTime = startTime
        self._stopTime = stopTime

    def __str__(self) -> str:
        return f"id:{self._id} ,speed:{self._speed} ,minF:{self._minFloor} ,maxF:{self._maxFloor} ,closeT:{self._closeTime} ,openT:{self._openTime} ,startT:{self._startTime} ,stopT:{self._stopTime}"

    def __repr__(self) -> str:
        return f"id:{self._id} ,speed:{self._speed} ,minF:{self._minFloor} ,maxF:{self._maxFloor} ,closeT:{self._closeTime} ,openT:{self._openTime} ,startT:{self._startTime} ,stopT:{self._stopTime}"