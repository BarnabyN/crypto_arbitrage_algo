import pandas as pd
import numpy as np
from math import log, e

rates = pd.DataFrame({
	'B':['XBT', 'USD', 'XET'],
	'S':['USD', 'XET', 'XBT'],
	'X':[48000, 1/1750, 1750/48000]
})

print(abs(1-e**(sum([log(i) for rate in rates['X']]))))
