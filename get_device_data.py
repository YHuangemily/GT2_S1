import time
import socket                
import logging

logger = logging.getLogger(__name__)

class DistanceSensor:
    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port
        self.s = socket.socket()          
        self.s.connect((self.host, self.port)) 
        logger.info('Connect to the device successfully.')

    def get_distance_value(self, sensor_index):
        """
        Get the distance value from the device.
        
        The index of the device start from 0
        """
        self.s.settimeout(1000)
        self.s.send(b'M0\r\n')
        message = self.s.recv(1024).decode('utf-8')
        message = message.split(",")
        if message[0] == "ER":
            raise SensorError(message)
        else:
            if sensor_index < len(message) - 1:
                distance=int(message[sensor_index + 1])
                return distance/10000
            else:
                raise SensorError("The device you are attempting to access does not exist")

    def disconnect_sensor(self):
        self.s.close()       

class SensorError(Exception):
    pass

if __name__ == "__main__":
    host="172.20.1.10"
    port=64000
    device_index=0
    dis= DistanceSensor(host,port)
    while(1):
        print('current disstance {} mm'.format(dis.get_distance_value(device_index)))
        time.sleep(1)
