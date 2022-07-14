liste = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
yeni_liste = []
def flatten(n):
    for i in n:
        if isinstance(i, list):
            flatten(i)
        else:
            yeni_liste.append(i)

flatten(liste)
print(yeni_liste)