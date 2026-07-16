import pygame

class Time:
    def __init__(self):
        self.second = pygame.time.get_ticks()/1000 #time in seconds
        self.milisecond = pygame.time.get_ticks() #time in miliseconds

    def stopwatch(self, screen, position, size):
        self.font = pygame.font.Font(None, size)

        #convert to digital stopwatch
        second = self.second % 60
        minute = self.second // 60
        milisecond = self.second % 1 * 100

        stopwatch_text = f"{int(minute):02d}:{int(second):02d}:{int(milisecond):02d}"

        stopwatch_font=self.font.render(stopwatch_text, True, (255,255,255))
        screen.blit(stopwatch_font,(position[0],position[1]))

    def get_time(self, sensor_detect, time_history):
        if len(time_history) == 0: #add empty element and default time (00:00:00)
            time_history += [[]]+[[0]]
   
        elif sensor_detect == True and len(time_history[0]) == 0: #add the timestamp the first time sensor detect True, on the empty element
            time_history[0] = [self.milisecond]

        elif sensor_detect == False and len(time_history[0]) == 1: #add the timestamp the first time sensor detect False as the element fills
            time_history[0] = time_history[0]+[self.milisecond]
            time_history[0:0] += [[]]    #add empty element for next timestamp
            
    def time_render(self, time_history, screen):
        for x, y in zip(time_history,range(len(time_history))):
            if len(x[0])>0:     #render the time history when the element populated
                #convert to digital stopwatch
                second= x[0][0] /1000 % 60 
                minute= x[0][0] /1000 // 60 
                milisecond= x[0][0] /1000 % 1 * 100 

                stopwatch_text= f"sensor {y+1} detect : {int(minute):02d}:{int(second):02d}:{int(milisecond):02d}"

                stopwatch_render=self.font.render(stopwatch_text, True, (255,0,255))
                screen.blit(stopwatch_render, (30,75+y*10))
                
            else:        #render the time history when the element is empty
                #convert to digital stopwatch
                second= x[1][0] /1000 % 60 
                minute= x[1][0] /1000 // 60 
                milisecond =x[1][0] /1000 % 1 * 100 
                
                stopwatch_text= f"sensor {y+1} detect : {int(minute):02d}:{int(second):02d}:{int(milisecond):02d}"

                stopwatch_render=self.font.render(stopwatch_text, True, (255,0,255))
                screen.blit(stopwatch_render, (30,75+y*10))