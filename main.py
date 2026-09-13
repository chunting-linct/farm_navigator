from gpiozero import DigitalOutputDevice

from time import sleep

ain1_1 = DigitalOutputDevice(26)
ain2_1 = DigitalOutputDevice(21)
stby_1 = DigitalOutputDevice(20)
bin1_1 = DigitalOutputDevice(19)
bin2_1 = DigitalOutputDevice(13)
pwmb_1 = DigitalOutputDevice(12)
pwma_1 = DigitalOutputDevice(5)

def a_1_foward():
    stby_1.on()
    pwma_1.on()
    ain1_1.on()
    ain2_1.off()
    sleep(2)
    stby_1.off()
    pwma_1.off()
    ain1_1.off()
    ain2_1.off()
def a_1_backward():
    stby_1.on()
    pwma_1.on()
    ain1_1.off()
    ain2_1.on()
    sleep(2)
    stby_1.off()
    pwma_1.off()
    ain1_1.off()
    ain2_1.off()


def b_1_foward():
    stby_1.on()
    pwmb_1.on()
    bin1_1.on()
    bin2_1.off()
    sleep(2)
    stby_1.off()
    pwmb_1.off()
    bin1_1.off()
    bin2_1.off()
def b_1_backward():
    stby_1.on()
    pwmb_1.on()
    bin1_1.off()
    bin2_1.on()
    sleep(2)
    stby_1.off()
    pwmb_1.off()
    bin1_1.off()
    bin2_1.off()



if __name__ == '__main__':
    a_1_foward()
    a_1_backward()
    b_1_foward()
    b_1_backward()
