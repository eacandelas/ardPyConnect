typedef void (*cmd)(char, char);

struct cmdStruct{
	char name;
	void (*thatFunc)(char,char);
	char const *msg;
};

struct cmdStruct cmdTable[4]={
	{'1', &dw, "dw called"},
	{'2', &fun2, "fun2 called"},
	{'3', &fun3, "fun3 called"},
	{'4', &setPins, "setPins called"},
	{'0',0,""}
};

int cmdTableSize = sizeof(cmdTable)/sizeof(cmdStruct);

/*---------------- MAIN -----------------------*/

void setup(){
	Serial.begin(9600);
	Serial.println("Init");
	Serial.print("Numero de comandos: ");
	Serial.println(cmdTableSize);
}

void loop(){
	char cmdArray[3];
//        getCmd(cmdArray);
//        delay(1000);
	if(getCmd(cmdArray)==0){
		excute(cmdArray);
	}	
				delay(1000);
}

/*----------------- Functions --------------------*/


void dw(char pin, char state){
	boolean stateBool;
	int pinInt = pin - '0';
	char msg[32]; msg[0]='\0';
	
	if (state == '0'){
		stateBool = false;
	}else{
		stateBool = true;
	}
	digitalWrite(pinInt, stateBool);
	
	Serial.println(pinInt);
	sprintf(msg,"Setting pin %d - %d", pinInt, dirInt);
	Serial.println(msg);
}

void setPins(char pin, char dir){
  
  int dirInt;
	int pinInt = pin - '0';
	char msg[32]; msg[0]='\0';

	if (dir == '0'){
		dirInt = INPUT; 															 // 0 = INPUT
	}else{
		dirInt = OUTPUT;															 // 1 = OUTPUT		
	}
	pinMode(pinInt, dirInt);
	
	sprintf(msg,"Setting pin %d as %d", pinInt, dirInt);
	Serial.print(msg);
}

void fun2(char pin, char value){
	analogWrite(pin, value);
	Serial.println("soy fun2");
}
void fun3(char pin, char value){
	Serial.println("soy fun3");
	Serial.println(pin);
	Serial.println(value);
}

int getCmd(char cmdRx[]){
	int bytesRx;
	if (bytesRx = Serial.available()){
								Serial.print("bytes in buffer");
								Serial.println(bytesRx);
		for(int i = 0; i < (bytesRx); i++){	
			char inChar = Serial.read();
			cmdRx[i] = inChar;
		}
		for(int i = 0; i < (bytesRx); i++){	
			Serial.println(cmdRx[i]);

		}
		return 0;
	}
	return 1;
}


void execute(char cmdArray[]){
			for (int i=0; i < (cmdTableSize); i++){
				char cmdByte = cmdTable[i].name;
				if ( cmdByte == cmdArray[0]){
					cmdTable[i].thatFunc(cmdArray[1],cmdArray[2]);
					Serial.println(cmdTable[i].msg);
				}
		}
}