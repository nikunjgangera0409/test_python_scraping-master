from collections import Counter

def exercise_one():
    for i in range(1,101):
        if(i%3==0 and i%5==0):
            print("ThreeFive")
        elif(i%3==0):
            print("Three")
        elif(i%5==0):
            print("Five")
        else:
            print(i)

def make_list(num):
    lst1 = []
    print(num//10)
    def num_str(val):
        print(val/10<0)
        if(val/10 < 1):
            lst1.append(int(val))
            return;
        else:
            num_str(val/10)
    num_str(num)
    print(lst1)

def exercise_2(A):
    hashmap = {}
    elements = list(str(A))
    n = len(elements)
    if n > 8 or (len(set(elements)) != len(elements)): return 0
    elif n == 1: return 1
    for i in range(n):
        temp = int(elements[i])
        if temp == 0 or temp == 1: return False
        try:
            if hashmap[temp]: return False
        except:
            hashmap[temp] = True
        for j in map(int, elements[i+1:]):
            temp *= j
            try:
                if hashmap[temp]: return False
            except:
                hashmap[temp] = True
    return True

def exercise_3(lst):
    total = 0
    for item in lst:
        if isinstance(item, str) and item.isdigit() or (isinstance(item, int) and item >= 0):
            total += int(item)
    return total if total > 0 else False

def check_anagrams(word1, word2):
    word1 = word1.replace(" ", "").lower()
    word2 = word2.replace(" ", "").lower()
    return sorted(word1) == sorted(word2)

def exercise_4(word, word_list):
    return [w for w in word_list if check_anagrams(word, w)]

