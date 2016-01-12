#!/usr/bin/env python3

import os
import time

f = open('test.out', 'r')
buffer_size = 64
retract_size = -32
start_time = time.time()

while True:
    f.seek(buffer_size, os.SEEK_CUR)
    # Process some data starting at the current position
    pass
    f.seek(retract_size, os.SEEK_CUR)
    # Process some data starting at the current position
    pass
    if f.tell() > 1024 * 1024 * 10:
        break
end_time = time.time()
f.close()
print('Normal time elapsed: {}'.format(end_time - time_start))


