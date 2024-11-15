// Pin definitions for Ultrasonic Sensor 1 (Volume)
const int trigPin1 = 9;
const int echoPin1 = 10;

// Pin definitions for Ultrasonic Sensor 2 (Frequency)
const int trigPin2 = 11;
const int echoPin2 = 12;

//LED pins
const int volPins[4] = {4,5,6,7};

const int freqPins[4] = {2,3,8,13};


// Variables to store sensor readings
long duration1, distance1; // For volume
long duration2, distance2; // For frequency

// Timing variables
unsigned long previousMillis = 0;  // Store last sensor read time
const long interval = 100;         // 100 ms interval for sensor readings

void setup() {
  Serial.begin(9600); // Initialize serial communication

  // Setup ultrasonic sensor pins
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

   for (int i = 0; i < 4; i++) {
    pinMode(volPins[i], OUTPUT);
    digitalWrite(volPins[i], LOW);
  }
  for (int i = 0; i < 4; i++) {
    pinMode(freqPins[i], OUTPUT);
    digitalWrite(freqPins[i], LOW);
  }
}

void loop() {
  unsigned long currentMillis = millis();

  // Check if 300ms have passed to read sensors
  if (currentMillis - previousMillis >= interval) {
    previousMillis = currentMillis;  // Update time

    // Measure distance from Sensor 1
    distance1 = getDistance(trigPin1, echoPin1); // Volume control (5-25 cm)

    // Wait for 100ms to prevent interference
    delay(100);

    // Measure distance from Sensor 2
    distance2 = getDistance(trigPin2, echoPin2); // Frequency control (5-25 cm)

    // Print only distance1 and distance2 to the serial monitor
    Serial.print(distance1); // Print distance1 (Volume)
    Serial.print("  ");      // Print space separator
    Serial.println(distance2); // Print distance2 (Frequency)

    // Map volume sensor to the number of LEDs to light up (1-5)
  int numvolLeds = map(distance1, 5, 25, 1, 4);
  numvolLeds = constrain(numvolLeds, 1, 4); // Ensure valid range

  int numfreqLeds = map(distance2, 5, 25, 1, 4);
  numfreqLeds = constrain(numfreqLeds, 1, 4);

  // Light up LEDs based on volume
  for (int i = 0; i < 4; i++) {
    if (i < numvolLeds) {
      digitalWrite(volPins[i], HIGH); // Turn on LED
    } else {
      digitalWrite(volPins[i], LOW);  // Turn off LED
    }
  }
  
  for (int i = 0; i < 4; i++) {
    if (i < numfreqLeds) {
      digitalWrite(freqPins[i], HIGH); // Turn on LED
    } else {
      digitalWrite(freqPins[i], LOW);  // Turn off LED
    }
  }


  }
}

// Function to measure distance using an ultrasonic sensor
long getDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH); // Measure echo time
  long distance = duration * 0.034 / 2;   // Convert to distance in cm
  return distance;
}
