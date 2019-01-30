#  Installing, importing, using modules

#  importing modules

import numpy as np
from pyfiglet import Figlet

# using modules

a = np.array([[1,2,3], [4,5,7], [11,12,13]])
var = np.var(a)
print(var)

# read the docs!
f = Figlet(font='big')
print(f.renderText('Python is cool!'))
