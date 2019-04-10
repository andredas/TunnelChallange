import time

#from phue import Bridge
#
#b = Bridge('192.168.0.45')
# b.connect()
# b.get_api()


#def all_on():
#         b.set_light([8,13,2,15,4],'on', True)
#
#
# def all_off():
#         b.set_light([8,13,2,15,4],'on', False)
#
#
# def all_brightness(brightness):
#         b.set_light([8,13,2,15,4], 'bri', brightness)
#
#
# def set_brightness(lamp, bright):
#         b.set_light(lamp, 'bri', bright)

# def set_on(lamp):
#         b.set_light(lamp, 'on', True)

# def set_off(lamp):
#         b.set_light(lamp, 'on', False)

#def get_info(lamp, typeI):
#    stringInfo = "'" + typeI + "'"
#    info = b.get_light(lamp, ("'", typeI, "'"))
#   return info

def set_status(status):
#         all_on()
        if(status == "0"):
#                 b.set_light([8,13,2,15,4], 'bri', 0)
#
#         elif(status == "1"):
#                 b.set_light([8,4], 'bri', 255)
#                 b.set_light([13,15], 'bri', 125)
#                 b.set_light(2, 'bri', 0)
#
#         elif(status == "2"):
#                 b.set_light([8,13,2,15,4], 'bri', 255)
            return 1

        else:
            return 0