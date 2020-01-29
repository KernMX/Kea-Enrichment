#include <Keyboard.h>
//
void setup() {
  // put your setup code here, to run once:
  //Initialize pins as input
  pinMode(0, INPUT);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
  //Output pins for the LEDs
  pinMode(4, OUTPUT); //Green
  pinMode(5, OUTPUT); //red
  pinMode(6, OUTPUT); //blue
  pinMode(7, OUTPUT); //yellow
}

void loop() {
  if(digitalRead(0)){
    Keyboard.press('r');
    Keyboard.release('r');
    digitalWrite(5, HIGH);
    delay(200);
    digitalWrite(5, LOW);
  }
  if(digitalRead(1)){
    Keyboard.press('g');
    Keyboard.release('g');
    digitalWrite(4, HIGH);
    delay(200);
    digitalWrite(4, LOW);
  }
  if(digitalRead(2)){
    Keyboard.press('b');
    Keyboard.release('b');
    digitalWrite(6, HIGH);
    delay(200);
    digitalWrite(6, LOW);
  }
  if(digitalRead(3)){
    Keyboard.press('y');
    Keyboard.release('y');
    digitalWrite(7, HIGH);
    delay(200);
    digitalWrite(7, LOW);
  }
}
