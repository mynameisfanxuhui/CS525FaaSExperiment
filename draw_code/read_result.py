import csv

def getDataDict():
    #{appName: {memorySize: {coldTimeList:[], warmTimeList:[]}}}
    dataDict = {}
    applicationList = ["awsNewRes/image_recognition_aws", "awsNewRes/graph_bfs_aws",
                       "awsNewRes/thumbnailer_aws", "awsNewRes/uploader_aws", "awsNewRes/compressor_aws",
                       "azureNewRes/image_recognition_azure", "azureNewRes/graph_bfs_azure",
                       "azureNewRes/thumbnailer_azure", "azureNewRes/uploader_azure", "azureNewRes/compressor_azure"
    ]
    for appName in applicationList:
        currentDataDict = {}
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
                memory = int(memory)

                sizeDataDict = currentDataDict.get(memory, dict())
                if not sizeDataDict:
                    warm_execution_time = []
                    cold_execution_time = []
                    sizeDataDict["cold_execution_time"] = cold_execution_time
                    sizeDataDict["warm_execution_time"] = warm_execution_time
                    currentDataDict[memory] = sizeDataDict
                else:
                    cold_execution_time = sizeDataDict["cold_execution_time"]
                    warm_execution_time = sizeDataDict["warm_execution_time"]
                # turn the ms to s
                executeTime = int(executeTime) / (10 ** 6)
                if isCold == "False":
                    warm_execution_time.append(executeTime)
                else:
                    cold_execution_time.append(executeTime)


        dataDict[appName] = currentDataDict

    return dataDict

