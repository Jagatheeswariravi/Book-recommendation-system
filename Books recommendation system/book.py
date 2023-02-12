# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 16:03:02 2022

@author: jagar
"""
import numpy as np
import pandas as pd

import streamlit as st
import pickle
pt= pickle.load(open('pt.pkl','rb'))

books= pickle.load(open('books.pkl','rb'))


similarity_matrix = pickle.load(open('similarity_matrix.pkl','rb'))

bookname = st.text_area("enter the book name")

def recommend(bookname):
    index = np.where(pt.index == bookname)[0]
    result = sorted(list(enumerate(similarity_matrix[index])),key =lambda x:x[1],reverse = True)[1:6]
    data = []
    for i in result:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    
    return data
        
favorite = recommend(bookname)

for i in favorite:
    for j in i:
        st.title(j)
    