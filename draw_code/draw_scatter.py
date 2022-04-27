import matplotlib.pyplot as plt
import csv
import numpy as np
from statistics import mean
import read_result

dataDict = read_result.getDataDict()
nameList = ["awsNewRes/image_recognition_aws", "awsNewRes/graph_bfs_aws",
            "awsNewRes/thumbnailer_aws", "awsNewRes/uploader_aws", "awsNewRes/compressor_aws",
            "azureNewRes/image_recognition_azure", "azureNewRes/graph_bfs_azure",
            "azureNewRes/thumbnailer_azure", "azureNewRes/uploader_azure", "azureNewRes/compressor_azure"]

appName = "azureNewRes/thumbnailer_azure"
print(dataDict[appName])
cold_execution_time_x = []
cold_execution_time_y = []
warm_execution_time_x = []
warm_execution_time_y = []


# for azure with no memory
for appName, subData in dataDict.items():
    if "azure" in appName:
        continue
    appName = appName[10:]
    appName = appName.replace("_aws", "")
    for memorySize, currentDataDict in subData.items():
        if memorySize != 2048:
            continue
        for executionTime in currentDataDict["cold_execution_time"]:
            cold_execution_time_x.append(appName)
            cold_execution_time_y.append(executionTime)
        for executionTime in currentDataDict["warm_execution_time"]:
            warm_execution_time_x.append(appName)
            warm_execution_time_y.append(executionTime)



# for memorySize, currentDataDict in dataDict[appName].items():
#     for executionTime in currentDataDict["cold_execution_time"]:
#         cold_execution_time_x.append(memorySize)
#         cold_execution_time_y.append(executionTime)
#
#     for executionTime in currentDataDict["warm_execution_time"]:
#         warm_execution_time_x.append(memorySize)
#         warm_execution_time_y.append(executionTime)



plt.scatter(cold_execution_time_x, cold_execution_time_y, c='b', marker='s', label='cold')

plt.scatter(warm_execution_time_x, warm_execution_time_y, c='g', marker='o', label='warm')
plt.xlabel("AWS Functions")
plt.ylabel("executed time(seconds)")
plt.title("AWS cold start time vs warm start time with biggest memory size")
plt.legend(loc='upper right')
# show plot
plt.show()
