import os
import sys
import argparse

def runRouting():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-p', '--path')
    parser.add_argument ('-ph', '--phone')
    parser.add_argument ('-d', '--database', nargs='?', choices=[0, 1], type=int)
    parser.add_argument ('-s', '--stage', choices=[1, 2], type=int)

    namespace = parser.parse_args(sys.argv[1:])
    return namespace

def removeFileByPath(path):
    os.remove(path)
