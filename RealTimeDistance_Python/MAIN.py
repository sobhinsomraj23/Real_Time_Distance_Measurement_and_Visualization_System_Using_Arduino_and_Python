import serial
import time
import matplotlib.pyplot as plt
import matplotlib.animation as ani

ser=serial.Serial('COM4', 9600)
time.sleep(2)

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')
Xdata, Ydata=[],[]

def update(frame):
    line=ser.readline().decode('utf-8').strip()
    if line:
        distance=float(line)
        Ydata.append(distance)
        Xdata.append(len(Ydata))

        plt.clf()
        ax = plt.gca()
        ax.set_facecolor('black')
        plt.plot(Xdata,Ydata, color='lightgreen')
        plt.grid(color='gray', linestyle='--', linewidth=0.5)
        plt.ylim([0,400])
        plt.title("Real Time Distance Measurement using Arduino and Python")
        plt.xlabel("Time")
        plt.ylabel("Distance in cm")

distance_animation=ani.FuncAnimation(fig,update, interval=100)
plt.show()
ser.close()
