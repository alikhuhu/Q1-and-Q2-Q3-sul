def jj(a):
    v=[]
    for x in a:
        v.append(x)
    for i in v:
        h=v.count(i)
        print(f"there's",h,"{",i,"}","in",a," in the string")   
a="hi im alik"
jj(a)