def fibbo(n):
    if n<=1:
        return n
    else:
        return fibbo(n-1) + fibbo(n-2)
n_terms = 7
if n_terms >= 0:
    for i in range(n_terms):
        print(fibbo(i))