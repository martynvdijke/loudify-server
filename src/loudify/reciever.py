import time

import numpy as np
import zmq


def zmq_recieve(_REQ_ADDR, _logger):
    """
    Returns:
        object: 

    """

    context = zmq.Context()
    reciever = context.socket(zmq.PULL)
    reciever.connect(_REQ_ADDR)
    _logger.debug("Ready to recieve packets")
    while True:
        buff = reciever.recv()
        print(time.time())
        data = np.frombuffer(buff, dtype="float32")
        data = data[0::2] + 1j * data[1::2]
        print(type(data))
        print(len(data))
