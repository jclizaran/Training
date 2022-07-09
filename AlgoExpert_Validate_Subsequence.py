# -*- coding: utf-8 -*-
"""
Created on Sat Jul  9 11:04:44 2022

@author: jclizaran
"""

#array = [5,1,22,25,6, -1, 8, 10]
#sequence = [1,6,-1,10]



def isValidSubsequence(array, sequence):
    # Write your code here.
    
    def get_array_clean(array,sequence):
        ## Function to generate a new array from array list, with the elements that also are in sequence list
        array_clean = []
        for i in array:
            if i in sequence:
                array_clean.append(i)
        return array_clean
    
    def find_sequence(array_clean,sequence):
        
        i=0
        found = False
        
        while found == False and (i + len(sequence) <= len(array_clean)):
            if array_clean[i:i+len(sequence)] == sequence:
                found = True
            i = i+1
        
        return found
    
    array_clean = get_array_clean(array,sequence)
    return find_sequence(array_clean,sequence)

# isValidSubsequence(array, sequence)

         
    pass