#include <Servo.h>
 
Servo myservo1,myservo2,myservo3;
int aci = 1;
int aci2 = 1;
int aci3 = 1;
int pos = 90;   
 
void setup() {
        Serial.begin(9600); 
        myservo1.attach(5); 
        myservo2.attach(3);
        myservo3.attach(6);
}
 
void loop() {
 
        // send data only when you receive data:
        while (Serial.available() > 0) {
                // read the incoming byte:
                int c = Serial.read();
                
                if(c>=1 && c<=35){
                   delay(2);
                   myservo1.write(c*5);
                   

                  }
                if(c>=36 && c<=71){
                  delay(2); 
                  myservo2.write((c-35)*5);
                  
                  }
                 if(c>=72 && c<=130){
                  delay(5); 
                  myservo3.write((c-71)*5);
                  
                  }
                delay(2);   
                // say what you got:
                Serial.print("C is ");
                Serial.println(c, DEC);
                
                
        }
}
