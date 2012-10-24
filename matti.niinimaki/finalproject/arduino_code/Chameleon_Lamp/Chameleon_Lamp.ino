/* Chameleon Lamp by Matti Niinimäki
 * Made for the Digital Fabrication Studio course at Aalto Fablab
 * 
 * The SoftI2CMaster library is needed to run this:
 * https://github.com/todbot/SoftI2CMaster
 * (based on the example code that comes with the library)
 */

const boolean testingI2CReads = false;

const byte sclPin = 5;  // digital pin 5 wired to 'c' on BlinkM
const byte sdaPin = 4;  // digital pin 4 wired to 'd' on BlinkM
const byte pwrPin = 6;  // not used
const byte gndPin = 7;  // not used

#include "SoftI2CMaster.h"
#include "BlinkM_funcs_soft.h"

byte blinkm_addr = 9;
byte r,g,b;

void setup()
{
  Serial.begin( 19200 );
  Serial.println("BlinkMSoftI2CDemo");
  
  // Pin 2 used for powering the sensor
  // Pin 3 used for setting the gain of the sensor.
  // All of the gain pins were wired together
  pinMode(2,OUTPUT);
  pinMode(3,OUTPUT);
  digitalWrite(2,HIGH);
  digitalWrite(3,LOW);
  
  BlinkM_begin( sclPin, sdaPin, pwrPin, gndPin );
 
  delay(100);

  BlinkM_off(0);
  BlinkM_setFadeSpeed( blinkm_addr, 5);

  for( int i=0; i< 10; i++ ) {  // flash the blinkms
    BlinkM_setRGB( blinkm_addr, 255,255,255 );
    delay(20);
    BlinkM_setRGB( blinkm_addr, 0,0,0 );
    delay(20);
  }
  
  if( testingI2CReads ) { 
    Serial.print("BlinkM version: ");
    int num = BlinkM_getVersion( blinkm_addr );
    char major_version = (char)(num>>8);
    char minor_version = (char)(num&0xff);
    Serial.print( major_version );
    Serial.println( minor_version );
    if( major_version == -1 ) {
        Serial.println("\nERROR: couldn't find a BlinkM\n");
    }
  }
}

void loop()
{
  // Read the RGB sensor
  r = analogRead(A3);
  g = analogRead(A2);
  b = analogRead(A1);
  
  // Map the values
  r = constrain(map(r,32,60,0,255),0,255);
  g = constrain(map(g,45,80,0,255),0,255);
  b = constrain(map(b,20,45,0,255),0,255);
  
  Serial.print("Setting r,g,b:"); Serial.print(r);
  Serial.print(",");      Serial.print(g);
  Serial.print(",");      Serial.println(b);
  
  BlinkM_fadeToRGB( blinkm_addr, r,g,b);

  if( testingI2CReads ) {
    for( int i=0; i<10; i++ ) {
      showCurrentColor();
      delay(100);
    }
  } 
  else {
    delay(100);
  }
}

//
void showCurrentColor()
{
  byte r,g,b;
  BlinkM_getRGBColor( blinkm_addr, &r,&g,&b);

  Serial.print("        r,g,b:"); Serial.print(r,HEX);
  Serial.print(",");      Serial.print(g,HEX);
  Serial.print(",");      Serial.println(b,HEX);
}



