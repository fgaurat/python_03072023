from ctypes import CDLL,c_char_p

def main():
    libc = CDLL('hello.o')
    libc.sayHello()
    s = b"fred"
    libc.hello(c_char_p(s))

if __name__ == '__main__':
    main()
    
    