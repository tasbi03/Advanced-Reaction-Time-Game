import serial
import matplotlib.pyplot as plt

plt.ion()  
fig, ax = plt.subplots()  # Create a figure and an axes

x = list()
y = list()

ser = serial.Serial('/dev/tty.usbmodem1302', 9600)  
ser.close()
ser.open()

try:
    while True:
        data = ser.readline().strip()  
        if data:  
            try:
                score = float(data)
                y.append(score)
                x.append(len(x))  
                ax.clear() 
                ax.plot(x, y, '-o')  
                plt.draw()
            except ValueError as e:
                print(f"Error converting '{data}' to float: {e}")

        plt.pause(0.0001)  

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    ser.close()
    plt.show(block=True)  
