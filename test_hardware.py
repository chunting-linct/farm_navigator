from gpiozero import DigitalOutputDevice
import sys

from time import sleep

ain1_1 = 26
ain2_1 = 21
stby_1 = 20
bin1_1 = 19
bin2_1 = 13
pwmb_1 = 12
pwma_1 = 5


if __name__ == '__main__':
    if sys.argv[2] == 1:
        DigitalOutputDevice(sys.argv[1]).on()
    elif sys.argv[2] == 0:
        DigitalOutputDevice(sys.argv[1]).off()
