import os
import machine
from machine import ADC, PWM, Pin
import time



adc = ADC(Pin(34))

adc.atten(ADC.ATTN_11DB)   
adc.width(ADC.WIDTH_12BIT)

newled = PWM(Pin(27), freq = 80000)

def OD(brightness):

    brightness = 30
    newled.duty(brightness)
    button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
    led = machine.Pin(13, machine.Pin.OUT)

    data = []   
    dataTime = []     
    value = 1
    
    while True:
        if not button.value():
            print("Button pressed!")
            value = value + 1
            print(str(value))
            
            while value % 2 == 0:
                led.on()
                print("modulus = 0")
                average = []
                
                for i in range(100):
                    sensor = adc.read()
                    average.append(sensor)
                    time.sleep(0.01)
        
        
                if not button.value():
                    print("Button pressed!")
                    value = value + 1
                    print(str(value))
        
                od = ((sum(average)/len(average))/0.28)-0.65
                data.append(od)
                dataTime.append(time.time())
                time.sleep(2)

                
                if value % 2 != 0:
                    print("Stopping")
                    led.off()
                    break
            break
    saveData(data,dataTime) 
    


def saveData(data, dataTime):
    
    outfile = open('dbdata.txt','w')    
    outfile.write(str(data))
    outfile.write(str(dataTime))
    outfile.close

OD(30)





