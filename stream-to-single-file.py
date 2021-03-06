#!/usr/bin/env python3

"""
Modified version of acq400_stream.py

python stream-to-single-file.py --verbose=1 --runtime=5 <module ip or name>

"""


import acq400_hapi
import numpy as np
import os
import time
import argparse
import socket
import sys
import shutil
from builtins import input


def run_stream(args):
    uut = acq400_hapi.Acq400(args.uuts[0])
    data_len_so_far = 0
    RXBUF_LEN = 4096
    cycle = 1

    port = acq400_hapi.AcqPorts.STREAM # use the streaming port (4210)

    skt = socket.socket()
    skt.connect((args.uuts[0], port))
    start_time = time.time()
    data_length = 0

    data_file=open(args.file, "wb")

    while time.time() < (start_time + args.runtime):

        data = skt.recv(RXBUF_LEN)

        data_length += len(data)
        data_len_so_far += len(data)

        data_file.write(data)

        if args.verbose == 1:
            print("New data file written.")
            print("Data Transferred: ", data_len_so_far, "KB")
            print("Streaming time remaining: ", -1 * (time.time() - (start_time + args.runtime)))
            print("\n" * 2)


def run_main():
    parser=argparse.ArgumentParser(description='stream to single file')
    parser.add_argument('--runtime',default=100,type=int,help="How long to stream data (s)")
    parser.add_argument('--file',default='run00001.dtq',type=str,help="filename")
    parser.add_argument('--verbose',default=0,type=int,help='Prints status messages as the stream is running')
    parser.add_argument('uuts', nargs='+', help="uuts")
    run_stream(parser.parse_args())


if __name__ == '__main__':
    run_main()
