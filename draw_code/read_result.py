import csv

def getDataDict():
    #{appName: {memorySize: {coldTimeList:[], warmTimeList:[]}}}
    dataDict = {}
    applicationList = ["dynamic_html", "thumbnailer_aws", "uploader_aws", "compression_aws"]
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

