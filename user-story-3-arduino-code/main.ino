```cpp
const int ledPin = 13;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  digitalWrite(ledPin, HIGH); // turn LED on
  delay(1000);               // wait 1 second
  digitalWrite(ledPin, LOW);  // turn LED off
  delay(1000);               // wait 1 second
}
```