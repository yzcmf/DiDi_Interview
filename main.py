#!/usr/bin/python
import urllib

# -------------------------  Build API --------------------------- #
def get_words(sec_dic,a, l, r, res):
    if l==r:
        word = ''.join(a[:])
        if word in sec_dic[r+1]:
            res.append(word)
            return res
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            get_words(sec_dic,a, l+1, r, res) 
            a[l], a[i] = a[i], a[l]

def dictionary_transform(dictionary):
    sec_dic = {}
    cnt = 0
    for d in dictionary:
        if sec_dic.get(len(d)):
            sec_dic[len(d)].append(d)
        else:
            sec_dic[len(d)] = [d]
        cnt += 1
    return sec_dic if cnt == len(dictionary) else None
    
def charCount(word): 
    dict = {} 
    for i in word: 
        dict[i] = dict.get(i, 0) + 1
    return dict
  
def get_wordsII(second_dictionary, charSet, k, res): 
    for word in second_dictionary[k]:
        word = word.lower()
        flag = 1
        chars = charCount(word) 
        for key in chars: 
            if key not in charSet: 
                flag = 0
            else: 
                if charSet.count(key) != chars[key]: 
                    flag = 0
        if flag == 1: 
            res.append(word)
    return res

if __name__ == '__main__':
        
    # -------------------------- Data Preparation -------------------- #
    print 'Pull the target dictionary from website...'
    dictionary = []
    link = "https://raw.githubusercontent.com/yzcmf/DiDi_Interview/master/words.txt"
    f = urllib.urlopen(link)
    line = f.readline()
    dictionary.append(line.strip())
    while line:
        line = f.readline()
        if line.strip():dictionary.append(line.strip().lower())
    f.close()

    n = len(dictionary)
    # dictionary = set(dictionary)
    
    sec_dic = dictionary_transform(dictionary)
    cnt = 0
    for i in range(25):
        if sec_dic.get(i):
            cnt += len(sec_dic[i])
    print 'dictionary build successful!' if n == cnt else 'dictionary build failure!'
        
    # --------------------------- Test the results  ----------------------------- #
    command = 's'
    while command == 's':
        k = int(raw_input('Enter test cases number from 1-5 or other number for user input:'))
        
        # -------------- Test the result from test_case.txt ---------------- #
        if k >= 1 and k <= 5:
            print 'Pull the test cases from website...'
            link2="https://raw.githubusercontent.com/yzcmf/DiDi_Interview/master/test_cases" + str(k) + ".txt"   
            f2 = urllib.urlopen(link2)
            line = f2.readline()
            print '--------------------Test Case ' + str(k) + '--------------------'
            strs = [line.strip()]
            while line:
                line = f2.readline()
                if line.strip():strs.append(line.strip().lower())
            f2.close()
            for i,s in enumerate(strs):
                res, n, a = [],len(s),list(s.lower()) 
                # get_words(sec_dic,a, 0, n-1, res)
                if n: get_wordsII(sec_dic, a, n, res)
                print 'case'+ str(i+1) + ':','input=',s,'res=',list(set(res))
        
        # -------------- Test the result from user's input ---------------- #
        else:
            N = int(raw_input('Enter total numbers of test cases you want to test:'))
            for i in range(N):
                s = raw_input('Input a string:').strip()
                res, n, a = [],len(s),list(s.lower()) 
                if n: get_wordsII(sec_dic, a, n, res)
                print 'case'+ str(i+1) + ':','input=',s,'res=',list(set(res))
        
        command = raw_input('Enter s to start or e to end the program:')
