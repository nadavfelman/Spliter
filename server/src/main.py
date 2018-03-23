"""
TODO:
    - finish implementing the protocol
    - finish run in client_thread
"""


import random
import socket
import sys
import threading

import dataSets
import time

LISTEN_AMOUNT = 20
GAMEBOARD_WIDTH = 9600
GAMEBOARD_HEIGHT = 5400

threads = []
dataBase = dataSets.dataBase()
traffic = {}
traffic_lock = threading.Lock()


def main():
    """[summary]

    Raises:
        IndexError -- [description]
        ValueError -- [description]
        ValueError -- [description]
        ValueError -- [description]
    """

    args = sys.argv[1:]

    if len(args) < 2:
        raise IndexError('Not enough parameters given')

    ip, port = args[0], args[1]

    if len(ip.split('.')) != 4:
        raise ValueError(
            'IP argument "{}" must be IPv4 format "XXXX.XXXX.XXXX.XXXX"'.format(ip))

    DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    if not all([c in DIGITS for c in port]):
        raise ValueError('Port argument "{}" has to be a number'.format(port))

    port = int(port)
    if not 0 < port < 65536:
        raise ValueError(
            'Port argument "{}" has to be in range of 0 to 65536'.format(port))

    server_socket = socket.socket()
    server_socket.bind((ip, port))
    server_socket.listen(LISTEN_AMOUNT)

    while True:
        client_socket, client_address = server_socket.accept()
        id_ = socket_id(client_socket)

        thread = client_thread(client_socket, client_address, id_)
        thread.start()

        threads.append(thread)


def socket_id(socket_):
    return id(socket_)

def orb_id(orb_):
    return id(orb_)

class client_thread(threading.Thread):
    """
    [summary]
    """

    def __init__(self, socket_, address, id_):
        """[summary]

        Arguments:
            socket_ {[type]} -- [description]
            address {[type]} -- [description]
            id_ {[type]} -- [description]
        """

        super(client_thread, self).__init__()
        self.socket_ = socket_
        self.address = address
        self.id_ = id_

    def run(self):
        # run start of protocol
        # do begining of connection

        self.receiver = receiving_thread(self.socket_, self.address, self.id_)
        self.receiver.start()
        self.sender = sending_thread(self.socket_, self.address, self.id_)
        self.sender.start()

        self.receiver.join()
        self.sender.join()


class receiving_thread(threading.Thread):
    """
    [summary]
    """

    def __init__(self, socket_, address, id_):
        """[summary]

        Arguments:
            socket_ {[type]} -- [description]
            address {[type]} -- [description]
            id_ {[type]} -- [description]
        """

        super(receiving_thread, self).__init__()
        self.socket_ = socket_
        self.address = address
        self.id_ = id_

    def run(self):
        while True:
            # recive data
            # change server data
            pass

class sending_thread(threading.Thread):
    """
    [summary]
    """

    def __init__(self, socket_, address, id_):
        """[summary]

        Arguments:
            socket_ {[type]} -- [description]
            address {[type]} -- [description]
            id_ {[type]} -- [description]
        """

        super(sending_thread, self).__init__()
        self.socket_ = socket_
        self.address = address
        self.id_ = id_
    
    def run(self):
        while True:
            # send data
            pass

class game_manipulator(threading.Thread):
    """
    [summary]
    """

    PAUSE_DURATION = 0.001

    def __init__(self, dataBase):
        super(game_manipulator, self).__init__()
        self.dataBase = dataBase

    def start(self):
        while True:
            self.add_orb()

            time.sleep(game_manipulator.PAUSE_DURATION)
    
    def add_orb(self):
        orb_x = random.randint(0, GAMEBOARD_WIDTH)
        orb_y = random.randint(0, GAMEBOARD_HEIGHT)
        orb_mass = random.randint(orb.MIN_MASS, orb.MAX_MASS)
        orb_color = random.choice(orb.orb_colors)
        orb_ = orb.orb(orb_x, orb_y, orb_mass, orb_color)

        id_ = orb_id(orb_)

        dataBase.add_orb(id_, orb_)

        # add to all traffics

if __name__ == '__main__':
    main()
