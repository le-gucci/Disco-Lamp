## once maxed out the angles stop bc they reach 89 and then become ineligble for change. so you must account for dierction

from gpiozero import AngularServo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory
from handy import *

pan = AngularServo(18, min_angle = -90, max_angle = 90, pin_factory = PiGPIOFactory())
tilt = AngularServo(17, min_angle = -90, max_angle = 90, pin_factory = PiGPIOFactory())

def adjust(cx, cy, tx, ty):
        
    MOE = 20

    deltax = cx - tx
    deltay = cy - ty

    if abs(deltax) > MOE:
        if sign(deltax) != sign(pan.angle) or abs(pan.angle) < 89:
            try:
                pan.angle += 1.5*deltax//MOE
                
            except OutputDeviceBadValue:
                pan.angle = 89 * sign(pan.angle)


    if abs(deltay) > MOE:
        if sign(deltay) != sign(tilt.angle) or abs(tilt.angle) < 89:
            try:
                tilt.angle += 1.5*deltay//MOE
                
            except OutputDeviceBadValue:
                tilt.angle = 89 * sign(pan.angle)


#####                neat implementation           ###################

##class Motor(AngularServo):

# adjust method accepts target and current and gets closer? sets in motion or snaps to correct positiion
# shouldn't be "setting" to correct position all the time, just adjusting in the right direction. so we are continuously manipulating/updating motor SPEED
# speed should be based on distance to target. but should have acceleration built in. so should accelerate, cruise, then decellerate as it approaches the target.
# should cap acceleration so as not to pull crazy Gs. call the cap a_max. assume a_min = -a_max
# speed then is irrelevant. constant motion is constant motion
# 1. take distance away from target and divide it by two. spend the first half accelerating and the back half decellerating. always go at the max
# 2. allocate either a period of time or a distance to acceleration. which?
#   2a. allocate a period of time - 0.5 seconds, say - to the accel and decel periods.but if this is a fixed period of time, what do we do if 1 whole second is too much? then spl

# OR allocate a fixed proportion of the *distance* to accel and deccel, and always go at the max. so if its a really short distance, you only accelerate for a moment before cruising and then eventually decellerating.

# we know x. da/dt is always 0 or undefined.
# x = 0.5a_maxt^2 + 
# say we divide each distance into fourths and dedicate the first and last fourth to chadning speed. then if x is one of those chunks,
# using max acceleration makes sense if the distance is odlong. but if its short like does it? idk i dont have the intuition for this yet. if you need to calculate time later then you use kinematics.

#def adjust(motor, delta_n):

#    for motor in motors
#    sign = delta_n/abs(delta_n) ## becomes either 1 or -1
#    motor.angle += 1*sign



# in a more complex robotic arm each motor would have perhaps an id, a dedicate degree of freedom (which corresponds to a dictionary where like x and y for instance have associated things like deltax... or maybe not.