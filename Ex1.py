import sys
from LookUpgradedAlgo import *


buildingInJson = sys.argv[1]
inputInCsv = sys.argv[2]
outputInCsv = sys.argv[3]

algorithm = LookUpgradedAlgo(buildingInJson,inputInCsv,outputInCsv)
algorithm.schedule()
algorithm.writeToCsv()