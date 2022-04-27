from cmath import nan
import matplotlib.pyplot as plt
from statistics import mean
from read_result import getDataDict

data_dict = getDataDict()

def draw_aws_image_recognition():
    y = []
    y.append(mean(data_dict['awsNewRes/image_recognition_aws'][512]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/image_recognition_aws'][1024]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/image_recognition_aws'][2048]['cold_execution_time']))

    plt.yscale('log')
    plt.xlim([0, 6])
    plt.xticks([1,2,3,4,5], ['128', '256', '512', '1024', '2048'])
    plt.plot([3,4,5], y, marker='o')
    plt.title('AWS Image Recognition')
    plt.xlabel('Allocated Memory (MB)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

def draw_aws_thumbnailer():
    y = []
    y.append(mean(data_dict['awsNewRes/thumbnailer_aws'][128]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/thumbnailer_aws'][256]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/thumbnailer_aws'][512]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/thumbnailer_aws'][1024]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/thumbnailer_aws'][2048]['cold_execution_time']))

    plt.yscale('log')
    plt.xlim([0, 6])
    plt.xticks([1,2,3,4,5], ['128', '256', '512', '1024', '2048'])
    plt.plot([1,2,3,4,5], y, marker='o')
    plt.title('AWS Thumbnailer')
    plt.xlabel('Allocated Memory (MB)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

def draw_aws_uploader():
    y = []
    y.append(mean(data_dict['awsNewRes/uploader_aws'][128]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/uploader_aws'][256]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/uploader_aws'][512]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/uploader_aws'][1024]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/uploader_aws'][2048]['cold_execution_time']))

    plt.yscale('log')
    plt.xlim([0, 6])
    plt.xticks([1,2,3,4,5], ['128', '256', '512', '1024', '2048'])
    plt.plot([1,2,3,4,5], y, marker='o')
    plt.title('AWS Uploader')
    plt.xlabel('Allocated Memory (MB)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

def draw_aws_compressor():
    y = []
    y.append(mean(data_dict['awsNewRes/compressor_aws'][256]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/compressor_aws'][512]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/compressor_aws'][1024]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/compressor_aws'][2048]['cold_execution_time']))

    plt.yscale('log')
    plt.xlim([0, 5])
    plt.xticks([1,2,3,4], ['256', '512', '1024', '2048'])
    plt.plot([1,2,3,4], y, marker='o')
    plt.title('AWS Compressor')
    plt.xlabel('Allocated Memory (MB)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()

def draw_aws_graph_bfs():
    y = []
    y.append(mean(data_dict['awsNewRes/graph_bfs_aws'][128]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/graph_bfs_aws'][256]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/graph_bfs_aws'][512]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/graph_bfs_aws'][1024]['cold_execution_time']))
    y.append(mean(data_dict['awsNewRes/graph_bfs_aws'][2048]['cold_execution_time']))

    plt.yscale('log')
    plt.xlim([0, 6])
    plt.xticks([1,2,3,4,5], ['128', '256', '512', '1024', '2048'])
    plt.plot([1,2,3,4,5], y, marker='o')
    plt.title('AWS Graph BFS')
    plt.xlabel('Allocated Memory (MB)')
    plt.ylabel('Execution Time (seconds)')
    plt.show()