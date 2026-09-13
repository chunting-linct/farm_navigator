from gpiozero import DigitalOutputDevice

from time import sleep

driver_1 = {
    "ain1" : DigitalOutputDevice(26),
    "ain2" : DigitalOutputDevice(21),
    "stby" : DigitalOutputDevice(20),
    "bin1" : DigitalOutputDevice(19),
    "bin2" : DigitalOutputDevice(13),
    "pwmb" :DigitalOutputDevice(12),
    "pwma" : DigitalOutputDevice(5)
}

driver_2 = {
    "ain1" : DigitalOutputDevice(22),
    "ain2" : DigitalOutputDevice(27),
    "stby" : DigitalOutputDevice(17),
    "bin1" : DigitalOutputDevice(18),
    "bin2" : DigitalOutputDevice(23),
    "pwmb" :DigitalOutputDevice(24),
    "pwma" : DigitalOutputDevice(4)
}


def a_1_foward(driver):
    driver["stby"].on()
    driver["pwma"].on()
    driver["ain1"].on()
    driver["ain2"].off()
    sleep(2)
    for pin in driver:
        driver[pin].off()
def a_1_backward(driver):
    driver["stby"].on()
    driver["pwma"].on()
    driver["ain1"].off()
    driver["ain2"].on()
    sleep(2)
    for pin in driver:
        driver[pin].off()

def b_1_foward(driver):
    driver["stby"].on()
    driver["pwmb"].on()
    driver["bin1"].on()
    driver["bin2"].off()
    sleep(2)
    for pin in driver:
        driver[pin].off()

def b_1_backward(driver):
    driver["stby"].on()
    driver["pwmb"].on()
    driver["bin1"].off()
    driver["bin2"].on()
    sleep(2)
    for pin in driver:
        driver[pin].off()



if __name__ == '__main__':
    a_1_foward(driver_1)
    a_1_backward(driver_1)
    b_1_foward(driver_1)
    b_1_backward(driver_1)
    a_1_foward(driver_2)
    a_1_backward(driver_2)
    b_1_foward(driver_2)
    b_1_backward(driver_2)
