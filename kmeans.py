#!/usr/bin/python
import math
import random

def distance(a,b):
	'''Calculates euclidean distance between two vectors a and b'''
	sum = 0
	for i in range(len(a)):
		sum +=((a[i]-b[i])**2)
	return math.sqrt(sum)

def mean_array(data):
	return [float(sum(l))/len(l) for l in zip(*data)]	
def calculate_cluster(mean, data):
	'''Given mean and the data array, returns an array sorting the data points into clusters'''
	cluster=[]
	for i in range(len(mean)):
		cluster.append([])
	for i in range(len(data)):
		temp=[]
		for j in range(len(mean)):
			temp.append(distance(data[i], mean[j]))
		cluster[temp.index(min(temp))].append(data[i])
	return cluster	
	
#Set the number of clusters
k=3

#set the input file to read data from and the delimiter
input_file = 'places.txt'
delimiter = ','

#Reading the data from the file into data array
csv_file = open(input_file, 'r')
data = []
for r in csv_file:
	r = r.strip()
	data.append([float(i) for i in r.split(delimiter)])
csv_file.close()

#Randomly choose k initial points
mean = random.sample(data, k)
old_mean = [0]*k

#run iterations of k-means
while(mean != old_mean):
	old_mean = mean[:]
	cluster = calculate_cluster(old_mean,data)
	for i in range(len(cluster)):
		mean[i] = mean_array(cluster[i])

#calculate final clusters
f = open('clusters.txt', 'w')
for i in range(len(data)):
	temp=[]
	for j in range(len(mean)):
		temp.append(distance(data[i],mean[j]))
	f.write(str(i)+' '+str(temp.index(min(temp)))+'\n')
f.close()
