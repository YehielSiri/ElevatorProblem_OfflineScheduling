import sys
from LookUpgradedAlgo import *


# to run the algorithm
# python3 Ex1.py Ex1_Buildings/B5.json Ex1_Calls/Calls_a.csv output.csv
# to run the tester
# java -jar libs/Ex1_checker_V1.2_obf.jar 1111,2222,3333 data/Ex1_input/Ex1_Buildings/B5.json output.csv out.log


buildingInJson = sys.argv[1]
inputInCsv = sys.argv[2]
outputInCsv = sys.argv[3]

algorithm = LookUpgradedAlgo(buildingInJson,inputInCsv,outputInCsv)
algorithm.schedule()
algorithm.writeToCsv()