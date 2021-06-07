
def reverse(li, start, wl):
    i, j = start, start + wl - 1
    while i < j:
        li[i], li[j] = li[j], li[i]
        i += 1
        j -= 1
 
def sen_rev(s):
    li = list(s)
    llen = len(li)
    start = 0
    while (start < llen) and (li[start] == ' '): #the first word start
        start += 1
    while start < llen: #Starting position
        wl = 0
        while ((start + wl) < llen) and (li[start + wl] != ' '): #Find out the length of the word
            wl += 1
        reverse(li, start, wl)
        start += wl
        while (start < llen) and (li[start] == ' '):
            start += 1
    li.reverse()
    return ''.join(li)
 
# w = input("input a sentence: ")
# rev_w = sen_rev(w)
# print(rev_w)