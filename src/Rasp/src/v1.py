import serial
import serial.tools.list_ports
import time
import requests


def get_serial_port():
    for i in serial.tools.list_ports.comports():
        p = str(i)
        if 'USB' in p:
            sp = p.split(' - ')
            return (sp[0])

try:
    ser = serial.Serial()
    ser.baudrate = 115200
    ser.port = get_serial_port()

    ser.open()

    print(ser.is_open)
    # for i in range(50):
    while 1:
        try:
            line = str(ser.readline())
            # print(line)
            if '--' in line:
                sp = line.split('--')
                hr = sp[1]
                tmp = sp[2]
                ecg = sp[3]
                print(f'Heart Rate: {hr}\t Body T: {tmp}\tECG: {ecg}')
                url = f'http://54.166.105.47:9999/update_live/?heart_rate={hr}&body_temp={tmp}&ecg={ecg}'
                r = requests.get(url = url)
                print(r)
            else:
                print(line)
        except KeyboardInterrupt:
            break
        except:
            print('Ser Err')
except KeyboardInterrupt:
    print('Closing Serial Port')
    ser.close()
finally:
    print('Closing Serial Port')
    ser.close()
