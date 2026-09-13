from gpiozero import DigitalOutputDevice

from time import sleep

ain1_1 = DigitalOutputDevice(26)
ain2_1 = DigitalOutputDevice(21)
stby_1 = DigitalOutputDevice(20)
bin1_1 = DigitalOutputDevice(19)
bin2_1 = DigitalOutputDevice(13)
pwmb_1 = DigitalOutputDevice(12)
pwma_1 = DigitalOutputDevice(5)

stby_1.on()
pwma_1.on()
ain1_1.on()
ain2_1.off()
sleep(2)
stby_1.off()
pwma_1.off()
ain1_1.off()
ain2_1.off()
