#include <Servo.h>
Servo myservo;

// 사용자 거리 감지
#define TRIG 9 //TRIG 핀 설정 -> 초음파 send
#define ECHO 8 //ECHO 핀 설정 -> 초음파 get

// 쓰레기통 내부 감지
#define TRIGINNER 12 //TRIG 핀 설정 -> 초음파 send
#define ECHOINNER 11 //ECHO 핀 설정 -> 초음파 get

#define LED_PIN 3 // LED 핀 설정

void setup() {
  Serial.begin(9600);

// /사용자 거리 감지
  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);

// 쓰레기통 내부 감지
  pinMode(TRIGINNER, OUTPUT);
  pinMode(ECHOINNER, INPUT);

  // LED
  pinMode(LED_PIN, OUTPUT);

// 모터
  myservo.attach(2);
  myservo.write(120);
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

  if (distance <= 20) {
    // 모터 열기
    // n 초 후에 자동으로 닫히게
    Serial.println("Object detected. Opening servo...");
    myservo.write(120); 
    delay(5000);       // 3초 대기
    Serial.println("Closing servo...");
    myservo.write(0);  
  }

  long duration_inner, distance_inner;

  digitalWrite(TRIGINNER, LOW);

  delayMicroseconds(2);

  digitalWrite(TRIGINNER, HIGH);

  delayMicroseconds(10);

  digitalWrite(TRIGINNER, LOW);

  duration_inner = pulseIn (ECHOINNER, HIGH);
  distance_inner = duration_inner * 17 / 1000; 

// log 찍기
  Serial.println(duration_inner );
  Serial.print("\nDIstanceInner : ");

  Serial.print(distance_inner);
  Serial.println(" Cm");

  if (distance_inner <= 10) {
    // LED 불빛 나오게
    Serial.println("LED ON");
    digitalWrite(LED_PIN, HIGH);
  } else {
    Serial.println("LED OFF");
    digitalWrite(LED_PIN, LOW);
  }

  delay(1000);


}
