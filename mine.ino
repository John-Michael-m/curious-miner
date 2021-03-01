//include <splash.h>
#include <Wire.h> //For I2C (How the display and board talk to each other)
#include <Arduino.h> //required for screen, idk what rn
#include <U8g2lib.h>
#include <string.h>
U8G2_SSD1306_128X64_NONAME_F_HW_I2C u8g2(U8G2_R2, SCL, SDA, U8X8_PIN_NONE);
int button = 6;
int button1 = 2;
int button2 = 3;
int g = 1;
char buff[30];
//char numGold[100];
unsigned long StartTime = millis();
unsigned long endTime = 600000;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
  u8g2.begin();
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB08_tr);
  while(digitalRead(button) == LOW) {
    u8g2.clearBuffer(); //Clears the screen
    u8g2.drawStr(5,40,"Press Any Button to ");
    u8g2.drawStr(45, 55, "Begin");
    u8g2.sendBuffer();
    Serial.println("don't loop");
  }
  StartTime = millis();

}


void loop() {
  u8g2.firstPage();
do {
  //u8g2.clearBuffer();                   // clear the internal memory
  u8g2.setFont(u8g2_font_ncenB08_tr);   // choose a suitable font
  u8g2.drawStr(45,40,"------->-->>");    // write something to the internal memory <--this works. it's not flashing but also this moves down
  long timeRemaining = 600000 - (millis() - StartTime);
  char buf[20];
  long sec = timeRemaining/1000;
  ltoa(sec, buf, 10);
  if(timeRemaining >= 0){
    u8g2.drawStr(45,35,buf);// i meant for this to be displayed under the arrow yeah. 
    // u8g2.sendBuffer();
    bool bt1state = digitalRead(button1)==LOW;
    bool bt2state = digitalRead(button2)==LOW;
    Serial.println(bt1state);
    Serial.println(bt2state);
    if(bt1state and bt2state) {
      //numGold[100] = g;
      //strcat(numGold, "G");
      itoa(g,buff, 10); 
      u8g2.drawStr(45,55, buff);
      //u8g2.sendBuffer();
      g++;
      delay(1000);
    }
  }else{
    u8g2.clearBuffer();
    u8g2.drawStr(45,55, "TIME'S UP!");
  }
} while (u8g2.nextPage());
  
}
