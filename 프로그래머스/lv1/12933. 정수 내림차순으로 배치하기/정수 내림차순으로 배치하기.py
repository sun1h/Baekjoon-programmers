def solution(n):
    n=str(n)
    lst=[]
    for i in n:
        lst.append(int(i))
    lst.sort(reverse=True)
    for i in range(len(lst)):
        lst[i] = str(lst[i])
    l=''.join(lst)
    return int(l)

# def solution(n):
#     ls = list(str(n))
#     ls.sort(reverse = True)
#     return int("".join(ls))