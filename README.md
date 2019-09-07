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

git clone git clone https://github.com/username/xyz.git
cd xyz && ./runme.sh


Note:

Commit 9132ae6 : contains details about each API; delete it for making the main good looking

Test cases : from 1-5, word length is 0-25 

Word dictionary : https://raw.githubusercontent.com/lad/words/master/words, around 22k words in total

Main program : enter number 1-5 to load corsponding test cases by github; enter other number to input test cases yourself.

get_word func: getwordI is much slower than getwordII, because I map length of the word as the key for getwordII; Both getword func is useful, and both of them could be optimized by using set(O(1)) for the store the words instead of list(O(N))
