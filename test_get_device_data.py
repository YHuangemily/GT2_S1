import time
import socket
import logging
import pytest
import os

logger = logging.getLogger(__name__)

class TestDistanceSensor:

    def test_get_distance_value(self, ip, port, index):
        """
        Get the distance value from the device.
        Parameters
        -----
        ip
            IP of the device (172.20.1.10)
        port
            port of the device (64000)
        index
            index of the sensor, which starts from 0
        -----
        """
        self.host = "{}".format(ip)
        self.port = int(port)
        self.socket = socket.socket()
        self.index=int(index)

        self.socket.connect((self.host, self.port))
        logger.info('Connect to the device successfully.')

        self.socket.settimeout(1000)
        self.socket.send(b'M0\r\n')
        message = self.socket.recv(1024).decode('utf-8')
        message = message.split(",")
        if message[0] == "ER":
            raise SensorError(message)
        else:
            if self.index < len(message) - 1:
                distance =int(message[self.index + 1])/10000
                logger.info('current distance {} mm'.format(distance))
            else:
                raise SensorError("The device you are attempting to access does not exist")


class SensorError(Exception):
    pass
