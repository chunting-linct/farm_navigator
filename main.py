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


def a_foward(driver: dict[str, DigitalOutputDevice]):
    driver["stby"].on()
    driver["pwma"].on()
    driver["ain1"].on()
    driver["ain2"].off()
def a_backward(driver: dict[str, DigitalOutputDevice]):
    driver["stby"].on()
    driver["pwma"].on()
    driver["ain1"].off()
    driver["ain2"].on()

def b_forward(driver: dict[str, DigitalOutputDevice]):
    driver["stby"].on()
    driver["pwmb"].on()
    driver["bin1"].on()
    driver["bin2"].off()

def b_backward(driver: dict[str, DigitalOutputDevice]):
    driver["stby"].on()
    driver["pwmb"].on()
    driver["bin1"].off()
    driver["bin2"].on()
def stop(driver : dict[str, DigitalOutputDevice]):
    for key in driver:
        driver[key].off()

def all_forward():
    a_foward(driver_1)
    a_foward(driver_2)
    b_forward(driver_1)
    b_forward(driver_2)
    sleep(2)
    stop(driver_1)
    stop(driver_2)

def all_backward():
    a_backward(driver_1)
    a_backward(driver_2)
    b_backward(driver_1)
    b_backward(driver_2)
    sleep(2)
    stop(driver_1)
    stop(driver_2)
def one_side_forward():
    a_foward(driver_1)
    b_forward(driver_1)
    sleep(2)
    stop(driver_1)

def turn():
    a_foward(driver_1)
    b_forward(driver_1)
    a_backward(driver_2)
    b_backward(driver_2)
    sleep(2)
    stop(driver_1)
    stop(driver_2)

if __name__ == '__main__':
    all_forward()
    all_backward()
    one_side_forward()
    turn()
