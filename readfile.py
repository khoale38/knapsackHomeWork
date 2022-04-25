from ctypes import sizeof
import numpy as np
filename = "R01000/s000.kp"

data = np.loadtxt(filename, dtype=int,skiprows=3)

amount=np.loadtxt(filename, dtype='str',delimiter='\n')

values = [
       
    ]
weights = [[
       
    ]]
for each in data:
        values.append(each[1])
        [weights].append(each[0])

print(len(values))
print(len(weights))

