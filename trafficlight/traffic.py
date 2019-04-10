from pyModbusTCP.client import ModbusClient

import time

modus = 0


class Traffic:
    beschikbaar = 0
    

    adress = 0
    rood_aan = 0b000100
    geel_aan = 0b001000
    groen_aan = 0b010000
    gedoofd = 0b000000

    time1 = time.time()

    def __init__(self):
        self.stand = 3
        self.c = ModbusClient(host="192.168.3.135", port=502, auto_open=True)

    def getStatus(self):
        return self.beschikbaar

    def setStand(self,modus):
        self.stand = modus

    def update_light(self):
        if self.stand == 3:
            self.c.write_single_register(self.adress, self.rood_aan)
        elif self.stand == 1:
            self.c.write_single_register(self.adress, self.geel_aan)
        elif self.stand == 0:
            self.c.write_single_register(self.adress, self.groen_aan)
        elif self.stand == 4:
            self.c.write_single_register(self.adress, self.gedoofd)

    def afsluiten(self):
        while 1:
            time2 = time.time() - self.time1
            if time2 < 3:
                self.setStand("geel_knipperen")
            elif 6 > time2 > 3:
                self.setStand("geel")
            elif time2 > 6:
                self.setStand("rood")
                break


    def normaal(self):
        while 1:
            time2 = time.time() - self.time1
            if time2 < 3:
                self.setStand(2) #rood
            elif 13 > time2 > 3:
                self.setStand(0) #groen
            elif time2 > 13:
                self.setStand(4)
                break


    def checkError(self):
        if (self.c.close() ):
            beschikbaar = 0
        elif (self.c.open()):
            beschikbaar = 1


