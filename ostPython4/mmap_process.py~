#!/usr/bin/env python3

import os
import time
import mmap

f = open('test.out', 'r')
m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
buffer_size = 64
retract_size = -32
start_time = time.time()

while True:
    m.seek(buffer_size, os.SEEK_CUR)
    # Process some data starting at the current position
    pass
    m.seek(retract_size, os.SEEK_CUR)
    # Process some data starting at the current position
    pass
    if m.tell() > 1024 * 1024 * 10:
        break
end_time = time.time()
m.close()
f.close()
print('mmap time elapsed: {}'.format(end_time - start_time))


