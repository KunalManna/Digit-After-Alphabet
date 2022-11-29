#Sort character of the string,first alphabet symbols followed by digit


def sepAlphaDigit(s):
    
    alphabet=[]
    digit=[]
    for ch in s:
        if ch.isalpha():
            alphabet.append(ch)
        else:
            digit.append(ch)
    k=sorted(alphabet)
    p=sorted(digit)
    output=''.join(k+p)
    return output

s=input("Enter the string:\n")            #B4A1D3
ans=sepAlphaDigit(s)
print(ans)                                #ABD134