import csv
import matplotlib.pyplot as plt

with open("compression_aws_result.csv") as csvfile:
    result_256 = [[],[],[], []]
    types = ["cold", "warm", "burst", "sequential"]
    for row in csv.reader(csvfile):
        if(row[0] == "256"):
            for i in range(len(types)):
                if(row[1] == types[i]):
                    result_256[i].append(float(row[3]))
    plt.boxplot(result_256)
    plt.xticks([1, 2, 3, 4], labels=types)
    plt.xlabel("AWS with 256MB memory size compression")
    plt.ylabel("execution time(seconds)")
    plt.show()