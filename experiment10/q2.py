# Method overloading find sum of two integer,three integer,four integer and five integers.
class Result:
    def sum(self,*a):
        sum=0
        for x in a:
            sum=sum+x
        print('Sum is :: ',sum)
r=Result()
r.sum(10,20)
r.sum(10,30,40)
r.sum(10,50,60,70)
r.sum(10,70,80,90,100)