#include <GSM.h>

#define CMD_RX_SIZE 3
#define MSG_SIZE 32
#define BAUD_RATE 9600

// PIN Number for the SIM
#define PINNUMBER ""

// initialize the library instances
GSM gsmAccess;
GSM_SMS sms;

// Array to hold the number a SMS is retreived from
char senderNumber[20];  


typedef void (*cmd)(char, char);

struct cmdStruct{
	char name;
	void (*thatFunc)(char,char);
	char const *msg;
};

struct cmdStruct cmdTable[]={
	{'1', &dw, "dw called"},
	{'2', &ar, "ar called"},
	{'3', &dr, "dr called"},
	{'4', &sp, "sp called"},
	{'0',0,""}
};

int cmdTableSize = sizeof(cmdTable)/sizeof(cmdStruct);

/*---------------- MAIN -----------------------*/

void setup(){
	Serial.begin(BAUD_RATE);
	Serial.println("Init");
	Serial.print("Numero de comandos: ");
	Serial.println(cmdTableSize);

	gsmInit();
}

void loop(){
	char cmdArray[CMD_RX_SIZE];
	char cmdBuffer[8];cmdBuffer[0]='\0';
//        getCmd(cmdArray);
//        delay(1000);
	if(smsGetCmd(cmdBuffer)==0){
		execute(cmdBuffer);
	}	
				delay(100);
}

/*----------------- Cmd Functions --------------------*/


void dw(char pin, char state){
	boolean stateBool;
	int pinInt = pin - '0';
	char msg[MSG_SIZE]; msg[0]='\0';
	
	if (state == '0'){
		stateBool = false;
	}else{
		stateBool = true;
	}
	digitalWrite(pinInt, stateBool);
	
	Serial.println(pinInt);
	sprintf(msg,"Setting pin %d - %d", pinInt, stateBool);
	Serial.println(msg);
}

void sp(char pin, char dir){
  
  	int dirInt;
	int pinInt = pin - '0';
	char msg[MSG_SIZE]; msg[0]='\0';

	if (dir == '0'){
		dirInt = INPUT; 															 // 0 = INPUT
	}else{
		dirInt = OUTPUT;															 // 1 = OUTPUT		
	}
	pinMode(pinInt, dirInt);
	
	sprintf(msg,"Setting pin %d as %d", pinInt, dirInt);
	Serial.println(msg);
}

void ar(char pin, char value){
	int pinInt = pin - '0';
	char msg[MSG_SIZE]; msg[0]='\0';
	int reading;
	
	reading = analogRead(pinInt);

	sprintf(msg,"Aread from pin %d as %d", pinInt, reading);
	Serial.println(msg);
}

void dr(char pin, char value){
	int pinInt = pin - '0';
	char msg[MSG_SIZE]; msg[0]='\0';
	int pinState;

	pinState = digitalRead(pinInt);

	sprintf(msg,"State on pin %d is %d", pinInt, pinState);
	Serial.println(msg);
}


/*-----------------operational functions------------------------------*/

int getCmd(char cmdRx[]){
	int bytesRx;
	if (bytesRx = Serial.available()){
			Serial.print("Bytes in buffer: ");
			Serial.println(bytesRx);
		for(int i = 0; i < (bytesRx); i++){	
			char inChar = Serial.read();
			cmdRx[i] = inChar;
			Serial.println(cmdRx[i]);
		}
		return 0;
	}
	return 1;
}

void execute(char cmdArray[]){
			for (int i = 0; i < (cmdTableSize); i++){
				char cmdByte = cmdTable[i].name;
				if ( cmdByte == cmdArray[0]){
					cmdTable[i].thatFunc(cmdArray[1],cmdArray[2]);
					Serial.println(cmdTable[i].msg);
				}
		}
}

/*--------------------- gsm functions ---------------*/

void gsmInit(){
	Serial.println("SMS command interface");

	boolean notConnected = true;

	while(notConnected){
		if(gsmAccess.begin(PINNUMBER)==GSM_READY){
	  		notConnected = false;
	  	}else{
	  		Serial.println("Not connected");
	  		delay(1000);
		}
	}

	Serial.println("GSM initialized");
	Serial.println("Waiting for commands");
}

int smsGetCmd(char cmdBufferFun[]){
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

	delay(1000);
	return 0;
  }

  delay(1000);
  return 1;
}