#waf ball_collide that takes 2 balls as parameters and computes if they are colliding.
import math
def ball_collide(x1,y1,r1,x2,y2,r2):
    dist=math.sqrt((x2-x1)**2+(y2-y1)**2);
    print("Distance b/w two balls:",dist)
    center=dist/2;
    print("Collision point",center);
    r=r1+r2;
    print("Sum of radious",r)
    if(center<=r):
        print("They are Colliding")
        return True;
    else:
        print("Not Colliding")
        return False;

c=ball_collide(4,4,3,2,2,3)
print(c)