from a1 import *
import math

def findMirrorPoint(p,l):
    z1=2*l.a*(l.a*p.x+l.b*p.y+l.c)/(l.a**2+l.b**2)
    z2=2*l.b*(l.a*p.x+l.b*p.y+l.c)/(l.a**2+l.b**2)
    p.x=p.x-z1
    p.y=p.y-z2

def checkSides(p1,p2,l1,l2):
    """
        Taking strictly greater case only,
        as particulars weren't mentioned in question.
    """
    z1=2*l1.a*(l1.a*p1.x+l1.b*p1.y+l1.c)/(l1.a**2+l1.b**2)
    z2=2*l1.b*(l1.a*p1.x+l1.b*p1.y+l1.c)/(l1.a**2+l1.b**2)
    r1=p1.x-z1
    r2=p1.y-z2
    r=Point(r1,r2)
    return((l2.a*r.x+l2.b*r.y+l2.c)*(l2.a*p2.x+l2.b*p2.y+l2.c)>0)
     
def checkIntersection(c1,c2):         
    d=math.sqrt((c1.centre_y-c2.centre_y)**2+(c1.centre_x-c2.centre_x)**2)
    return (((c1.radius+c2.radius)>d) and (d>c1.radius) and (d>c2.radius))


    
    
    
    
