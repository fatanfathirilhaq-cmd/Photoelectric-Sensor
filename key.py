import pygame

class Keyboard:
    def __init__(self, event, speed):
        self.event=event
        self.speed=speed

    def speed_text (self):
        #backspace
        if self.event.key == pygame.K_BACKSPACE:
            self.speed=self.speed[:-1]
            if self.speed == '':
                self.speed='0'
                return self.speed
            else :
                return self.speed
        
        #insert a number
        elif self.event.unicode.isnumeric():
            if self.speed=='0': #remove 0 when self.speed is exactly 0
                self.speed=self.event.unicode
                return self.speed
            else:
                self.speed+=self.event.unicode
                return self.speed
            
        #insert a comma
        elif self.event.unicode == ','or self.event.unicode == '.' :
            self.speed+='.'
            return self.speed
        else :
            return self.speed