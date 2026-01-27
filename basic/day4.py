mm=int(input())
if mm<0 or mm>100:
    print("invalid marks")
elif mm>89:
    print("distinction")
elif mm>74:
    print("merit")
elif mm>39:
    print("pass")
else:
    print("fail")
