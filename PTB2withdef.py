from PTB1withdef import PTB1
def PTB2(a,b,c):
    if a == 0:
        return PTB1(b,c)
    else: 
        delta = b**2 - 4*a*c
        if delta > 0:
            x1 = round((-b + delta**(1/2) )/(2*a),2)
            x2 = round((-b - delta**(1/2) )/(2*a),2)
            return "2 nghiem phan biet la", "x1 =", round(x1,2), "x2 =", round(x2,2)
        elif delta == 0:
            x = round(-b/2*a,2)
            return "Nghiem kep",f"x={x}".format(round(x,2))
        else: 
            return "Vo nghiem"

a = float(input("Nhập số a:"))
b = float(input("Nhập số b:"))
c = float(input("Nhập số c:"))

print(f"Phương trình của bạn có dạng: {a}x**2+{b}x+{c}")
kq = PTB2(a,b,c)
print(kq)