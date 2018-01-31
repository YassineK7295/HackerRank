def minion_game(string):
    n = len(string)
    i = 0
    
    kevin = 0
    stuart = 0
    
    while (i < n):
        if string[i:i+1] in ['A','E','I','O','U']:
            kevin = kevin + n-i
        else:
            stuart = stuart + n-i
                
        i = i + 1
            
    if kevin > stuart:
        print("Kevin " + str(kevin))
    elif stuart == kevin:
        print("Draw")
    else:
        print("Stuart " + str(stuart))

if __name__ == '__main__':
    s = input()
    minion_game(s)
