from class_test import Person
import numpy as np
import cmath  

x=Person()
y=np.sin(4)
print(x.age)
print(y)
word="hi"
word="hi"+str(1)
print(word)

de=[35,40,45,50,55]

for i in de:
    cos=np.cos(np.deg2rad(i))
    sin=np.sin(np.deg2rad(i))
    sx=80.3*cos+5.3-40
    sy=280-80.3*sin
    a=sy-sin/cos
    b=0
    c=981/2

    d = (b**2) - (4*a*c)
    t = (-b+cmath.sqrt(d))/(2*a)

    print(t)