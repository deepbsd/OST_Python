#!/usr/bin/env python3



import struct
from datetime import datetime, timedelta
from time import ctime

file_dict = {}
packet_dict = {}
packetlog = open('wireshark.bin', 'rb')


def end():
    packetlog.close()


def read_header():
    for name, len, format in FILEHEADER:
        bindata = packetlog.read(len)
        file_dict[name] = struct.unpack(format, bindata)


def read_packet():
    for name, len, format in PACKETHEADER:
        bindata = packetlog.read(len)
        packet_dict[name] = struct.unpack(format, bindata)
            

    unix_date = datetime.fromtimestamp(packet_dict['ts_sec'][0])
    micro_delta = timedelta(microseconds=packet_dict['ts_usec'][0])
    unix_date += micro_delta
    return unix_date


def read_contents():
    packetlog.seek(24)
    while True:
        print(read_packet())
        packetlog.seek(packet_dict['incl_len'][0], 1) 


FILEHEADER = (
        ('magic_number', 4, '<L'),
        # int is the same length as long
        ('minor_version_number', 4, '<I'),
        ('major_version_number', 4, '<I'),
        ('GMT', 4, '!l'),
        ('time_stamp_sigfig', 4, '<L'),
        ('max_packet_length', 4, '<L'),
        ('data_link_type', 4, '<L'))

PACKETHEADER = (('ts_sec', 4, '<L'),
        ('ts_usec', 4, '<L'),
        ('incl_len', 4, '<L'),
        ('orig_len', 4, '<L'))

try:
    read_contents()
except struct.error:
    print('End of File')

end()


