/*
 SMS receiver
 
 This sketch, for the Arduino GSM shield, waits for a SMS message 
 and displays it through the Serial port. 
 
*/

// include the GSM library
#include <GSM.h>

// PIN Number for the SIM
#define PINNUMBER ""

// initialize the library instances
GSM gsmAccess;
GSM_SMS sms;

// Array to hold the number a SMS is retreived from
char senderNumber[20];  

void setup() 
{
  	pinMode(9,OUTPUT);
	digitalWrite(9,LOW);
	delay(2000);
	digitalWrite(9,HIGH);  // initialize serial communications and wait for port to open:
  	Serial.begin(9600);
  	while (!Serial) {
	; // wait for serial port to connect. Needed for Leonardo only
  } 

  Serial.println("SMS Messages Receiver");
	
  // connection state
  boolean notConnected = true;
  
  // Start GSM connection
  while(notConnected)
  {
	if(gsmAccess.begin(PINNUMBER)==GSM_READY)
	  notConnected = false;
	else
	{
	  Serial.println("Not connected");
	  delay(1000);
	}
  }
  
  Serial.println("GSM initialized");
  Serial.println("Waiting for messages");
}

void loop() 
{
	char cmdBuffer[8];cmdBuffer[0]='\0';
	smsGetCmd(cmdBuffer);
	// Serial.print("cmdBuffer: ");
	// Serial.print(cmdBuffer);

}

void smsGetCmd(char cmdBufferFun[]){
  int i = 0;
  int c;
  // If there are any SMSs available()  
  if (sms.available())
  {
	Serial.println("Message received from:");
	
	// Get remote number
	sms.remoteNumber(senderNumber, 20);
	Serial.println(senderNumber);

	// Read message bytes and print them
	while(c=sms.read()){
		cmdBufferFun[i]=c;	
		Serial.println(cmdBufferFun[i]);
		i++;
	}
	cmdBufferFun[i] = '\0';
	Serial.print("cmdBufferFun: ");
	Serial.print(cmdBufferFun);

	  
	Serial.println("\nEND OF MESSAGE");
	
	// Delete message from modem memory
	sms.flush();
	Serial.println("MESSAGE DELETED");
  }

  delay(1000);
}

