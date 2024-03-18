# 數組（Tuple）、集合（Set）以及詞典（Dictionary），詞典搜尋

d={}
while(True):
    k=input("Key: ")
    if k=="end":break
    v=input("Value: ")
    d[k]=v
k=input("Search Key: ")
print(k in d)