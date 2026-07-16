class Speed:
    def __init__(self, time, distance):
        self.temporary_time=time
        self.temporary_distance=distance

        self.time=[[[],[]]]*(len(time)-1) #create the list according to the number of sensor
        self.distance=[]

    def time_sorting(self):
        for x, y in zip(self.temporary_time, range(len(self.temporary_time))): #(time history, time history sequence)
            if len(x[0])>0:
                if y-1 < 0: #if the earliest time sequence ([x],[y],..)
                    self.time[0][0]=int(x[0][0])
                elif y-1 >= 0 and y+1 < len(self.temporary_time)-1: #if the time sequence in between 2 other time sequences (..,[y],[x],[z],..)
                    self.time[y][0]=int(x[0][0])
                    self.time[y-1][1]=int(x[0][0])
                elif y-1 >= 0 and y+1 >= len(self.temporary_time)-1: #if the time sequence is at the end (..,[y],[x])
                    self.time[y-1][1]=int(x[0][0])
            else:
                if y-1 < 0: #if the earliest time sequence ([x],[y],..)
                    self.time[0][0]=int(x[1][0])
                elif y-1 >= 0 and y+1 < len(self.temporary_time)-1: #if the time sequence in between 2 other time sequences (..,[y],[x],[z],..)
                    self.time[y][0]=int(x[1][0])
                    self.time[y-1][1]=int(x[1][0])
                elif y-1 >= 0 and y+1 >= len(self.temporary_time)-1: #if the time sequence is at the end (..,[y],[x])
                    self.time[y-1][1]=int(x[1][0])

    def distance_sorting(self):
        temporary_value=[]
        for x in self.temporary_distance:
                temporary_value+=[x[0]]
                if len(temporary_value)==2:
                    self.distance.append(temporary_value[:])
                    temporary_value.clear()

    def calculation(self, screen, font):
        for x,y in zip(self.time, self.distance): 
            #time
            time=(int(x[1])-int(x[0]))/1000

            if time > 0 :
                time_text=f'Time interval : {time} s'
            else:
                time_text=f'Time interval : -'
        
            time0=f'Inital time : {x[0]} ms'
            timet=f'Final time : {x[1]} ms'

            time_render=font.render(time_text, True, (0,255,0))
            time0render=font.render(time0, True, (0,255,0))
            timetrender=font.render(timet, True, (0,255,0))

            screen.blit(time_render,(30,130)) 
            screen.blit(time0render,(30,110))  
            screen.blit(timetrender,(30,120))  
            
            #distance
            distance=int(y[1])-int(y[0]) 

            distance_text=f"distance : {distance} cm"
            distance0=f'position sensor 1 : {y[0]} cm'
            distancet=f"position sensor 2 : {y[1]} cm"
        
            distance_render=font.render(distance_text, True, (0,255,0))
            distance0_render=font.render(distance0, True, (0,255,0))
            distancet_render=font.render(distancet, True, (0,255,0))

            screen.blit (distance_render,(30,170))
            screen.blit(distance0_render,(30,150))
            screen.blit(distancet_render,(30,160))

            #speed
            if time > 0 :
                speed=(distance/time)
                speed_text=f"Measured speed : {str(speed)[:5]} cm/s"
            else:
                speed_text=f"Measured speed : -"

            speed_render=font.render(str(speed_text), True, (0,255,0))
            screen.blit(speed_render,(30,190))     