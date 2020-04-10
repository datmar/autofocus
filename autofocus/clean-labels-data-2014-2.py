#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import glob
import matplotlib.pyplot as plt
import pathlib

file = pathlib.Path("../data/lpz_2012-2014/lpz_2012-2014/raw/labels_clean.csv") # TODO: replace with absolute path
if not file.exists ():
    print('file doesnt exist')
    df_17 = pd.read_csv('../data/lpz_2016_2017/processed/labels.csv')
    df_14 = pd.read_csv('../data/lpz_2012-2014/lpz_2012-2014/raw/labels.csv')

    # Lowercase feature names
    df_14.Species = df_14.Species.apply(lambda x: x.lower())

    # Replace bird species with 'bird'
    labels_replacement_birds = ['house sparrow', 'eurasian collared-dove', 'crow', 'starling', 
                          'yellow-rumped warbler', 'chipping sparrow', 'great horned owl',
                          'american woodcock', 'northern flicker', 'downy woodpecker',
                          'white-throated sparrow', 'great blue heron', 'grackle',
                          "swainson's thrush", 'gray catbird', 'red-tailed hawk',
                          'cardinal', 'hermit thrush', 'american robin',
                          'red winged blackbird', 'pigeon', 'sparrow', 'ring-billed gull',
                          'mallard', 'mourning dove', 'red-winged blackbird',
                          'eurasian collared dove', 'white-crowned sparrow', 'hairy woodpecker',
                          'red winged black bird', 'blue jay', 'song sparrow', 'robin',
                          'brown thrasher'
                               ]
    df_14_clean = df_14.replace(to_replace=labels_replacement_birds, value='bird')

    # Replace 2014 labels to match 2017 df where possible
    replace_map = {'dom dog': 'dog', 'mower': 'lawn mower', 'skunk': 'striped skunk',
                   'coyote ': 'coyote', 'opossum': 'v. opossum', 'deer': 'w. t. deer'}
    df_14_clean = df_14_clean.replace(replace_map)
    df_14_clean = df_14_clean.replace(to_replace=['domestic cat', 'dom cat'], value='cat')

    # Remove unused labels from df_14
    labels_unused = ['bike', 'canada goose', 'not visible', 'duck', '1', 'other vehicle',
                     'car', 'tractor', 'livestock', 'rabbit', 'truck', '`', '10']
    df_14_clean = df_14_clean[~df_14_clean['Species'].isin(labels_unused)]

    # Change label column name
    df_14_clean.rename(columns={'Species': 'label'}, inplace=True)

    df_14_clean.to_csv('../data/lpz_2012-2014/lpz_2012-2014/raw/labels_clean.csv')
else:
    df_14_clean = pd.read_csv('../data/lpz_2012-2014/lpz_2012-2014/raw/labels_clean.csv')

