import math
import random


data = [
    [1, 2], [1.5, 1.8], [5, 8], [8, 8], [1, 0.6], [9, 11]
]

k = 2

# calculates euclidean distance between two points
def destance(p1,p2):
    return math.sqrt(sum((a-b)**2 for a,b in zip(p1,p2)))

# picks k random data points as initial centroids
def initialize_centroids(data,k):
    return random.sample(data,k)

# assigns each data point to the nearest centroid
def assign_clusters(data, centroids):
    clusters =[[] for _ in centroids]

    for point in data:
        distances = [destance(point,centroid) for centroid in centroids]

        closest_index = distances.index(min(distances))
        clusters[closest_index].append(point)
    
    return clusters

# updates centroids by calculating the mean(average) of all points in each cluster
def update_centroids(clusters):
    new_centroids = []
    for cluster in clusters:
        new_centroids.append(calculate_mean(cluster))
    return new_centroids

# calculates the mean(average) of all points in a cluster
def calculate_mean(cluster):
    return [sum(x)/len(x) for x in zip(*cluster)] 

# main k-means algorithm
def k_means(data, k , max_iters=100):
    centroids = initialize_centroids(data,k)
    
    for _ in range(max_iters):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)

        if new_centroids == centroids:
            break
        
        centroids = new_centroids

    return centroids, clusters

# run k-means
centroids, clusters = k_means(data, k)

print("Final centroids:", centroids)
print("Clusters:", clusters)


    