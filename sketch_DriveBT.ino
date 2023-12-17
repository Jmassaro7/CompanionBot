#define CUSTOM_SETTINGS
#define INCLUDE_GAMEPAD_MODULE
#include <Dabble.h>

#include <Arduino.h>
#include "PWMDcMotor.hpp"

//create two DC Motor objects
PWMDcMotor rightMotor;
PWMDcMotor leftMotor;

static uint8_t sMotorDirection = DIRECTION_FORWARD; //global static declaration of forward direction value, used in many functions
uint8_t option = 0; //set option selected to 0

//global IR sensor pin numbers used in setup() and loop()
//<TODO change pin numbers when building physical bot>
int leftFront = 38;
int leftRear = 39;
int rightFront = 36;
int rightRear = 37;

/***************************************************
 * This is a function whose purpose is to allow the*
 * user to controll the companion bot through the  *
 * dabble app.                                     *
 **************************************************/
int rcConnect()
{
    
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);      // make sure your Serial Monitor is also set at this baud rate.
  Dabble.begin(9600);      //Enter baudrate of your bluetooth.Connect bluetooth on Bluetooth port present on evive.
  
  //initialize motors (IN1,IN2,PWM)
  leftMotor.init(24,25,3); // (AIN1, AIN2)
  rightMotor.init(27,26,2); // (BIN1, BIN2)

  //com pins and modes
  pinMode(50, OUTPUT); //is ready
  pinMode(52, INPUT);  //is drive
  pinMode(53, INPUT);  //is dance

  //set IR pin modes
  pinMode(leftFront, INPUT);
  pinMode(leftRear, INPUT);
  pinMode(rightFront, INPUT);
  pinMode(rightRear, INPUT);

}

void loop() {
  digitalWrite(50, HIGH);
  
//BEGIN EDGE DETECTION
  //BEGIN corner detection
  /*while(digitalRead(leftFront)==LOW)
  {
    leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
    delay(1000);
    leftMotor.stop();
    rightMotor.stop();
    delay(10);
  }
  
  while(digitalRead(leftRear)==LOW)
  {
    leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
    delay(1000);
    leftMotor.stop();
    rightMotor.stop();
    delay(10);
  }
  
  while(digitalRead(rightFront)==LOW)
  {
      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);
      leftMotor.stop();
      rightMotor.stop();
      delay(10);
  }
  while(digitalRead(rightRear)==LOW)
  {
    rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
    delay(1000);
    leftMotor.stop();
    rightMotor.stop();
    delay(10);
  }
  //END corner detection
  
  //whole front detection
  while(digitalRead(leftFront)==LOW&&digitalRead(rightFront)==LOW)
  {
      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);

      leftMotor.stop();
      rightMotor.stop();
      delay(10);
  }
  //whole back detection
  while(digitalRead(leftRear)==LOW&&digitalRead(rightRear)==LOW)
  {
      rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(1000);

      leftMotor.stop();
      rightMotor.stop();
      delay(10);
  }

  //Whole front and back detection
  while(digitalRead(leftFront)==LOW && digitalRead(rightFront)==LOW && digitalRead(leftRear)==LOW && digitalRead(rightRear)==LOW)
  {
    leftMotor.stop();
    rightMotor.stop();
    delay(10);
  }*/
//END EDGE DETECTION
  
  //START default option
  while (option == 0)
  {
    digitalWrite(50, HIGH); //is ready since HIGH
    Serial.print("Ready to perform Arduino function. \n");
    
    //TO drive
    if (digitalRead(52) == HIGH)//is_drive set
    {
      Serial.print("Transitioning to Arduino drive function.\n");
      option = 9;
    }

    //TO dance
    if (digitalRead(53) == HIGH)//is_dance set
    {
      Serial.print("Transitioning to Arduino dance function.\n");
      option = 1;
    }

    //debug
    if (digitalRead(52)==HIGH && digitalRead(53)==HIGH)
    {
      Serial.print("ERROR: Drive and Dance are both selected\n");
    }
  }
  //END default option


  //BEGIN dance option
  if (option == 1)
  {
      
      Serial.print("Not ready to return control. In Arduino Dance Function\n");

      //dance sequence begin
      rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(1000);

      leftMotor.stop();
      rightMotor.stop();
      delay(10);

      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);
      
      leftMotor.stop();
      rightMotor.stop();
      delay(10);

      rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(1000);

      leftMotor.stop();
      rightMotor.stop();
      delay(10);

      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);

      
      leftMotor.stop();
      rightMotor.stop();
      delay(1000);
      option = 0;
      digitalWrite(50, LOW);
  }
  //END dance option

  
  //BEGIN drive option
  while (option == 9)
  {
    
    Serial.print("Not ready to return control. In Arduino Drive Function\n\n");
    Dabble.processInput();// used to get data from a bluetooth enabled device

    /*if(digitalRead(leftFront) == LOW)
    {
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(1000);
      leftMotor.stop();
      rightMotor.stop();
      delay(10);
    }
    
    if(digitalRead(leftRear) == LOW)
    {
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);
      leftMotor.stop();
      rightMotor.stop();
      delay(10);
    }
    
    if(digitalRead(rightFront) == LOW)
    {
        rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
        delay(1000);
        leftMotor.stop();
        rightMotor.stop();
        delay(10);
    }
    if(digitalRead(rightRear) == LOW)
    {
      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(1000);
      leftMotor.stop();
      rightMotor.stop();
      delay(10);
    }
    //END corner detection
    
    //whole front detection
    if(digitalRead(leftFront) == LOW && digitalRead(rightFront) == LOW)
    {
        rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
        leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
        delay(1000);
  
        leftMotor.stop();
        rightMotor.stop();
        delay(10);
    }
    //whole back detection
    if(digitalRead(leftRear) == LOW && digitalRead(rightRear) == LOW)
    {
        rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
        leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
        delay(1000);
  
        leftMotor.stop();
        rightMotor.stop();
        delay(10);
    }
  
    //Whole front and back detection
    if(digitalRead(leftFront) == LOW && digitalRead(rightFront) == LOW && digitalRead(leftRear) == LOW && digitalRead(rightRear) == LOW)
    {
      leftMotor.stop();
      rightMotor.stop();
      delay(10);
    }*/
    
    if (GamePad.isUpPressed())
    {
      Serial.print("up\n");
  
      rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(100);
      
    }
  
    if (GamePad.isDownPressed())
    {
      Serial.print("down\n");
  
      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(100);
    }
  
    if (GamePad.isLeftPressed())
    {
      Serial.print("left\n");
  
      rightMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      leftMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      delay(100);
    }
  
    if (GamePad.isRightPressed())
    {
      Serial.print("right\n");
  
      rightMotor.setSpeedPWMAndDirection(255, oppositeDIRECTION(sMotorDirection));
      leftMotor.setSpeedPWMAndDirection(255, sMotorDirection);
      delay(100);
    }

    //return to default option
    if (GamePad.isCrossPressed())
    {
      Serial.print("Cross\n");
      Serial.print("return to default\n");
      option = 0;
      digitalWrite(50, LOW); //is not ready
    }
    
    //stop motors
    leftMotor.stop();
    rightMotor.stop();
    delay(1);
  }
  //END drive option

}
  
  
