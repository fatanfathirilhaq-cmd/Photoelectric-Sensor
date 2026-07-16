import pygame
from sensor import Sensor
from object import Object
from key import Keyboard
from time_measurement import Time
from speed import Speed

pygame.init()
screen=pygame.display.set_mode((600,600))

#default speed
speed_object='100'

#starting position 
object_x_update = 0
sensor1_y_update = 600
sensor2_y_update = 600

#object detection upon contact with sensor
detection_sensor1=False
detection_sensor2=False

#stores a timestamp when the sensor is triggered
history_sensor1=[]
history_sensor2=[]

clock=pygame.time.Clock()

#default font
font=pygame.font.Font(None,16)

running=True
while running:
    for event in pygame.event.get():   
        if event.type == pygame.QUIT:
            running=False
        elif event.type == pygame.KEYDOWN:
            speed_object=Keyboard(event=event, speed=speed_object)
            speed_object=speed_object.speed_text()

    screen.fill((0,0,0))

    #convert speed per frame to speed per second
    delta_time=clock.tick(60)/1000

    #render speed to screen
    speed_render=font.render(f'object speed : {speed_object} cm/s',True,(255,255,255))
    screen.blit(speed_render,(30,50))

    #stopwatch
    stopwatch=Time()
    stopwatch.stopwatch(screen=screen, position=(30,30), size=16)
    
    #object
    object=Object(x_position=object_x_update, y_position=300, radius=5)
    objectposition=object.position()
    object_x_update=object.update(start_position=0, speed_perframe=speed_object, delta_time=delta_time)
    object.object_render(screen)
    
    #sensor no.1
    sensor1=Sensor(x_position=200,y_position=sensor1_y_update, radius=5)
    sensor1_y_update=sensor1.update(limit=600, object_position=objectposition, delta_time=delta_time)
    sensor1position=sensor1.position()
    sensor1.sensor_render(screen)

    detection_sensor1=sensor1.detect()
    stopwatch.get_time(sensor_detect=detection_sensor1, time_history=history_sensor1)
    
    #sensor no.2
    sensor2=Sensor(x_position=400,y_position=sensor2_y_update, radius=5)
    sensor2_y_update=sensor2.update(limit=600, object_position=objectposition, delta_time=delta_time)
    sensor2position=sensor2.position()
    sensor2.sensor_render(screen)
    
    detection_sensor2=sensor2.detect()
    stopwatch.get_time(sensor_detect=detection_sensor2, time_history=history_sensor2)
    
    #all sensor position
    sensorposition=[sensor1position, sensor2position]

    #all history sensor time
    history=[history_sensor1, history_sensor2]

    #render timestamp from the history sensor time
    stopwatch.time_render(time_history=history, screen=screen)

    #speed measurement
    speed_measurement=Speed(time=history, distance=sensorposition)
    speed_measurement.time_sorting()
    speed_measurement.distance_sorting()
    speed_measurement.calculation(screen=screen, font=font)


    
    pygame.display.flip()
pygame.quit()