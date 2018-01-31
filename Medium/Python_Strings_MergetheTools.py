def merge_the_tools(string, k):
    l = [string[i*k:i*k+k] for i in range(int(len(string)/k))]
    s = ""
    c = 0
    for ele in l:
        for letter in ele:
            if letter not in s:
                s = s + letter
        print(s)
        s = ""

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
