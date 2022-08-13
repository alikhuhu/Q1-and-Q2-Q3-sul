class ff:
    def jj (self,a,b):
        v=""
        for k in a:
            if k!=b:
                v+=k
        print (v)
a=input("enter the string")
b=input("inter the charcter you want to remove ")

g=ff()
g.jj(a,b)