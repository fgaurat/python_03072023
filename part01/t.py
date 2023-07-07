


theListOfTheValues = input("entrez des chiffres : ")
# theListOfTheValues = "1,2,8,9"
list_int =[int(value) for value in theListOfTheValues.split(',')] 
s = sum(list_int)
print(s)