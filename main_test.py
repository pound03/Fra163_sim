import class_test
import numpy as np
import cmath  
from resolution import *
from sympy import symbols, Eq, solve
import os

def findvfromo(sx,sy,g,o):
    sy=-sy
    degree=np.deg2rad(o)
    tan=np.tan(degree)
    cos=np.cos(degree)
    a=tan*sx
    b=(g*sx*sx)/(cos*cos*2)
    v0=(sy-a)/(-b)
    v0=np.sqrt(v0)
    v0=1/v0
    v0=round(v0,5)
    # print(a,end="a\n")
    # print(sy-a,end="sy-a\n")
    # print(b,end="b\n")
    # print(v0,end="v0\n")
    # print(v0,end="vroot\n")
    return v0

def eqation(a,b,c):
    # calculate the discriminant  
    d = (b**2) - (4*a*c)
    # print("b**2 : %.3f\t4*a*c : %.3f" % (b**2,4*a*c))
    if(d<0):
        print("error root less < 0")
        return 0
    # find two solutions  
    sol1 = (-b-np.sqrt(d))/(2*a)  
    sol2 = (-b+np.sqrt(d))/(2*a)
    # return [sol1,sol2]
    if(sol1 > sol2):
        # print(sol1)
        return sol1
    else:
        # print(sol2)
        return sol2

def findomax(sy,g,v):
    a=2*g*(-sy)+v*v
    b=2*g*(-sy)+2*v*v
    coso=np.sqrt(a/b)
    jearn_rad=np.arccos(coso)
    jearn_degree=np.rad2deg(jearn_rad)
    return jearn_rad

def loop_findo(sx_need,sy,g,v):
    percent=1
    up_level=1+percent*0.01
    low_level=1-percent*0.01
    jearn=1
    # print("in")  
    for i in range(80*jearn,40,-1):
        # print()
        o_degree=i/jearn
        o_rad=np.deg2rad(o_degree)
        cos_loop=np.cos(o_rad)
        sin_loop=np.sin(o_rad)
        # print("v : %.3f \tsin : %.3f" % (v,sin_loop))
        # print("a : %.3f \tb : %.3f \tc : %.3f" % (g/2,v*-1*sin_loop,sy))
        t_loop=eqation(g/2,v*-1*sin_loop,sy)
        print("degree : %.3f\tsx_need : %.3f\tsy_need : %.3f" %(o_degree,sx_need,sy))
        """
        for j in t_loop:
            sx_loop=v*cos_loop*j
            print("t_loop : %.3f\tsx_loop : %.3f" %(j,sx_loop))
            if(sx_loop>=sx_need * low_level and sx_loop<=sx_need * up_level):
            #* that ok
                return o_degree
        """
        sx_loop=v*cos_loop*t_loop

        print("t_loop : %.3f\tsx_loop : %.3f" %(t_loop,sx_loop))
        if(sx_loop>=sx_need * low_level and sx_loop<=sx_need * up_level):
            #* that ok
            # print("ok")
            return o_degree
        else:
            continue

    print("fall")
    return 0

def findofromv(sx_need,sy,g,v):
    omax_rad=findomax(sy,g,v)

    cos_o=np.cos(omax_rad)
    sin_o=np.tan(omax_rad)
    
    t=eqation(g/2,v*-1*sin_o,sy)
    if(t==0):
        print("error root < 0 ")
        return 0
    sx_max=v*cos_o*t
    if(sx_max<sx_need):
        print("cannot shoot")
        return 0
    else:
        print("can shoot")
        return loop_findo(sx_need,sy,g,v)

# kim=findofromv(2.24,0.25,9.81,5)
# print(kim)
print("hello")
ob=class_test.student("kim",18)
ob.showname()
# a.changename("jearn")
# a.showname()




eqation(9.81/2,-1*2*np.sin(np.deg2rad(0)),-1)

"""
findomax(1,9.81,5)
path = os.listdir("lilac\lilac3\edit")
print(path)
if(35>=35):
    print("Hello")

x = symbols('x')
eq1 = Eq(x**2 -5*x + 6)
sol = solve(eq1)
print(sol)

x=Person()
y=np.sin(4)
print(x.age)
print(y)
word="hi"
word="hi"+str(1)
print(word)

de=[35,40,45,50,55]

s="hello"
num=len(s)
print(num)
"""

