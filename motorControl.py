from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

pan = AngularServo(18, min_angle = -90, max_angle = 90, pin_factory = PiGPIOFactory())
tilt = AngularServo(17, min_angle = -90, max_angle = 90, pin_factory = PiGPIOFactory())


#cx = frame.shape[1]//2
#cy = frame.shape[0]//2

#cx/cy = center of screen x and y
#tx/ty = target x and y

def adjust(cx, cy, tx, ty):
        
    MOE = 20

    deltax = cx - tx
    deltay = cy - ty

    if abs(deltax) > MOE:
        sign = deltax/abs(deltax) ## becomes either 1 or -1
        if abs(pan.angle) < 90:
            pan.angle += 1*sign

    if abs(deltay) > MOE:
        sign = deltay/abs(deltay)
        if abs(tilt.angle) < 90:
            tilt.angle += 1*sign


#####                neat implementation           ###################

##class Motor(AngularServo):


#def adjust(motor, delta_n):

#    for motor in motors
#    sign = delta_n/abs(delta_n) ## becomes either 1 or -1
#    motor.angle += 1*sign
