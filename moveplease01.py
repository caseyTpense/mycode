#!/usr/bin/env python3

#import utilities
import shutil
import os


def main()
    """called when ran"""
    os.chdir('/home/student/mycode/')  #move into this working directory
    shutil.move('raynor.obj', 'ceph_storage/') # attempts to move raynor.ob to ceph storage/ dir

    #program pauses and asks for input
    xname = input('What is the new name for kerrigan.obj? ') # collects input on what to name the file

    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname) # moves kerrigan.obj to ceph_storage/ with the new name from input


main() #calls the function




