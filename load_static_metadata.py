#! /usr/bin/env python3

import pprint
import os.path
import sys
import re
import pickle
import string

DOMAIN_TABLES_WANTED = [
    'birth_cohort', 'deprivation_index_eng', 'employment_sector',
    'employment_status', 'living_arrangement', 'marital_status',
    'occupation_1990', 'occupation_2010', 'region'
]

class StaticMetadataLoader(object):
    def run(self, args):
        index = pickle.load(open('index.pkl', 'rb'))

        possible_values_index = {}

        for key, item in index.items():
            for field, value in item.items():
                possible_values_index.setdefault(field, set()).add(value)


        for table in DOMAIN_TABLES_WANTED:
            values = possible_values_index[table]
            
            i = 1
            for value in values:
                # we represent blank cells as NULLs
                if value is None: continue
                print("INSERT INTO %s VALUES (%d, '%s');" % (table, i, value))
                i += 1



if __name__ == '__main__':
    obj = StaticMetadataLoader()
    obj.run(sys.argv[1:])
    
