# Name: Eugene Zhuravel, Ian Wodder, Israel Nolazco
# Date: 7/24/2019
# Course Name:CPSC-51100-003
# Semester: Summer 2018
# Assignment: Programming Assignment 2

import sys
import os


# Opens file in local directory, read each line and cast to a float
def open_file(filename):
    location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    location = location + os.sep + filename
    lines = [float(x.rstrip()) for x in open(location)]
    return lines


# initialize empty clusters, raise error if there are more clusters than points
def initialize_clusters(num_clusters, points):
    if num_clusters > len(points):
        raise IndexError("More clusters than points")
    else:
        return range(num_clusters)


# using the old clusters, create new centroids which are the average of each cluster
# iterate over all points, moving each point to the centroid with the smallest absolute value
def initialize_new_centroids(prev_clusters={}, points=[]):
    centroids = {}
    for value in prev_clusters.values():
        new_centroid_point = sum(value)/len(value)
        centroids[round(new_centroid_point, 2)] = []

    for item in points:
        prev_abs = max(points)
        for key in centroids.keys():
            if abs(item - key) < prev_abs:
                prev_abs = abs(item - key)
                value_to_insert = item
                key_spot = key

        centroids.get(key_spot).append(value_to_insert)

    return centroids


# initialize the first centroids from the first values in the input file equal to the number of clusters
# entered by the user
def initialize_first_centroids(num_clusters, points=[]):
    centroids = {x: [] for x in points[:num_clusters]}

    for item in points:
        prev_abs = max(points)
        for key in centroids.keys():
            if abs(item - key) < prev_abs:
                prev_abs = abs(item - key)
                value_to_insert = item
                key_spot = key

        centroids.get(key_spot).append(value_to_insert)

    return centroids


# Entry point of application
def main(argv):

    # Print header
    print("CPSC-51100, Summer 2019")
    print("NAME: Eugene Zhuravel. Iam Wodder, Israel Nolazco")
    print("PROGRAMMING ASSIGNMENT #2")
    print("")

    # read file
    points = open_file("prog2-input-data.txt")

    # get user name
    number_clusters = int(input("Enter the number of clusters: "))

    # initialize the first clusters
    clusters = initialize_clusters(number_clusters, points)

    # user len of clusters because initialize_clusters checks to make sure there are fewer clusters
    # than points. Create our first cluster mapping
    old_centroids = initialize_first_centroids(len(clusters), points)
    old_clusters = dict(zip(range(number_clusters), old_centroids.values()))
    
    iteration = 1
    while True:
       
        new_centroids = initialize_new_centroids(old_clusters, points)
        new_clusters = dict(zip(range(number_clusters), new_centroids.values()))
       
        print ("Iteration " + str(iteration))
        count = 0
        for value in old_clusters.values():
            print (str(count) + " " + str(value))
            count = count + 1
        
        # When points don't move between clusters and when the centroids are the same we have achieved
        # the best clustering.
        if (new_clusters == old_clusters) and (new_centroids.keys() == old_centroids.keys()):
            #print("They matched")  # TODO, remove just for example purposes
            break
        else:
            # Assign new clusters to old clusters because we didn't match            
            old_clusters = new_clusters
            old_centroids = new_centroids
            
        
        
        iteration = iteration +1 
        print ()

    # TODO remove, just for verification that I achieve same output as the sample doc
    
    print()
    cluster_num = 0
    for cluster in old_clusters.values():
        for point in cluster:
            print ("Point " + str(point) + " in cluster " + str(cluster_num))
        cluster_num = cluster_num + 1

    # TODO: print result

    pass


if __name__ == "__main__":
    main(sys.argv)

