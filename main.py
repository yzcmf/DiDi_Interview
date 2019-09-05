import urllib

# -------------------------  Build API --------------------------- #
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
            
if __name__ == '__main__':
    
    # -------------------------- Data Preparation -------------------- #
    print 'Read file from target website'
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
    # print len(dictionary)
    # print dictionary[0], dictionary[1],dictionary[n-2], dictionary[n-1]
    dictionary = set(dictionary)
    
    # -------------------------- Test the result -------------------- #
    N = int(raw_input('Enter total numbers of test cases:'))
    for _ in range(N):
        res = []
        s = raw_input('Input a string:').rstrip()
        n = len(s) 
        a = list(s.lower()) 
        # print s,a
        get_words(a, 0, n-1, res)
        print 'res=',list(set(res))
    
