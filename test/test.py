
def g():
    a,b,idx=0,1,0
    while idx<10:
        a,b,idx=b,a+b,idx+1
        yield b

if __name__ == "__main__":
    print(1)
    f=g()
    for i in f:
        print(i)
