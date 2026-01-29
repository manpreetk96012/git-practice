mm=int(input())
if mm<0 or mm>100:
    print("invalid marks")
elif mm>=90:
    print("pass")
    print ("grade=A")
elif mm>=75:
    print("pass")
    print ("grade=B")
elif mm>=60:
    print("pass")
    print ("grade=C")
elif mm>=45:
    print("pass")
    print ("grade=D")
elif mm>=33:
    print("pass")
    print ("grade=E")
else:
    print("fail")
    print("grade=F")
