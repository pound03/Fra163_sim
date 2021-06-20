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
        self.base_font = pygame.font.Font(None, 32)
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
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input="Gray "):
        self.base_font = pygame.font.Font(None, 28)
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color = pygame.Color(color1_input)
        self.Text = Text_input
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect_class)
        text_surface_time = self.base_font.render(self.Text, True, (255, 255, 255))
        screen.blit(text_surface_time, (self.rect_class.x+10, self.rect_class.y+5))
    def update_text(self,text_input):
        self.Text = text_input

class Input_box:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",bool= True,word1="",word2="",color1_input='BLUE',color2_input='chartreuse4'):
        self.base_font = pygame.font.Font(None, 32)
        self.rect_class = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = self.color_passive
        self.active = False
        self.Text = Text_input
        self.off = bool
        self.word_front=word1;
        self.word_end=word2;

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
        if(self.v.get_position_y(time)<-1):
            return True
        else:
            return False
    def setsize(self,size_intput):
        if(size_intput>1):
            self.size=size_intput*10
        else:
            self.size=10

def findVfromk(k,m,x):
    v=k*x*x/m
    v=np.sqrt(v)
    return v

def findxfromv(k,m,v):
    x=v*v*m/k
    x=np.sqrt(x)
    return x

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