import sys


if __name__ == "__main__":
    
    sys.argv[1:3]
    # theListOfTheValues = input("entrez des chiffres : ")
    # theListOfTheValues = "1,2,8,9"
    if len(sys.argv)==2:
        sys.exit("dis donc !")


    theListOfTheValues = sys.argv[1]
    list_int =[int(value) for value in theListOfTheValues.split(',')] 
    s = sum(list_int)
    print(s)