# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:00:11 2018

@author: wangw
"""
def find_prod_array(intlist):
    before = [1]
    after = [1]
    idx = 0;
    while(idx < len(intlist)-1):
        before.append(before[idx]*intlist[idx])
        after.insert(0,after[0]*intlist[len(intlist) - idx - 1])
        idx += 1
    idx = 0;
    while(idx<len(intlist)):
        intlist[idx] = before[idx]*after[idx]
        idx += 1
    return intlist
def main():
    test = [1,2,3,4,5]
    prod_list = find_prod_array(test)
    print(prod_list)
    
    test2 = [1]
    print(find_prod_array(test2))
main()