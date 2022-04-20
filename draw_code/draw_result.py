import matplotlib.pyplot as plt
import csv
import numpy as np
from statistics import mean

dataDict = {}
applicationList = ["dynamic_html", "thumbnailer"]
for appName in applicationList:
    currentDataDict = {}
    maxTime = 0
    minTime = 1000000000
    warm_execution_time = []
    cold_execution_time = []
    # opening the CSV file
    fileName = appName + "_" + 'result.csv'
    with open(fileName, mode='r') as file:
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        rowNumber = 0
        for lines in csvFile:
            if rowNumber == 0:
                rowNumber += 1
                continue
            memory, type, isCold, executeTime, _, _, _, _ = lines
            minTime = min(minTime, int(executeTime))
            maxTime = max(maxTime, int(executeTime))
            if isCold == "False":
                warm_execution_time.append(int(executeTime))
            else:
                cold_execution_time.append((int(executeTime)))
    currentDataDict["maxTime"] = maxTime
    currentDataDict["minTime"] = minTime
    currentDataDict["cold_execution_time"] = cold_execution_time
    currentDataDict["warm_execution_time"] = warm_execution_time
    dataDict[appName] = currentDataDict


appName = "thumbnailer"
cold_execution_time = dataDict[appName]["cold_execution_time"]
warm_execution_time = dataDict[appName]["warm_execution_time"]
print("this is which application", appName)

print("cold worker number is", len(cold_execution_time))
print("warm worker number is", len(warm_execution_time))
multiMediaAverageColdTime = mean(cold_execution_time)
multiMediaAverageWarmTime = mean(warm_execution_time)
# print(averageColdTime)
# print(averageWarmTime)
# bins = np.linspace(minTime, maxTime, 50)
#
# plt.hist([warm_execution_time, cold_execution_time], bins, label=['warm_execution_time', 'cold_execution_time'])
# plt.title(appName)
# plt.legend(loc='upper right')
# plt.show()



appName = "dynamic_html"
cold_execution_time = dataDict[appName]["cold_execution_time"]
warm_execution_time = dataDict[appName]["warm_execution_time"]
webAppAverageColdTime = mean(cold_execution_time)
webAppAverageWarmTime = mean(warm_execution_time)
keys = ['Web_Warm', 'Web_Cold', 'Media_Warm', 'Media_Cold']
values = [webAppAverageWarmTime, webAppAverageColdTime, multiMediaAverageWarmTime, multiMediaAverageColdTime]

fig = plt.figure(figsize=(10, 5))

# creating the bar plot
plt.bar(keys, values, color='maroon',
        width=0.4)

plt.xlabel("type")
plt.ylabel("Execution Time")
plt.title("Different type of application's execution time")
plt.show()