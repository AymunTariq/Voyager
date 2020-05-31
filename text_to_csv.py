# -*- coding: utf-8 -*-
"""
Created on Wed May 13 10:25:25 2020

@author: AymunTariq
"""

import pandas as pd

df = pd.read_csv("abc.txt",delimiter=';')
df.to_csv('Demo1.csv')