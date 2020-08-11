"""
CSE101: Introduction to Programming
Assignment 3

Name        :   Ansh Arora
Roll-no     :   2019022
"""



import math
import random



def dist(p1, p2):
    """
    Find the euclidean distance between two 2-D points

    Args:
        p1: (p1_x, p1_y)
        p2: (p2_x, p2_y)
    
    Returns:
        Euclidean distance between p1 and p2
    """
    return ((p1[1]-p2[1])**2+(p1[0]-p2[0])**2)**(1/2)                   #uses the formula sqrt(delx^2 + dely^2) to compute distance




def sort_points_by_X(points):
    """
    Sort a list of points by their X coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by X coordinate
    """
    n=len(points)                                                       #used bubble sort to arrange points in ascending order of x coordinate values
    for i in range(n):
        for j in range(0,n-i-1):
            if points[j][0]>points[j+1][0]:
                points[j],points[j+1]=points[j+1],points[j]
    return points



def sort_points_by_Y(points):
    """
    Sort a list of points by their Y coordinate

    Args:
        points: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]
    
    Returns:
        List of points sorted by Y coordinate 
    """
    n=len(points)                                                       #used bubble sort to arrange points in ascending order of y coordinate values
    for i in range(n):
        for j in range(0,n-i-1):
            if points[j][1]>points[j+1][1]:
                points[j],points[j+1]=points[j+1],points[j]
    return points


def naive_closest_pair(plane):
    """
    Find the closest pair of points in the plane using the brute
    force approach

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    mp1_code = 0                                                        #initial placeholder values given for mp1_code and mp2_code
    mp2_code = 0
    minlen = float('inf')                                               #infinity is taken as initial minimum length
    n = len(plane)
    for i in range(n-1):                                                #Nested loop is used to compare each point w each point
        for j in range(i+1,n):
            if minlen>dist(plane[i],plane[j]):                          #Each time a distance lesser than the previous least distance is found out, 
                mp1_code = i                                            #minimimum points and minimum distance are assigned their new values
                mp2_code = j
                minlen = dist(plane[i],plane[j])
                
    return [minlen,plane[mp1_code],plane[mp2_code]]    



def closest_pair_in_strip(points, d):
    """
    Find the closest pair of points in the given strip with a 
    given upper bound. This function is called by 
    efficient_closest_pair_routine

    Args:
        points: List of points in the strip of interest.
        d: Minimum distance already found found by 
            efficient_closest_pair_routine

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)] if
        distance between p1 and p2 is less than d. Otherwise
        return -1.
    """
    n = len(points)                                                     #takes in sorted points and finds out the number of points in the list
    x=d                                                                 #x is assigned initial value of d to check for unchanged condition in the end(d is infact the minimum distance)
    mp1_code = 0
    mp2_code = 0
    for i in range(n-1):                                                #Each point is compared with its next nearest 5 points, to find set of points with distance lesser than original d and the new minimum length
        if (n-i)>=6:
            for j in range(i+1,i+6):
                if dist(points[i],points[j])<d:
                    d=dist(points[i],points[j])
                    mp1_code=i
                    mp2_code=j
        else:                                                           #A flow of control has been added to keep sure that the list out of range error is avoided for the last 5 elements.
            for j in range(i+1,n):
                if dist(points[i],points[j])<d:
                    d=dist(points[i],points[j]) 
                    mp1_code=i
                    mp2_code=j
    if d<x:                                                             #Checks whether there is infact a change in the value of initial d and returns the new values, otherwise just returns a -1.
        return [d,points[mp1_code],points[mp2_code]]
    else:
        return -1



def efficient_closest_pair_routine(points):
    """
    This routine calls itself recursivly to find the closest pair of
    points in the plane. 

    Args:
        points: List of points sorted by X coordinate

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    n=len(points)                                                       #First checks the number of points being returned in recursion to the fucntion
    if n<=2:                                                            #Means that we have reached the final level of division
        if n==1:                                                        #If just one value remaining after dividing the previous level, we take the distance between points and the 2nd points as None, hence returning just the single point
            return [None,points[0],None]
        elif n==2:                                                      #If two values remain, we just find out the distance between the two and return it along with the two points
            return [dist(points[0],points[1]),points[0],points[1]]
    
    mid=n//2                                                            #Middle point to draw the middle line
    s1=points[:mid]                                                     #The points are divided into two sets
    s2=points[mid:]
    d1=efficient_closest_pair_routine(s1)                               #The function is called recursively, and assigned to the new sets d1 and d2, for s1 and s2 respectively, until final level is reached
    d2=efficient_closest_pair_routine(s2)
    d=0
    if d1[0]==None and d2[0]!=None:                                     #Takes care of the single point left case by assinging the mindistance value accordingly
        d=d2[0]
    elif d1[0]!=None and d2[0]==None:
        d=d1[0]
    else:                                                               #If the last level has two sets of two points
        d=min(d1[0],d2[0])

    if d==d1[0]:                                                        #Checks to which set does d belong to, and assigns the set to final
        final=d1
    else :
        final=d2

    for x in points:                                                    #Loop checks for point lying outside the line-d line+d set and eliminates them
        if x[0]<(points[mid][0]-d) or x[0]>(points[mid][0]+d):
            points.remove(x)

    points=sort_points_by_Y(points)                                     #Points sorted by y coordinate
    l=closest_pair_in_strip(points,d)                                   #Function is ran, in which the points are compared with the adjacent next 5 points

    if l == -1:                                                         #If the prev function returns -1, it means that the preexisting value for d was the least and hence returns final, which holds the points for that distance and the distance
        return final
    else:                                                               #If there is a new least value extracted from the prev function, we return that value
        return l                                                        



def efficient_closest_pair(points):
    """
    Find the closest pair of points in the plane using the divide
    and conquer approach by calling efficient_closest_pair_routine.

    Args:
        plane: List of points [(p1_x, p1_y), (p2_x, p2_y), ...]

    Returns:
        Distance between closest pair of points and closest pair 
        of points: [dist_bw_p1_p2, (p1_x, p1_y), (p2_x, p2_y)]
    """
    points=sort_points_by_X(points)                                    #Points are sorted by x coordinate and passed into the routine function, as asked for
    fin=efficient_closest_pair_routine(points)
    return fin                                                         #Final answer returned



def generate_plane(plane_size, num_pts):
    """
    Function to generate random points.

    Args:
        plane_size: Size of plane (X_max, Y_max)
        num_pts: Number of points to generate

    Returns:
        List of random points: [(p1_x, p1_y), (p2_x, p2_y), ...]
    """
    
    gen = random.sample(range(plane_size[0]*plane_size[1]), num_pts)
    random_points = [(i%plane_size[0] + 1, i//plane_size[1] + 1) for i in gen]

    return random_points



if __name__ == "__main__":  
    #number of points to generate
    num_pts = 10
    #size of plane for generation of points
    plane_size = (10, 10) 
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    #naive_closest_pair(plane)
    #efficient_closest_pair(plane)