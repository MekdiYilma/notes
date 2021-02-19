
A = [ [ 2, 4], [ 1, 7], [-1, 8] ]

B = [ [3, 2, -5, 6],  [1, -3, 4, 8] ]

result = [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A   ]


for r in result:
   print(r)

# for A_row in zip(A):
#     print(A_row)
# print()
# for B_col in zip(*B):
#     print(B_col)
# print()
 
# A_row = [A_row for A_row in A]
# B_col = [B_col for B_col in zip(*B)]
# [sum(a*b for a, b in zip(A_row, B_col))]
  


# result = []

# for A_row in A:
#     for B_col in zip(*B):
#         for a, b in zip(A_row, B_col):
            # print(a,b)

# print(result)


import numpy as np
import pandas as pd


class ElonTweet():
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.raw = pd.read_csv(self.file_path)
    
    def cleaning(self):
        text_col = self.raw.loc[:,'text']
        punc = '?,.<>";:[]}{-!@$%^&*()+=-_`/'
        
        def rm_punc(x):
            return ''.join([char for char in x.lower() if char not in punc])
        
        self.cleanedtweets = text_col.apply(rm_punc)

if __name__ == '__main__':
    filepath = 'filepathhere'
    tw = ElonTweet(file_path)
    raw_tweet = tw.raw
    tw.cleaning()
    clean_tweet = tw.cleanedtweets



    