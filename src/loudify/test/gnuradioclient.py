"""
Majordomo Protocol client example. Uses the mdcli API to hide all MDP aspects

Author : Min RK <benjaminrk@gmail.com>

"""
import sys

import numpy
from mdcliapi2 import MajorDomoClient


def main():
    verbose = '-v' in sys.argv
    client = MajorDomoClient("tcp://localhost:5555", verbose)
    # number of request
    requests = 50
    # for now open dump file to really test with "live" gnuradio data
    f = numpy.fromfile(open("test_frame.txt"), dtype=numpy.complex64)

    for i in range(requests):
        try:
            client.send(b"echo", f)
        except KeyboardInterrupt:
            print("send interrupted, aborting")
            return

    count = 0
    while count < requests:
        try:
            reply = client.recv()
        except KeyboardInterrupt:
            break
        else:
            # also break on failure to reply:
            if reply is None:
                break
        count += 1
    print("%i requests/replies processed" % count)


if __name__ == '__main__':
    main()
