#Program to set temeperature sensor using I2C communication and set min/max temperature to take action
# Follow thse two git repositories for testing, module needed for testing
#https://github.com/RolfBly/DS1621
#https://github.com/cpb-/Article-RPi-DS1621

# This below program is taken from RPi article and seems very basic code

import smbus

bus = smbus.SMBus(1)
addr= 0x48

START_CONVERT=0xEE
ACCESS_CONFIG=0xAC
READ_TEMPERATURE=0xAA

bus.write_byte_data(addr, ACCESS_CONFIG, bus.read_byte_data(addr, ACCESS_CONFIG)| 0x01)


# Demarrer l'acquisition
bus.write_byte(addr, START_CONVERT)
while (bus.read_byte_data(addr, ACCESS_CONFIG) & 0x80) == 0:
    pass

v=bus.read_byte_data(addr, READ_TEMPERATURE)
if v > 127:
    v -= 256
print v
