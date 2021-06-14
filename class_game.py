import numpy as np
import pygame
class Velocity:
    def __init__(self,input_V_x,input_V_y):
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
        self.rect = pygame.Rect(posi_x_input, posi_y_input, size_x_input, size_y_input)
        self.color_active = pygame.Color(color1_input)
        self.color_passive = pygame.Color(color2_input)
        self.color = color_passive
        self.active = False
        self.Text = Text_input

        self.base_font = pygame.font.Font(None, 32)