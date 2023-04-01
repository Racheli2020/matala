# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 00:10:39 2023

@author: rache
"""

def revword(fhand:str):
            fhand = fhand.lower()[::-1]
            return fhand


def countword():
    fhand = open("text.txt","r")
    count1 = 1
    for w in fhand:
        words = w.split(" ")
        if len(words)==1:
            first = words[0].lower().strip()
        else:
            for i in words :
                word = revword(i).strip()
                if word == first:
                    count1 += 1
    print(count1)
countword()       
    
    
    
