# Find-deranged-words
Find deranged words for test

I met some tests like this: 
"FORDFA-have enough money for something."

Tescher want we find the correct form in "FORDFA". I know it's "Afford" but it takes me long time.

So, This program was born.

# How to use it

It include two files. csv is dictionary and py is a program.

You need put them in the same directory.
And open a terminal and run 
```
python find-words.py
```
Put the words you want to find (program will convert words to lower case).

Wait a moment, program will return all the words which found in dictionary.

Like this:

```
PS E:\Research\Find-deranged-words\src> python .\find-word.py
oerh
['oher', 'abbr. Ohio (美国俄亥俄州及其邮政编码)']
['rohe', ' [人名] 罗厄']
['rheo', 'n. rheostat的简写']
['hoer', 'n. 锄地者']
['hore', ' [人名] [英格兰人姓氏] 霍尔 Hoare的变体']
['hero', 'n. 英雄, 超越常人者, 男主角']
```
