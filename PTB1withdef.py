def PTB1(a,b):
    if a==0 and b == 0:
        return "Vô số nghiệm"
    elif    a==0 and b != 0:
        return "Vô nghiệm"
    else:
        x  = round(-b/a,2)
        return "Nghiệm x là:",x


