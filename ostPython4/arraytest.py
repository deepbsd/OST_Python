#!/usr/bin/python3

def __str__(self):
    '''
    '''
    ret = ''
    for row in range(self._rows):
        for col in range(self._cols):
            for depth in range(self._depth):
                print(row, col, depth)
                ret += '{}'.format(self[row,col,depth])
            ret += '\n'
        ret += '\n'
    return ret
