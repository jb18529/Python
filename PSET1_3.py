# MITx 6.00.1x
# Introduction to Computer Science and Programming Using Python
'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc

'''
#Aim was to eliminate redundancy in code so minimum of 13 lines.
ans = ""
for i in range(0, len(s)-1):
    p_string = s[i]
    m = i
    while m < len(s)-1:
        if s[m] <= s[m+1]:
            p_string += s[m+1]
            m += 1         
        elif m == len(s)-1 or s[m] > s[m+1]:
            break    
    if len(p_string) > len(ans) or len(p_string) == 0:
        ans = p_string                      
print(ans)
     
                
    
        

        