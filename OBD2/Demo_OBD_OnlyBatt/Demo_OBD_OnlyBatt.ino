#include <FreematicsPlus.h>
#include <WiFi.h>
#include <Firebase_ESP_Client.h>
#include "addons/TokenHelper.h"
#include "addons/RTDBHelper.h"
#include <SD.h>

#define DEBUG_PORT Serial
#define API_KEY "AIzaSyDeuDvt1c5fEfgdx3WWwaO5aj8c7BjW2ds" ;
#define DATABASE_URL "https://realtime-database-a9abe-default-rtdb.asia-southeast1.firebasedatabase.app/"
#define PIN_LED 4

FirebaseData fbdo ;

FirebaseAuth auth;
FirebaseConfig config ;

unsigned long sendDataPrevMillis = 0 ;
bool signupOK = false ;

const char* ssid     = "Merlinz_2.4G"; 
const char* password = "1234toei" ;

FreematicsESP32 sys;
COBD obd;
bool connected = true;
unsigned long count = 0;
int count_v = 0;
int Control = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(PIN_LED, OUTPUT);
  digitalWrite(PIN_LED, HIGH);
  delay(1000);
  digitalWrite(PIN_LED, LOW);
  DEBUG_PORT.begin(115200);

  WiFi.mode(WIFI_STA);
  WiFi.begin(ssid , password);

  while(WiFi.status() != WL_CONNECTED){
    DEBUG_PORT.print(".");
    delay(500);
  }
  if(WiFi.status() == WL_CONNECTED) {
    DEBUG_PORT.println("Wifi Connected");
  }

  DEBUG_PORT.println("=== Start === ");

  config.api_key = API_KEY ;
  config.database_url = DATABASE_URL ;

 // Sign up //
  if(Firebase.signUp(&config , &auth , "" , "" )){
    DEBUG_PORT.println("Sign Up Done") ;
    signupOK = true ;
  }
  else{
    DEBUG_PORT.printf("%s\n" , config.signer.signupError.message.c_str());
  }

   // Assign the callback function for the long running token generation task //
  config.token_status_callback = tokenStatusCallback ;

  Firebase.begin(&config , &auth);
  Firebase.reconnectWiFi(true);


}

void loop() {
  digitalWrite(PIN_LED, HIGH);
  if(Firebase.ready() &&signupOK &&(millis() - sendDataPrevMillis > 15000 || sendDataPrevMillis == 0)){
    
    sendDataPrevMillis = millis();

    //Firebase.RTDB.setInt(&fbdo, "OBD2/Control", 0);
    //if (Firebase.RTDB.getInt(&fbdo , "OBD2/Control'")){
      //if (fbdo.dataType() == "int"){
        //Control = fbdo.intData();
      //}
      //if (Control == 1 ){
        //connected = true ;
      //}
    //}

    //int value;
    //DEBUG_PORT.print('[');
    //DEBUG_PORT.print(millis());
    //DEBUG_PORT.print("] #");
    //DEBUG_PORT.print(count++);
    //if (obd.readPID(PID_RPM, value)) {
      //DEBUG_PORT.print(" RPM:");
      //DEBUG_PORT.print(value);
      //Firebase.RTDB.setInt(&fbdo, "OBD2/RPM", value);
    //}
    //if (obd.readPID(PID_SPEED, value)) {
      //DEBUG_PORT.print(" SPEED:");
      //DEBUG_PORT.print(value);
     // Firebase.RTDB.setInt(&fbdo, "OBD2/SPEED", value);
    //}

    DEBUG_PORT.print(" BATTERY:");
    DEBUG_PORT.print(obd.getVoltage());
    //DEBUG_PORT.print('V');
    int v = obd.getVoltage();
    Firebase.RTDB.setInt(&fbdo, "OBD2/BATTERY Voltage", v);
    //if (v < 13) {
      //count_v ++;
    //}

    DEBUG_PORT.print(" CPU TEMP:");
    DEBUG_PORT.print(readChipTemperature());
    DEBUG_PORT.println();
    digitalWrite(PIN_LED, LOW);
  
  //}

    
    DEBUG_PORT.println(Control);
    if(v >= 13){
      Firebase.RTDB.setString(&fbdo, "OBD2/Engine", "Stop");
      Firebase.RTDB.setInt(&fbdo, "OBD2/Control", 0);
    }
    else {
      Firebase.RTDB.setString(&fbdo, "OBD2/Engine", "Stop");
    }
    //if (count_v == 15){
      //count_v = 0;
      //connected = false ;
    //}
    if (Firebase.RTDB.getInt(&fbdo , "OBD2/Control'")){
      if (fbdo.dataType() == "int"){
        Control = fbdo.intData();
      }
    } 
  }    
  delay(1000);
}
