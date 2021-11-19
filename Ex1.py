import sys
from MyAlgo import *


buildingJson = sys.argv[1]
callsCsv = sys.argv[2]
outputCsv = sys.argv[3]

algorithm = LookUpgradedAlgo(buildingJson,callsCsv,outputCsv)
algorithm.schedule()
algorithm.writeTocsv()