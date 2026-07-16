import pygame

class Sensor:
    def __init__(self, x_position, y_position, radius):
        self.x=x_position
        self.y=y_position
        self.radius=radius
        self.laserspeed=3*10**10 #light speed cm per second

    def update(self, limit, object_position, delta_time):
        self.limit=limit

        #if the object is at the sensor's position
        for i in range(self.x - self.radius, self.x + self.radius): #range(all positional points on the sensor radius)
            for z in range(int(object_position[0])-object_position[2],int(object_position[0])+object_position[2]+1): #range(all positional points on the object radius)
                if z == i :
                    self.y=object_position[1]-object_position[2]*2 #the laser tip positioned above the object
                    return self.y
        
        #if position of the laser tip is not at the limit position
        if limit > self.y:
            if limit > self.laserspeed: 
                return self.y + self.laserspeed * delta_time
            else:
                return limit
        else :
            return self.y
        
    def sensor_render(self, screen):
        #a bunch of circles form a line like a laser
        for i in range(int(self.y)):
            pygame.draw.circle(screen,(255 ,0 ,255), (self.x,self.y-i*2),self.radius)

    def detect(self):
            if self.y < self.limit :
                return True
            else:
                return False
            
    def position(self):
        return self.x, self.y
