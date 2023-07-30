# this tests numpy array simplification using VW
# 216804 --> 3061 points (98.5% reduction)
# 300ms per RDP operation on MBA Core i7

import json
import numpy as np
from pybind11_rdp import _rdp

with open("test/coords_complex.json", "r") as f:
    coords = np.array(json.load(f))
for x in range(50):
    _rdp(coords, epsilon=0.01)
