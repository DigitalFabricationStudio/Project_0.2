import sftp.*;

Sftp sftp;
PImage img;

void setup() {
  size(900,600);
  background(0);

  // Create the SFTP object
  // if 3rd argument is false, you must set the password in your code
  // if 3rd argument is true, you will be prompted to enter your password
  sftp = new Sftp("192.168.0.13","pi", false);
  sftp.setPassword("raspberry");
  sftp.start(); // start the thread
  long time = millis();
  while(millis()-time < 10000); //wait for connection...
  frameRate(1);
}

void draw() {
  sftp.executeCommand("get webcam/crop.png");
  img = loadImage("crop.png");
  image(img, 0, 0, width, height);
}

