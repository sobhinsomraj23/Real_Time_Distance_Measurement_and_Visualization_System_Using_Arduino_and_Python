#define trig_pin 9
#define echo_pin 10

void setup() 
{
  Serial.begin(9600);
  pinMode(trig_pin, OUTPUT);
  pinMode(echo_pin, INPUT);
}

void loop() 
{
  digitalWrite(trig_pin, LOW);
  delayMicroseconds(2);
  digitalWrite(trig_pin,HIGH);
  delayMicroseconds(10);
  digitalWrite(trig_pin, LOW);

  long duration=pulseIn(echo_pin,HIGH);

  float distance=duration * 0.0343/2;

  Serial.println(distance);
  delay(100);
}