void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(4, OUTPUT);
}

int value1 = 0;
int value2 = 0;

int treatValue(int data) {
  return (data * 9 / 1024) + 48;
}


void loop() {
  // put your main code here, to run repeatedly:
  value1 = analogRead(0);
  delay(100);
  value2 = analogRead(1);

//  digitalWrite(4, HIGH);          
//  delay(value1);
//  digitalWrite(4, LOW);
//  delay(value2);

  //Tools -> Serial Monitor
  Serial.print('J');
  Serial.print(treatValue(value1));
  Serial.print('-');
  Serial.println(treatValue(value2));
}
