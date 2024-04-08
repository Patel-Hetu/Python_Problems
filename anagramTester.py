#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 20:13:21 2022

@author: saachigupta
"""

import unittest

def anagramTester(string1, string2):
    '''
    Assume that the two parameters are strings.
    Return True if string1 and string2 are anagrams of each other,
    and False if not.
    Reminder, a word a is an anagram of another word b if a's letters 
    can be rearanged to write b.
    '''
    word = ""
    for i in string1:
        if i in string2:
            word +=i
        
    return word == string1
    
  
class anagramTests(unittest.TestCase):
    def test1(self):
        self.assertEqual(anagramTester('listen','silent'), True)
    def test2(self):
        self.assertEqual(anagramTester('listen','silence'), False)
    def test3(self):
        self.assertEqual(anagramTester('evil','vile'), True)
    def test4(self):
        self.assertEqual(anagramTester('a gentleman','elegant man'), True)
    def test5(self):
        self.assertEqual(anagramTester('this really','shouldn\'t work'), False)
        

if __name__ == '__main__':
    unittest.main(exit=True)