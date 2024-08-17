Initially, we define the pins connected to the Ultrasonic Distance Sensor (HC-SR04): the trig_pin (trigger pin) is connected to pin number 9 on the Arduino, and the echo_pin (echo pin) is connected to pin number 10.

First, we initialize the serial communication at a baud rate of 9600 bits per second. The baud rate indicates the rate at which the signal changes per second. In this case, a baud rate of 9600 means the signal changes 9600 times per second.

Next, we set the trig_pin as an output pin and the echo_pin as an input pin.

Inside the loop() function, the trig_pin is first set to LOW to ensure it is off, followed by a delay of 2 microseconds to make sure the trigger pin is completely off. The trig_pin is then set to HIGH for 10 microseconds to send out the ultrasonic pulse, and it is turned off again.

The long duration variable measures the time taken for the ultrasonic pulse to bounce back to the sensor, as received by the echo_pin. This duration is measured in microseconds.

The distance is then calculated. Given that the speed of sound in air is approximately 343 meters per second, we can convert this to centimeters per microsecond:

Speed of sound: 343 m/s = 34,300 cm/s
1 second = 1,000,000 microseconds
Therefore, the speed of sound is 34,300 cm/s ÷ 1,000,000 µs/s = 0.0343 cm/µs

Using this conversion factor, the distance is calculated and sent to the serial monitor. The program then pauses for 100 milliseconds before taking another measurement.