s = "z"
n = 1

def solution(s, n):
    answer = ''
    alpha_low = "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y"
    alpha_up = tuple(low.upper() for low in alpha_low)
    for x in s:
        if x.islower() == True:
            y = alpha_low.index(x)
            z = alpha_low[y+n]
            answer += z
        elif x.isupper() == True:
            y = alpha_up.index(x)
            z = alpha_up[y+n]
            answer += z
        else:
            answer += " "
    return answer

print(solution(s, n))

def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i]=chr((ord(s[i])-ord('A')+ n)%26+ord('A'))
        elif s[i].islower():
            s[i]=chr((ord(s[i])-ord('a')+ n)%26+ord('a'))

    return "".join(s)

def caesar(s, n):
    result = ""
    for i in s:
        if i.isalpha():
            if i.islower():
                result += chr((ord(i) - ord("a") + n) % 26 + ord("a"))
            else:
                result += chr((ord(i) - ord("A") + n) % 26 + ord("A"))
        else:
            result += i
    return result

