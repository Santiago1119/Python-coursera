# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


serie = pd.Series(np.random.normal(100, 20, 100))

print(serie)
print(serie.sort_values())