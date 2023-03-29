#include <M5Core2.h>
#include <Arduino.h>
#include <WiFi.h>
#include <Free_Fonts.h>
#include <Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"
#include <SD.h>
#include <M5_ENV.h>
#include <Wire.h>

#define DEBUG_PORT Serial
#define API_KEY "AIzaSyDeuDvt1c5fEfgdx3WWwaO5aj8c7BjW2ds" ;
#define DATABASE_URL "https://realtime-database-a9abe-default-rtdb.asia-southeast1.firebasedatabase.app/"

FirebaseData fbdo ;

FirebaseAuth auth;
FirebaseConfig config ;

SHT3X sht30;
QMP6988 qmq6988 ;

float tmp = 0.0 ;
float hum = 0.0 ;
float pressure = 0.0 ;

unsigned long sendDataPrevMillis = 0 ;
int count = 0 ;
bool signupOK = false ;

const char* ssid     = " "; 
const char* password = " " ;

int LOOP_COUTER = 0 ;
int LCD_BRIGHTNESS = 150;


void setup() {

  DEBUG_PORT.begin(115200);

  M5.begin();
  M5.Lcd.setBrightness(150);
  M5.Lcd.setTextColor(0xE73C , TFT_BLACK);
  M5.Lcd.setTextSize(1);
  M5.Lcd.setFreeFont(FF19);

  Wire.begin();
  qmq6988.init();

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid , password);

  M5.lcd.clear();
  M5.Lcd.setCursor(50 ,130) ;
  M5.Lcd.print("Connecting");
  DEBUG_PORT.println("Connecting");

  while(WiFi.status() != WL_CONNECTED){
    DEBUG_PORT.print(".");
    M5.Lcd.print(".");
    delay(100);
  }

  
  DEBUG_PORT.println("=== Start === ");

  M5.lcd.clear();
  M5.Lcd.setCursor(50 ,130) ;
  M5.Lcd.print("=== Start ===");
  DEBUG_PORT.println(WiFi.localIP());

  config.api_key = API_KEY ;
  config.database_url = DATABASE_URL ;

  // Sign up //
  if(Firebase.signUp(&config , &auth , "" , "" )){
    M5.lcd.clear();
    M5.Lcd.setCursor(50 ,130);
    M5.Lcd.print("Firebase SignUp");
    DEBUG_PORT.println("Sign Up Done") ;
    signupOK = true ;
  }
  else{
    DEBUG_PORT.printf("%s\n" , config.signer.signupError.message.c_str());
  }
  
  /* Assign the callback function for the long running token generation task */
  config.token_status_callback = tokenStatusCallback ;

  Firebase.begin(&config , &auth);
  Firebase.reconnectWiFi(true);
  M5.lcd.clear();

}

void loop() {
  if(Firebase.ready() &&signupOK &&(millis() - sendDataPrevMillis > 15000 || sendDataPrevMillis == 0)){
    sendDataPrevMillis = millis();

    pressure = qmq6988.calcPressure();
    if(sht30.get() == 0) {
      tmp = sht30.cTemp ;
      hum = sht30.humidity;
    }
    else{
      tmp = 0 , hum = 0 ;
    }
    DEBUG_PORT.printf("Temp: %2.1f  \r\nHumi: %2.0f%%  \r\nPressure:%2.0fPa\r\n",tmp, hum, pressure);
    int tmp2 = tmp;
    int hum2 = hum ;
    M5.lcd.clear();
    M5.lcd.setCursor(70,130);
    M5.lcd.printf("Temp: %2.1f  \r\n",tmp);
    M5.lcd.setCursor(70,200);
    M5.lcd.printf("Humi: %2.0f%%  \r\n",hum);
    Firebase.RTDB.setInt(&fbdo, "M5/Temp", tmp2);    
    Firebase.RTDB.setInt(&fbdo, "M5/Hum", hum2);
    
  }
  delay(500);
}
