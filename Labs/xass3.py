import math
import random

def dist(p1,p2):
	return ((p1[1]-p2[1])**2+(p1[0]-p2[0])**2)**(1/2)					#uses the formula sqrt(delx^2 + dely^2) to compute distance

def sort_points_by_X(points):
	n=len(points)														#used bubble sort to arrange points in ascending order of x coordinate values
	for i in range(n):
		for j in range(0,n-i-1):
			if points[j][0]>points[j+1][0]:
				points[j],points[j+1]=points[j+1],points[j]
	return points

def sort_points_by_Y(points):
	n=len(points)														#used bubble sort to arrange points in ascending order of y coordinate values
	for i in range(n):
		for j in range(0,n-i-1):
			if points[j][1]>points[j+1][1]:
				points[j],points[j+1]=points[j+1],points[j]
	return points

def naive_closest_pair(plane):

	mp1_code = 0
	mp2_code = 0
	minlen = float('inf')
	n = len(plane)
	for i in range(n-1):
		for j in range(i+1,n):
			if minlen>dist(plane[i],plane[j]):
				mp1_code = i
				mp2_code = j
				minlen = dist(plane[i],plane[j])
				
	return [minlen,plane[mp1_code],plane[mp2_code]]

def closest_pair_in_strip(points, d):
	n = len(points)
	x=d
	mp1_code = 0
	mp2_code = 0
	for i in range(n-1):
		if (n-i)>=6:
			for j in range(i+1,i+6):
				if dist(points[i],points[j])<d:
					d=dist(points[i],points[j])
					mp1_code=i
					mp2_code=j
		else:
			for	j in range(i+1,n):
				if dist(points[i],points[j])<d:
					d=dist(points[i],points[j])	
					mp1_code=i
					mp2_code=j
	if d<x:
		return [d,points[mp1_code],points[mp2_code]]
	else:
		return -1

def efficient_closest_pair_routine(points):

	n=len(points)
	if n<=2:
		if n==1:
			return [None,points[0],None]
		elif n==2:
			return naive_closest_pair(points)
	
	mid=n//2
	s1=points[:mid]
	s2=points[mid:]
	d1=efficient_closest_pair_routine(s1)
	d2=efficient_closest_pair_routine(s2)
	if d1[0]==None and d2[0]!=None:
		d=d2[0]
	elif d1[0]!=None and d2[0]==None:
		d=d1[0]
	else:
		d=min(d1[0],d2[0])
	if d==d1[0]:
		final=d1
	else :
		final=d2
	for x in points:
		if x[0]<(points[mid][0]-d) or x[0]>(points[mid][0]+d):
			points.remove(x)
	points=sort_points_by_Y(points)
	l=closest_pair_in_strip(points,d)
	if l == -1:
		return final
	else:
		return l
	
def efficient_closest_pair(points):

	points=sort_points_by_X(points)
	fin=efficient_closest_pair_routine(points)
	return fin

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
    num_pts = 7
    #size of plane for generation of points
    plane_size = (10, 10) 
    plane = generate_plane(plane_size, num_pts)
    print(plane)
    print(naive_closest_pair(plane))
    print(efficient_closest_pair(plane))