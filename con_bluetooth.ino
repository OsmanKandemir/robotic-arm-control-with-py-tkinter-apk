#include <SoftwareSerial.h>
#include <Servo.h>  
Servo myservo1, myservo2, myservo3, myservo4; 

int bluetoothTx = 10;
int bluetoothRx = 11;  

SoftwareSerial bluetooth(bluetoothTx, bluetoothRx);

void setup()
{
myservo1.attach(3);  
myservo2.attach(5);
myservo3.attach(6);

Serial.begin(9600);  
bluetooth.begin(9600); 
}

void loop()
{
if (bluetooth.available() >= 2 ) 
{
unsigned int servopos = bluetooth.read(); 
unsigned int servopos1 = bluetooth.read(); 
unsigned int realservo = (servopos1 * 256) + servopos;  


//if (realservo >= 1 && realservo <= 135) // tut bırak
//{
//int servo1 = realservo;
//servo1 = map(servo1, 1, 135, 0, 135);
//myservo1.write(servo1);
//delay(10);
//}

if (realservo >= 136 && realservo <= 226) { // sağ sol

int servo2 = realservo;
servo2 = map(servo2, 136, 226, 0, 90);
myservo2.write(servo2);
delay(10);
}

if (realservo >= 227 && realservo <= 406) { // yukarı aşağı
int servo3 = realservo;
servo3 = map(servo3, 227, 406, 0, 180);
myservo3.write(servo3);
delay(10);

}

if (realservo >= 407 && realservo <= 526) { // ileri geri

int servo1 = realservo;
servo1 = map(servo1, 407, 526, 0, 120);
myservo1.write(servo1);
delay(10);

}
}
}
