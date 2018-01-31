if __name__ == '__main__':
    mn = input()
    array = input()
    A = input()
    B = input()
    
    m = int(mn.split(' ')[0])
    n = int(mn.split(' ')[1])
    
    l = array.split(' ')
    As = set(A.split(' '))
    Bs = set(B.split(' '))
    
    happiness = 0
    
    for i in l:
        if i in As:
            happiness = happiness + 1
        if i in Bs:
            happiness = happiness - 1
            
    print(happiness)
