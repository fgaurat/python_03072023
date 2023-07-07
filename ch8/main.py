import sys
import traceback


class DivBy12Error(Exception):
    
    def __init__(self):
        super().__init__("Division par 12 !")
    
def div(a,b):
    if b==12:
        # raise Exception("Division par 12 !")
        e = DivBy12Error()
        raise e 
    result = a/b
    return result

def call_div(a,b):
    
    try:
        print('LOG: start call_div',a,b)
        r = div(a,b)
        
    # except Exception as e:
    #     print(e)
    #     print('LOG: end call_div. Close file',a,b)
    #     raise e
    finally:
        print('LOG: end call_div. Close file',a,b)
    return r

def main():
    try:
        a = 2
        b = int(input('b : '))
        c = call_div(a,b)
        print("c",c)
    except DivBy12Error as e:
        print("DivBy12Error",e)    
        # traceback.print_exc()
    except ZeroDivisionError as e:
        print("ZeroDivisionError",e)    
        # traceback.print_exc()
    except TypeError as e:
        print("TypeError",e)    
        # traceback.print_exc()
    except ValueError as e:
        print("ValueError",e)    
        # traceback.print_exc()
    except Exception as e:
        print("Exception",e)    
        traceback.print_exc()
    else:
        print('else') 
    finally:
        print('finally') 
        
    
    print("après")

if __name__=='__main__':
    main()
