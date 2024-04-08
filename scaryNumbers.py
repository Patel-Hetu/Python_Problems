#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 21:29:29 2022

@author: saachigupta
"""
# Python example solution midterm

scary_count = 0
for i in range(10**4, 10**5+1):
	tempstr = str(i)
	if (tempstr.find("000") != -1):
		if (tempstr.find("000") == True):
			print("True case", tempstr.find("000"), i) # You're catching these (where the index returned is 1 (1 == True in Python))
		else:
			print("Valid case", tempstr.find("000"), i) # But missing these... (where the index returned is not 1 (e.g. 2) but also NOT -1 (so it does occur))
		scary_count += 1

print(scary_count)
    