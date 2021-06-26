import numpy as np
import pygame
from resolution import *

#now use x1, x2..


class Velocity:
    def __init__(self,input_V_x=0,input_V_y=0):
        self.V_x=input_V_x
        self.V_y=input_V_y
        self.gravity=9.81

    def get_position_x(self,time):
        return self.V_x*time*scale

    def get_position_y(self,time):
        return (self.V_y*time-1/2*(self.gravity*100)*(time**2))*scale
    
    def setspeed(self,speed_input,degree,g):
        speed_input=speed_input*100
        self.V_x=speed_input*np.cos(np.deg2rad(degree))
        self.V_y=speed_input*np.sin(np.deg2rad(degree))
        self.gravity=g


class Button:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input='yellow',color2_input='pink'):
        self.base_font = pygame.font.Font(None, base_front)
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = self.color_passive
        self.active = False
        self.Text = Text_input
    
    def change(self):
        if(self.active):
            self.color= self.color_active
        else:
            self.color= self.color_passive

    def check(self,pos):
        if(self.rect_class.collidepoint(pos)):
            self.active = True
            return 1
        else:
            return 0

    def draw(self,screen):
        self.change()
        pygame.draw.rect(screen,self.color,self.rect_class)
        text_surface_time = self.base_font.render(self.Text, True, (0, 0, 0))
        screen.blit(text_surface_time, (self.rect_class.x+40, self.rect_class.y+5))

class labbel:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input="Gray ",bool=True,word1="",word2="",size_front=front_labbel):
        self.base_font = pygame.font.Font(None, size_front)
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color = pygame.Color(color1_input)
        self.Text = Text_input
        self.word_front=word1;
        self.word_end=word2;
        self.bool=bool;

    def draw(self,screen):
        x=0
        if(self.bool):
            x=5
            pygame.draw.rect(screen,self.color,self.rect_class)

        dummy=self.Text + "     "
        dummy= self.word_front + dummy + self.word_end
        text_surface_time = self.base_font.render(dummy, True, (0, 0, 0))
        screen.blit(text_surface_time, (self.rect_class.x+10, self.rect_class.y+x))
    def update_text(self,text_input):
        self.Text = text_input

class Input_box:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",not_use= True,word1="",word2="",color1_input='BLUE',color2_input='chartreuse4'):
        self.base_font = pygame.font.Font(None, base_front)
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = self.color_passive
        self.active = False
        self.Text = Text_input
        self.off = not_use
        self.word_front=word1;
        self.word_end=word2;
        self.default_value=self.Text

    def change(self):
        if(self.off):
            self.color = pygame.Color("gray")
        elif(self.active):
            self.color= self.color_active
        else:
            self.color= self.color_passive

    def check(self,pos):
        if(not(self.off)):
            if(self.rect_class.collidepoint(pos)):
                self.active = True
                return 1
            else:
                return 0
        else:
            return 0

    def draw(self,screen):
        self.change()
        pygame.draw.rect(screen,self.color,self.rect_class)
        dummy=self.Text + "     "
        dummy=dummy[0:5]
        text_surface_time = self.base_font.render(self.word_front + dummy + self.word_end, True, (255, 255, 255))
        screen.blit(text_surface_time, (self.rect_class.x+10, self.rect_class.y+5))

    def new_word(self,event):
        if(self.active and not(self.off)):
            if event.key == pygame.K_BACKSPACE:
                self.Text = self.Text[:-1]
            else:
                if(len(self.Text)<4):
                    self.Text += event.unicode

class Check_box:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,color1_input='chartreuse4',color2_input='lightskyblue3'):
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = self.color_passive
        self.active = True

    def change(self):
        if(self.active):
            self.color= self.color_active
        else:
            self.color= self.color_passive

    def check(self,pos):
        if(self.rect_class.collidepoint(pos)):
            if(self.active):
                self.active = False
            else:
                self.active = True
            return 1
        else:
            return 0

    def draw(self,screen):
        self.change()
        pygame.draw.rect(screen,self.color,self.rect_class)
    
