#! /usr/bin/env python

import os

CMD = "python"
DIR_HW = "src"
DIR_CHECK = "../../tools"
THIS_DIR = os.path.basename(os.getcwd())

def main():
    os.system(f"{CMD} {DIR_CHECK}/chk_{THIS_DIR}.py")

if __name__ == "__main__":
    main()
