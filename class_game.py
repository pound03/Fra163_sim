import numpy as np
import pygame


#now use x1, x2..
size_ui=200
size_screen_wide=1286+size_ui
size_screen_hight=720

class Velocity:
    def __init__(self,input_V_x=0,input_V_y=0):
        self.V_x=input_V_x
        self.V_y=input_V_y
        self.realx=self.V_x
        self.realy=self.V_y

    def get_position_x(self,time):
        return self.V_x*time

    def get_position_y(self,time):
        return self.V_y*time-1/2*(981)*(time**2)

    def resetpositon(self):
        self.V_x=self.realx
        self.V_y=self.realy
    
    def setspeed(self,speed_input,degree):
        self.V_x=speed_input*np.cos(np.deg2rad(degree))
        self.V_y=speed_input*np.sin(np.deg2rad(degree))
        self.realx=self.V_x
        self.realy=self.V_y

class Button:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input='lightskyblue3',color2_input='chartreuse4'):
        self.base_font = pygame.font.Font(None, 32)
        self.rect_class = pygame.Rect(posi_x_input, size_screen_hight-posi_y_input, size_x_input, size_y_input)
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
        text_surface_time = self.base_font.render(self.Text, True, (255, 255, 255))
        screen.blit(text_surface_time, (self.rect_class.x+40, self.rect_class.y+5))

class labbel:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input="white "):
        self.base_font = pygame.font.Font(None, 24)
        self.rect_class = pygame.Rect(posi_x_input, size_screen_hight-posi_y_input, size_x_input, size_y_input)
        self.color = pygame.Color(color1_input)
        self.Text = Text_input
    def draw(self,screen):
        pygame.draw.rect(screen,self.color,self.rect_class)
        text_surface_time = self.base_font.render(self.Text, True, (0, 0, 0))
        screen.blit(text_surface_time, (self.rect_class.x+40, self.rect_class.y+5))
    def update_text(self,text_input):
        self.Text = text_input

class Input_box:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,Text_input="",color1_input='lightskyblue3',color2_input='chartreuse4'):
        self.base_font = pygame.font.Font(None, 32)
        self.rect_class = pygame.Rect(posi_x_input, size_screen_hight-posi_y_input, size_x_input, size_y_input)
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
        text_surface_time = self.base_font.render(self.Text, True, (255, 255, 255))
        screen.blit(text_surface_time, (self.rect_class.x+10, self.rect_class.y+5))
    def new_word(self,event):
        if(self.active):
            if event.key == pygame.K_BACKSPACE:
                self.Text = self.Text[:-1]
            else:
                self.Text += event.unicode

class Check_box:
    def __init__(self,posi_x_input,posi_y_input,size_x_input,size_y_input,color1_input='lightskyblue3',color2_input='chartreuse4'):
        self.rect_class = pygame.Rect(posi_x_input, size_screen_hight-posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = self.color_passive
        self.active = False

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
    def __init__(self,size_intput=1,posi_x_input=size_ui,posi_y_input=size_screen_hight,color1_input='red',speed_input=500,degree=45):
        self.posi_x=posi_x_input
        self.posi_y=posi_y_input
        self.size=size_intput
        self.color=color1_input

        self.v= Velocity()
        self.v.setspeed(speed_input, degree)

    def run(self,screen,time):
        pygame.draw.circle(screen,self.color, (self.v.get_position_x(time)+self.posi_x,self.posi_y-self.v.get_position_y(time)), self.size)

    def check_fall(self,time):
        if(self.v.get_position_y(time)<-1):
            self.v.resetpositon()
            return True
        else:
            return False