#define CMD_RX_SIZE 3
#define MSG_SIZE 32
#define BAUD_RATE 9600

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
}

void loop(){
	char cmdArray[CMD_RX_SIZE];
//        getCmd(cmdArray);
//        delay(1000);
	if(getCmd(cmdArray)==0){
		execute(cmdArray);
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