#!/usr/bin/env python3

import sys

print ( "Testing your installation ... " )
try:
    import torch
except:
    print ( "cannot import torch. install it (try e.g. pip3 install --user torch, or consult http://pytorch.org)" )
    sys.exit()

#if not "0.4.1" in torch.__version__:
#    print ( "this is torch version %s. we need torch version: 0.4.1. update! (try e.g. pip3 install --user --upgrade torch, or consult http://pytorch.org)" % torch.__version__ )
#    sys.exit()

try:
    import torchvision
except:
    print ( "cannot import torchvision. install it (try e.g. pip3 install --user torchvision" )
    sys.exit()

#if not "0.2.1" in torchvision.__version__:
#    print ( "this is torchvision version %s. we need torchvision version: 0.2.1. update! (try e.g. pip3 install --user torchvision==0.2.1" % torchvision.__version__ )
#    sys.exit()

try:
    import matplotlib
except:
    print ( "cannot import matplotlib. install it (try e.g. pip3 install --user matplotlib" )
    sys.exit()

print ( "Installation seems to be ok. Have fun with the exercises!" )
