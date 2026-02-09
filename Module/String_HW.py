
from collections import Counter

def char_freq(s):
    freq = {}
    for ch in s:
        ct = 0
        for i in s:
            if i == ch:
                ct += 1
        freq[ch] = ct
    return freq

str1 = "banana"
feq = char_freq(str1)
print(feq)

freq=Counter(str1)
print(freq)

l=['a','b','c','a','b','a']
freq_list = Counter(l)
print(freq_list)    

