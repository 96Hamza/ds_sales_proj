# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 00:23:31 2023

@author: Humza
"""

import pandas as pd

data =pd.read_csv(r"C:\Users\Humza\Documents\ds_sales_proj\amazon.csv")

#print(data.head())

# Analisis Kategori Produk
category_counts = data['category'].value_counts()
print(category_counts)

data.columns
data.info()
data.describe()