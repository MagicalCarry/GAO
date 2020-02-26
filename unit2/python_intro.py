import os
import numpy as np
path = "C:/Users/Administrator/Desktop/git/ghy/SES2020spring/unit2/readme.md"
if os.path.isfile(path):
    f = open(path, 'r')
    data = f.read()
    print(len(data.split()))
    f.close()
