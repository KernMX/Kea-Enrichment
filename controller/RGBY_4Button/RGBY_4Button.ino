#include <Keyboard.h>

void setup() {
  // put your setup code here, to run once:
  //Initialize pins as output
  pinMode(0, INPUT);
  pinMode(1, INPUT);
  pinMode(2, INPUT);
  pinMode(3, INPUT);
}

void loop() {
  if(digitalRead(0)){
    Keyboard.press('r');
    Keyboard.release('r');
  }
  if(digitalRead(1)){
    Keyboard.press('g');
    Keyboard.release('g');
  }
  if(digitalRead(2)){
    Keyboard.press('b');
    Keyboard.release('b');
  }
  if(digitalRead(3)){
    Keyboard.press('y');
    Keyboard.release('y');
  }
}
