x = 10


def demo(x):
    y = x + 5
    print("Di dalam fungsi:")
    print("x =", x)
    print("y =", y)
    return y


hasil = demo(20)

print("Di luar fungsi:")
print("x =", x)
print("hasil =", hasil)
