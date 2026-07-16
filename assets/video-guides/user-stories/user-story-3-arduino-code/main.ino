const int ledPin = 13;
const unsigned long blinkDelayMs = 1000;
bool ledIsOn = false;

void setup() {
  pinMode(ledPin, OUTPUT);
}

void loop() {
  ledIsOn = true;
  digitalWrite(ledPin, HIGH); // turn LED on
  delay(blinkDelayMs);        // wait 1 second

  ledIsOn = false;
  digitalWrite(ledPin, LOW);   // turn LED off
  delay(blinkDelayMs);         // wait 1 second
}