class ball:
    def __init__(self,size_intput=1,posi_x_input=0,posi_y_input=0,color1_input='red',speed_input=500,degree=45):
        self.posi_x_add=posi_x_input
        self.posi_y_add=posi_y_input
        self.size=size_intput
        self.color=color1_input
        self.posi_x=0
        self.posi_y=0
        self.v= Velocity()
        self.v.setspeed(speed_input, degree,9.81)

    def run(self,screen,time):
        self.posi_x=self.v.get_position_x(time)+self.posi_x_add+size_ui_x
        self.posi_y=size_pic_y-self.posi_y_add-self.v.get_position_y(time)
        pygame.draw.circle(screen,self.color, (self.posi_x,self.posi_y), self.size)

    def check_fall(self,time):
        if(self.v.get_position_y(time)+self.posi_y_add<-1):
            return True
        else:
            return False
    def setsize(self,size_intput):
        if(size_intput>1):
            self.size=size_intput*10
        else:
            self.size=10
    def setposion_start(self,x,y):
        self.posi_x_add=x
        self.posi_y_add=y

class Tail:
    def __init__(self,list_x=[],list_y=[],size_intput=1,color1_input='red'):
        self.x = list_x
        self.y = list_y
        self.circile_list = []
        self.color="red"
        self.size=size_intput
        self.color=color1_input

    def add_position(self,x,y):
        self.x.append(x)
        self.y.append(y)

    def draw(self,screen):
        for i in range(len(self.x)):
            pygame.draw.circle(screen,self.color, (self.x[i],self.y[i]), self.size)
    
    def reset(self):
        self.x = []
        self.y = []

    """
def findVfromk(k,m,o,g,x):
    sin=np.sin(np.deg2rad(o))
    v=(1/2*k*x*x-m*g*x*sin)*2/m
    v=np.sqrt(v)
    return v

def findxfromv(k,m,o,g,v):
    sin=np.sin(np.deg2rad(o))
    a=k/2
    b=-1*m*g*sin
    c=-1/2*m*v*v
    # print("a : %.3f \tb : %.3f \tc : %.3f" % (a,b,c))
    x=eqation(a,b,c)
    # print(x)
    return x
"""
def findVfromk(k,m,x):
    v=k*x*x/m
    v=np.sqrt(v)
    return v

def findxfromv(k,m,v):
    x=v*v*m/k
    x=np.sqrt(x)
    return x
def findvfromo(sx,sy,g,o):

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
        # print("a : %.3f \tb : %.3f \tc : %.3f" % (a,b,c))
        # print("error root less < 0")
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
    percent=0.1
    up_level=1+percent*0.01
    low_level=1-percent*0.01
    jearn=10
    # print("in")  
    for i in range(89*jearn,1,-1):
        # print()
        o_degree=i/jearn
        o_rad=np.deg2rad(o_degree)
        cos_loop=np.cos(o_rad)
        sin_loop=np.sin(o_rad)
        t_loop=eqation(g/2,v*-1*sin_loop,sy)
        if(t_loop==0):
            # print("v : %.3f \tsin : %.3f" % (v,sin_loop))
            # print("a : %.3f \tb : %.3f \tc : %.3f" % (g/2,v*-1*sin_loop,sy))
            # print("degree : %.3f\tsx_need : %.3f\tsy_need : %.3f" %(o_degree,sx_need,sy))
            # print("t_loop : %.3f\tsx_loop : %.3f" %(t_loop,sx_loop))
            continue
        sx_loop=v*cos_loop*t_loop

        
        if(sx_loop>=sx_need * low_level and sx_loop<=sx_need * up_level):
            #* that ok
            # print("ok %.2f",%(o_degree))
            return o_degree
        else:
            continue

    print("fall")
    return -5

def findofromv(sx_need,sy,g,v):
    omax_rad=findomax(sy,g,v)

    cos_o=np.cos(omax_rad)
    sin_o=np.tan(omax_rad)
    
    t=eqation(g/2,v*-1*sin_o,sy)
    if(t==0):
        # print("error root < 0 ")
        return 0
    sx_max=v*cos_o*t
    if(sx_max<sx_need):
        # print("cannot shoot")
        return 0
    else:
        print("can shoot")
        return loop_findo(sx_need,sy,g,v)