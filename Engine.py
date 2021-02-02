import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
import math
import pickle
import json
import random

class RecommendationEngine :
    knlg_base_filename = 'Knowledge-Base.xls'
    dataset_filename = 'Menu-Items.xls'
    recommendation_name = 'menu-items'
    
    def __init__(self, ctgID, n):
        self.ctgID = ctgID
        self.n = n

    def set_Dataset_Filename(self, file):
        self.dataset_filename = file

    #Method to get the association rule from the knowledge base
    def getSuffixIDs(self, prefix):
        df = pd.read_excel(self.knlg_base_filename)
        pre = df['prefix']
        for i in range (len(pre)):
            if pre[i] == prefix :
                return [df['suffix1'][i], df['suffix2'][i], df['suffix3'][i]]
         
    #Method to randomly pick items from each category
    def getItems(self, IDs, combined):
        items = []
        for i in range (len(combined[1])):
            if combined[0][i] in IDs :
                items.append([combined[1][i] , combined[2][i] , combined[3][i] ])
        random.shuffle(items)
        picked = items[:self.n]
        return picked
        
    def run (self):
        suffix = self.getSuffixIDs(self.ctgID)
        '''
        # loading the data into lists
        df = pd.read_excel(self.dataset_filename)
        
        ids = df['id']
        ctgIDs = df['ctg_id']
        names = df['name']
        prices = df['price']
        combined = [ctgIDs , ids, names, prices]
        with open('saved-items.pkl', 'wb') as f:
            pickle.dump(combined, f) 
        '''
        with open('saved-items.pkl', 'rb') as f:
            combined = pickle.load(f)
        
        #Get the top nearest N items
        items = self.getItems(suffix, combined)
        '''
        #Not working
        jsonData =  {
            'type' : self.recommendation_name,
            'data' : items
        }
        jsonStr = json.dumps(jsonData)
        '''
        print (items)