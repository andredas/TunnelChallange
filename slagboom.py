#!/usr/bin/env python3

from pyModbusTCP.client import ModbusClient

class Slagboom:
    SERVER_PORT = 502
    input1 = 0b000001
    input2 = 0b000010
    start_pos = 0b000001
    end_pos = 0b000010
    input_reg = 5391
    output_reg = 00000

    def  __init__(self, host):
        self.SERVER_HOST = host
        print("host: "+self.SERVER_HOST+"\tport: "+str(self.SERVER_PORT))
        self.c = ModbusClient(host=self.SERVER_HOST, port=self.SERVER_PORT, auto_open=True, auto_close=True)
        return
    
    def open_slagboom(self):
        ret = 0
        while not ret:
            self.c.write_single_register(self.output_reg, self.input1)
            ret = self.c.read_holding_registers(self.input_reg, 1)[0] & self.star_pos
        return

    def close_slagboom(self):
        ret = 0
        while not ret:
            self.c.write_single_register(self.output_reg, self.input2)
            ret = self.c.read_holding_registers(self.input_reg, 1)[0] & self.stop_pos
        
        return

s = Slagboom("192.168.3.134")
#s.open_slagboom()
#s.close_slagboom()
