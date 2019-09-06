import urllib
import random

# -------------------------  Build API --------------------------- #
def random_char():
    return random.randint(97, 122)

def generate_test_case(sec_dic):
    res = []
    for i in range(24,25): # max length is 24
        for j in range(11):
            #sub = []
            word = ''
            k = i
            while k > 0:
                word += chr(random_char())
                k -= 1
            # get_wordsII(sec_dic,word,len(word),sub)
            # if sub: 
            print word
            res.append(word)
    return res

def get_words(a, l, r, res):
    if l==r:
        word = ''.join(a[:])
        if word in dictionary:
            res.append(word)
            return res
    else: 
        for i in range(l,r+1): 
            a[l], a[i] = a[i], a[l] 
            get_words(a, l+1, r, res) 
            a[l], a[i] = a[i], a[l] # backtrack 
    
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
  
def get_wordsII(lwords, charSet, k, res): 
    for word in lwords[k]:
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
            print(word)
            res.append(word)
            return res

if __name__ == '__main__':
        
    # -------------------------- Data Preparation -------------------- #
    print 'Pull the target dictionary from website'
    dictionary = []
    link = "https://raw.githubusercontent.com/yzcmf/DiDi_Interview/master/words.txt"
    f = urllib.urlopen(link)
    line = f.readline()
    dictionary.append(line.strip())
    while line:
        line = f.readline()
        if line.strip():dictionary.append(line.strip().lower())
    f.close()

    # n = len(dictionary)
    # print len(dictionary)
    # print dictionary[0], dictionary[1],dictionary[n-2], dictionary[n-1]
    # dictionary = set(dictionary)
    
    # sec_dic = dictionary_transform(dictionary)
    # cnt = 0
    # for i in range(25):
    #     if sec_dic.get(i):
    #         cnt += len(sec_dic[i])
    #         print i,len(sec_dic[i])
    # print n == cnt
    
    # print sec_dic[9][0:32403:1000]
    #generate_test_case(sec_dic) # generate test case
        
    # -------------- Test the result from user's input ---------------- #
    # N = int(raw_input('Enter total numbers of test cases:'))
    # for _ in range(N):
    #     res = []
    #     s = raw_input('Input a string:').rstrip()
    #     n = len(s) 
    #     a = list(s.lower()) 
    #     get_words(a, 0, n-1, res)
    #     print 'res=',list(set(res))
        
    # -------------- Test the result from test_case.txt ---------------- #
    print 'Pull the test cases from website'
    for i in [0,1,2]:
        if i>0: 
            link2 = "https://raw.githubusercontent.com/yzcmf/DiDi_Interview/master/test_cases" + str(i+1) + ".txt"
        else:
            link2 = "https://raw.githubusercontent.com/yzcmf/DiDi_Interview/master/test_cases.txt"
        f2 = urllib.urlopen(link2)
        line = f2.readline()
        print '--------------------Test Case ' + str(i+1) + '--------------------'
        tests = []
        tests.append(line.strip())
        while line:
            line = f2.readline()
            if line.strip():tests.append(line.strip().lower())
        f2.close()
    
        for test in tests:
            res = []
            s = test
            n = len(s) 
            a = list(s.lower()) 
            get_words(a, 0, n-1, res)
            print 'input=',s,'res=',list(set(res))
