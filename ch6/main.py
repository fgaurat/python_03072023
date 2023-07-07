import fibo as fi
# from fibo import fib as f
from fibo import fib as theFib,fib2

def fib(n):
    print("bonjour",n)

if __name__ == "__main__":
    print("main",__name__)

    # fibo.fib(1000)
    # l = fibo.fib2(1000)
    # fi.fib(1000)
    # l = fi.fib2(1000)
    # print(l)

    fib(1000)
    theFib(1000)
