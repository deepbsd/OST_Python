#!/usr/local/bin/python3
#
#    File Type Lister (FileTypeLister.py)
#       by David S. Jackson
#         on Jan 16, 2015
#       for OST Python 2
#     Instructor Pat Barton
#
"""This program lists all files in designated directory
by file extension and records the number of occurances
for each file type.  Files without a suffix are designated 
as part of the category 'None'.
"""
import os
import glob


#dirpath = "/home/dsj/tmp/tmp*tempdir"
dirpath = "/home/dsj/bin"

def listFiles(wkdir):
    """This function returns a dictionary of number of files 
    in dir by type of suffix.
    """
    suf_dict = {}
    files = glob.glob(os.path.join(wkdir, "*"))
    
    for f in files:
        if not os.path.isfile(f):
            files.remove(f)
    
    for f in files:
        f = os.path.basename(f)
        name, ext = os.path.splitext(f)
        if ext not in suf_dict.keys():
            suf_dict[ext] = 1
        else:
            suf_dict[ext] = suf_dict[ext] + 1
    return suf_dict


def printFiles(suf_dict):
    """ Prints files by type and totals them """
    print("\nFiles by type in {}".format(dirpath))
    print("\nSuffix\t\t\tOccurances")
    print("="*40+"\n")
    for ext, values in sorted(suf_dict.items()):
        if ext == '':
            ext = 'None'
        print("{}\t\t\t{}".format(ext, values))
    


if __name__ == "__main__":
    #listFiles(dirpath)
    printFiles(listFiles(dirpath))

