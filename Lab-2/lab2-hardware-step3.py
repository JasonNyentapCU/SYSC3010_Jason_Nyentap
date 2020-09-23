import pigpio
import smbus
import time

#Hardware Used
#1. Futaba S3003 servo motor
#2. Bipolar stepper motor driven by L298N dual H bridge
#3. VEML7700 I2C ambient light sensor

duty = 1600
up = False
address = 0x10
config = [[0x00,0x0000],[0x01,0xFFFF],[0x02,0x0000],[0x03, 0x0000]]

bus = smbus.SMBus(1)
pi = pigpio.pi()
pi.set_mode(25, pigpio.OUTPUT)
pi.set_mode(8, pigpio.OUTPUT)
pi.set_mode(7, pigpio.OUTPUT)
pi.set_mode(24, pigpio.OUTPUT)

pi.write(25,0)
pi.write(8,0)
pi.write(7,0)
pi.write(24,0)

for c in config:
	bus.write_i2c_block_data(address, c[0], [c[1] & 0xFF, c[1] >> 8])

while True:
    
    #This section of code sweeps the servo motor back and forth
    if(up):
        duty = duty + 1
    else:
        duty = duty - 1
        
    if(duty > 1900):
        up = False
        duty = 1900
        time.sleep(0.25)
        
    if(duty < 1100):
        up = True
        duty = 1100
        time.sleep(0.25)
    
    pi.set_servo_pulsewidth(12, duty)
    
    #This section of code steps the servo motor.
    #The motor is using full stepping
    pi.write(25,1)
    pi.write(8,0)
    pi.write(7,0)
    pi.write(24,0)
    time.sleep(0.01)
    pi.write(25,0)
    pi.write(8,0)
    pi.write(7,1)
    pi.write(24,0)
    time.sleep(0.01)
    pi.write(25,0)
    pi.write(8,1)
    pi.write(7,0)
    pi.write(24,0)
    time.sleep(0.01)
    pi.write(25,0)
    pi.write(8,0)
    pi.write(7,0)
    pi.write(24,1)
    time.sleep(0.01)
	
    #This section of code prints out the light sensor reading
    Val = bus.read_i2c_block_data(address, 0x4, 2)
    print("Value: ", Val[0] + (Val[1] << 8))
    time.sleep(0.1);
