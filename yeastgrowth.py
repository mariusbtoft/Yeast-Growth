import numpy as np
import matplotlib.pyplot as plt
import math

f = open("yeastGrowth.txt", "r")

time = []
ADC = []

for lines in f:
    split = lines.split("	")
    time.append(str(split[0]))
    ADC.append(str(split[1]))


time = time[2:]
timeData = []
ADC = ADC[2:]
ADCData = []



for i in range(len(time)):
    timeData.append(float(time[i]))
    ADCData.append(float(ADC[i]))



OD = []
for i in range(len(timeData)):
    OD.append(-math.log(float(ADC[i])/2100,10))

loglist = []
for i in range(len(OD)):
    loglist.append(math.log(OD[i]))



dy = []

for i in range(len(timeData)-1):
    dy.append(((OD[i+1]-OD[i])/(timeData[i+1]-timeData[i]))/OD[i+1])
    

#curve = np.polyfit(timeData[20:-1],dy[20:],3)
#poly = np.poly1d(curve)
#newy = []




testpoints = 10
polypoints = []
for i in range(len(timeData)-(2*testpoints)):
    y_test = loglist[0+i:20+i]
    x_test = timeData[0+i:20+i]
    curvepoly = np.polyfit(x_test, y_test, 1)
    polypoints.append(curvepoly[0])

#print(polypoints)    
plt.plot(timeData[10:-10],polypoints)
print("The maximum growth rate is " + str(max(polypoints)))
print((np.log(2))/(max(polypoints)))




#for i in range(len(timeData[20:-1])):
 #   calc = poly(i+1)
  #  newy.append(calc)

#plt.plot(timeData, loglist)
#plt.plot(timeData[42:101], loglist[42:101])
#plt.plot(timeData,OD)
#plt.plot(timeData[20:-1],dy[20:])
#plt.plot(timeData[20:-1], newy)

plt.show()

m = (loglist[101]-loglist[42])/(timeData[101]-timeData[42])
#print(m)
