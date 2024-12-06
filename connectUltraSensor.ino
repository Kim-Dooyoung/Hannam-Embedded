#include <Servo.h>
Servo myservo;

#define TRIG 9 //TRIG 핀 설정 -> 초음파 send
#define ECHO 8 //ECHO 핀 설정 -> 초음파 get

void setup() {
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

  myservo.attach(2);
  myservo.write(0);
}

void loop() {
  long duration, distance;

  digitalWrite(TRIG, LOW);

  delayMicroseconds(2);

  digitalWrite(TRIG, HIGH);

  delayMicroseconds(10);

  digitalWrite(TRIG, LOW);

  duration = pulseIn (ECHO, HIGH);
  distance = duration * 17 / 1000; 

// log 찍기
  Serial.println(duration );
  Serial.print("\nDIstance : ");

  Serial.print(distance);
  Serial.println(" Cm");

  // delay(1000);

  if (distance <= 20) {
    // 모터 열기
    // n 초 후에 자동으로 닫히게
    Serial.println("Object detected. Opening servo...");
    myservo.write(90); 
    delay(5000);       // 3초 대기
    Serial.println("Closing servo...");
    myservo.write(0);  
  }

  delay(1000);


}
