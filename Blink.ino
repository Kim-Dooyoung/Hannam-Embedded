#include <Servo.h>
Servo myservo;

int trig = 3; // 초음파 센서 send
int echo = 4; // 초음파 센서 get
int servo = 9; // 서브모터

void setup()
{
  Serial.begin(9600);
  //초음파센서
  pinMode(trig, OUTPUT);
  pinMode(echo, INPUT);
  //서브모터
  myservo.attach(servo);
  //적외선센서
  pinMode(6, INPUT);
  pinMode(12, OUTPUT);
  pinMode(13, OUTPUT);
}

void loop(){
  //초음파센서, 서브모터
  long duration, distance;

//  digitalWrite(echo, LOW);
//  digitalWrite(trig, LOW);
//  delayMicroseconds(2);
  digitalWrite(trig, HIGH);
  delayMicroseconds(10);
  digitalWrite(trig, LOW);

  duration = pulseIn(echo, HIGH);

  Serial.print("duration = ");
  Serial.println(duration);
  
  distance = duration/29/2;

  Serial.print("distance = ");
  Serial.println(distance);

// 쓰레기통 열기
  if(distance < 10)
  {
    myservo.write(180);
    delay(3000);
     myservo.write(0);
  }
//  else {
//    
//  }
  
  
  //적외선센서
  int val = digitalRead(6);
//  Serial.print(val);

  if (val== 0 )
  {
    digitalWrite(13,HIGH);
    digitalWrite(12,HIGH);
  }
  else
  {
    digitalWrite(13,LOW);
    digitalWrite(12,LOW);
  }
  delay(30);
}
