#!/usr/bin/env python3

from pyModbusTCP.client import ModbusClient

class Slagboom:
    SERVER_HOST = "192.168.3.134"
    SERVER_PORT = 502
    motor1 = 1
    motor2 = 2
    start_pos = 5
    end_pos = 4
    input_reg = 5391
    output_reg = 00000

    def  __init__(self):
        print("host: "+self.SERVER_HOST+"\tport: "+str(self.SERVER_PORT))
        self.c = ModbusClient(host=self.SERVER_HOST, port=self.SERVER_PORT, auto_open=True, auto_close=True)
        while True:
            self.c.write_single_register(self.output_reg, 0b000100)
            print("output_reg:\t"+str(self.c.read_holding_registers(self.output_reg, 1)[0]))
            start_ret = self.c.read_holding_registers(self.input_reg, 1)[0] & (1 << self.start_pos)
            print("start_sensor_state:\t"+str(start_ret))
            end_ret = self.c.read_holding_registers(self.input_reg, 1)[0] & (1 << self.end_pos)
            print("end_sensor_state:\t"+str(end_ret))
        return
    
    def open_slagboom(self):
        ret = 0
        print("open_slagboom")
        reg = self.c.read_holding_registers(self.output_reg, 1)[0] | (1 << self.input1)
        while not ret:
            self.c.write_single_register(self.output_reg, reg)
            ret = self.c.read_holding_registers(self.input_reg, 1)[0] & (1 << self.start_pos)
            print("input1 on\tstart_sensor_state:\t"+str(ret))
        reg = self.c.read_holding_registers(self.output_reg, 1)[0] & ~(1 << self.input1)
        self.c.write_single_register(self.output_reg, reg)
        return

    def close_slagboom(self):
        ret = 0
        reg = self.c.read_holding_registers(self.output_reg, 1)[0] | (1 << self.input2)
        while not ret:
            self.c.write_single_register(self.output_reg, reg)
            ret = self.c.read_holding_registers(self.input_reg, 1)[0] & (1 << self.end_pos)
            print("input2 on\tend_sensor_state:\t"+str(ret))
        reg = self.c.read_holding_registers(self.output_reg, 1)[0] & ~(1 << self.input2)
        self.c.write_single_register(self.output_reg, reg)
        return

s = Slagboom()
#s.open_slagboom()
#s.close_slagboom()
