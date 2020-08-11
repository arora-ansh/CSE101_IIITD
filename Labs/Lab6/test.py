from introcs import *
from a1 import *
from module import *

p1=Point(3,4)
p2=Point(3,-3)
l1=Line(1,1,-7)
l2=Line(-1,2,-1)

findMirrorPoint(p1,l1)
findMirrorPoint(p2,l2)

assert_equals(3,p1.x)
assert_equals(4,p1.y)
print("Test1 Passed")
assert_equals(-1,p2.x)
assert_equals(5,p2.y)
print("Test2 Passed")

s1=Point(3,4)
s2=Point(3,-1)
t1=Line(0,1,0)
t2=Line(0,1,-1)
assert_equals(True,checkSides(s1,s2,t1,t2))
print("Test3 Passed")
q1=Point(3,-3)
q2=Point(-5,-7)
r1=Line(1,-2,1)
r2=Line(1,1,1)
assert_equals(False,checkSides(q1,q2,r1,r2))
print("Test4 Passed")

ca1=Circle(0,0,5)
ca2=Circle(6,0,2)
cb1=Circle(0,0,4)
cb2=Circle(7,0,2)

assert_equals(True,checkIntersection(ca1,ca2))
print("Test5 Passed")
assert_equals(False,checkIntersection(cb1,cb2))
print("Test6 Passed")

