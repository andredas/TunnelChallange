from pyModbusTCP.client import ModbusClient
import time;
# TCP auto connect on first modbus request
c = ModbusClient(host="192.168.3.135", port=502, auto_open=True)

# managing TCP sessions with call to c.open()/c.close()
print(c.open());
ja = 0;
while(1):
	x = c.read_holding_registers(5391,1)
	if (x[0] == 1):
		time1 =  time.time()
		ja = 1
		while(x[0] == 1):
			x= c.read_holding_registers(5391,1)
	if(x[0] == 2):
		if( ja == 1):
			ja = 0
			time2 = time.time() - time1
			s=5/time2
			s=s/100*3600/1000
			print( s)
		else:
			print("spookrijder")
			print (ja)
		while(x[0] == 2):
			x = c.read_holding_registers(5391,1);
print(x)

