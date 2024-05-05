# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:26:01 2023

@author: 21091A05H9

Automorphic : A number whose square ends in the same digits as in the number itself


Trimorphic : A number whose cube ends in the same digits as in the number itself


Anagram : letters of one string can be rearranged to form the other string
"""

isAutomorphic = lambda n:str(n*n).endswith(str(n))
isTrimorphic = lambda n:str(n**3).endswith(str(n))
isAnagram = lambda n1,n2:set(n1) == set(n2)