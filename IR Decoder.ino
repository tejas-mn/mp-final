#include <IRremote.h>

int RECV_PIN = 10; 

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()

{

  pinMode(9,OUTPUT); digitalWrite(9,LOW);// GND

  pinMode(8,OUTPUT); digitalWrite(8,HIGH);//VCC

  Serial.begin(115200);

  

  Serial.println("Enabling IRin");

  irrecv.enableIRIn(); // Start the receiver

  Serial.println("Enabled IRin");

}

void loop() {

  if (irrecv.decode()) {

    Serial.println(irrecv.decodedIRData.decodedRawData, HEX);

    irrecv.resume(); // Receive the next value

  }

  

  delay(50);

}
