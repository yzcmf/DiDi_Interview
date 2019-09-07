# DiDi_Interview
Interview problem hold for DiDi 2019.9.3

Word Anagram
Requirements

Input: a set of input characters, ranging from a-z, case-insensitive.
Output: all the possible English words from the dictionary that could be composed of these characters, case-insensitive.
The possible English words could be fetched from, for example,  https://raw.githubusercontent.com/lad/words/master/words which is a copy of /usr/share/dict/words.
Ensure the main program can be run in https://coderpad.io/
 

Deliverable

Submit your code to github.com and email us the link of your code repo, where the repo contains the following.
One source code file for the main program.
One runme.sh bash script to (compile and) run the program on Linux or Mac terminal.
[Optional] one README file with additional instructions, if needed.
[Bonus] one additional file with test cases.

How to test

git clone https://github.com/yzcmf/DiDi_Interview.git

cd DiDi_Interview && ./runme.sh


Note:

Commit 9132ae6 : contains details about each API; delete it for making the main good looking

Test cases : from 1-5, word length is 0-25 

Word dictionary : https://raw.githubusercontent.com/lad/words/master/words, around 22k words in total

Main program : enter number 1-5 to load corsponding test cases by github; enter other number to input test cases yourself.

Get_words API: mainly API to get all the words from the input string. getwordsI() is much slower than getwordsII(), because I map length of the word as the key for getwordII; Both getword func is useful, and both of them could be optimized by using set(O(1)) for the store the words instead of list(O(N))


Demo:

(base) wirelessprv-10-195-83-103:OA user$ git clone https://github.com/yzcmf/DiDi_Interview.git
Cloning into 'DiDi_Interview'...
remote: Enumerating objects: 67, done.
remote: Counting objects: 100% (67/67), done.
remote: Compressing objects: 100% (60/60), done.
remote: Total 219 (delta 34), reused 8 (delta 4), pack-reused 152
Receiving objects: 100% (219/219), 817.20 KiB | 6.75 MiB/s, done.
Resolving deltas: 100% (94/94), done.
(base) wirelessprv-10-195-83-103:OA user$ 
(base) wirelessprv-10-195-83-103:OA user$ cd DiDi_Interview && ./runme.sh
Pull the target dictionary from website...
dictionary build successful!
Enter test cases number from 1-5 or other number for user input:1
Pull the test cases from website...
--------------------Test Case 1--------------------
case1: input= A res= ['a']
case2: input= f res= ['f']
case3: input= k res= ['k']
case4: input= p res= ['p']
case5: input= u res= ['u']
case6: input= aa res= ['aa']
case7: input= am res= ['ma', 'am']
case8: input= ay res= ['ay', 'ya']
case9: input= de res= ['ed', 'de']
case10: input= er res= ['re', 'er']
case11: input= aal res= ['aal', 'ala']
case12: input= ach res= ['cha', 'ach']
case13: input= aes res= ['aes', 'sea', 'ase']
case14: input= aid res= ['aid', 'ida']
case15: input= aku res= ['auk', 'kua', 'aku']
case16: input= abelite res= ['abelite']
case17: input= abigail res= ['abigail']
case18: input= abjoint res= ['abjoint']
case19: input= aardvark res= ['aardvark']
case20: input= abatised res= ['abatised']
case21: input= abducens res= ['abducens']
case22: input= abeyance res= ['abeyance']
case23: input= abjectly res= ['abjectly']
case24: input= aaronical res= ['aaronical']
case25: input= abashedly res= ['abashedly']
case26: input= abdicator res= ['abdicator']
case27: input= abhorrent res= ['abhorrent', 'earthborn']
case28: input= abnegator res= ['abnegator']
case29: input= aani res= ['aani']
case30: input= abie res= ['abie']
case31: input= achy res= ['chay', 'achy']
case32: input= actu res= ['actu']
case33: input= adda res= ['dada', 'adad', 'adda']
case34: input= aalii res= ['aalii']
case35: input= abate res= ['beata', 'ateba', 'batea', 'abate']
case36: input= abear res= ['abear']
case37: input= abmho res= ['abohm', 'abmho']
case38: input= abort res= ['abort', 'tabor']
case39: input= ababua res= ['ababua']
case40: input= abater res= ['artabe', 'eartab', 'abater', 'trabea']
case41: input= abduce res= ['abduce']
case42: input= abject res= ['abject']
case43: input= ablins res= ['ablins']
case44: input= aaronic res= ['aaronic', 'ocarina', 'nicarao']
case45: input= abashed res= ['abashed']
Enter s to start or e to end the program:s
Enter test cases number from 1-5 or other number for user input:0
Enter total numbers of test cases you want to test:3
Input a string:efw
case1: input= efw res= ['few']
Input a string:dog
case2: input= dog res= ['god', 'dog']
Input a string:cat
case3: input= cat res= ['cat', 'act']
Enter s to start or e to end the program:e
(base) wirelessprv-10-195-83-103:DiDi_Interview user$ 
