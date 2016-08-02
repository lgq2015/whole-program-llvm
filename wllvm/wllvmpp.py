#!/usr/bin/env python
"""This is a wrapper around the real compiler.  

It first invokes a real compiler to generate an object file.  Then it
invokes a bitcode compiler to generate a parallel bitcode file.  It
records the location of the bitcode in an ELF section of the object
file so that it can be found later after all of the objects are linked
into a library or executable.
"""

import sys

from utils import *
import logconfig

def main():
    cmd = list(sys.argv)
    cmd = cmd[1:]

    builder = getBuilder(cmd, True)
    buildObject(builder)
    if not os.environ.get('WLLVM_CONFIGURE_ONLY', False):
        buildAndAttachBitcode(builder)


    
if __name__ == '__main__':
    sys.exit(main())
        
