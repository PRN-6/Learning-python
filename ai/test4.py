
#k-means from scratch 

import random
import math

#distance function (euclidean distance)
def distance(p1,p2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))

#initialize centroids
#starting points are random
def initialize_centroids(data,k):
    #.simple returns ramdom unique elements
    return random.sample(data,k)

#assign data points to clusters
def assign_clusters(data, centroids):
    clusters = [[] for _ in centroids]

    for point in data:
        distances = [distance(point,centroid) for centroid in centroids]
        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)
    
    return clusters


data = [
    [2, 3], [3, 4], [2, 4],
    [10, 11], [11, 12], [10, 12]
]
