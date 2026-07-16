import pygame

class Object:
    def __init__(self, x_position, y_position, radius):
        self.x=x_position
        self.y=y_position
        self.radius=radius

    def object_render(self, screen):
        pygame.draw.circle(screen,(255 ,0 ,0), (self.x, self.y),self.radius)

    def update(self, speed_perframe, start_position, delta_time):
        if self.x < 600 :
            return self.x+float(speed_perframe) * delta_time
        else :
            self.x = start_position
            return self.x
        
    def position(self):
        return self.x, self.y, self.radius
        
    