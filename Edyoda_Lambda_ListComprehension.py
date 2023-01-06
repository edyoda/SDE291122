def subtracting_5(num):
  #num = num - 5
  return num - 5
 
print(subtracting_5(10))

subtracting_5_new = lambda num : num - 5
# lambda <paramter> : <expressions>
print(subtracting_5_new(10))


multiply_two_nos = lambda x,y : x*y
print(multiply_two_nos(10,20))

def multi(a,c):
    b = a*c
    return b

def maximum(a,b):
    if a>b:
        return a
    else:
        return b
    
print(maximum(100,50))   

maximum_new = lambda a,b : a if a>b else b
print(maximum_new(100,50))  
    
    
# lambda <parameters> : <if Expression>
# <if Expression> --> TRUE if condition else FALSE


maximum_new = lambda a,b : str(a)+" is greater" if a>b else str(b)+" is greater"
print(maximum_new(100,150)) 

maximum_new = lambda a,b : f"{a} is greater" if a>b else "{b} is greater"
print(maximum_new(1000,150)) 
int("1")

a,b,c = "abc","pqr","xyz"
print(a, b, c)
print(a+b+c)
print(a+" -- "+b+" -- "+c)
print(f"{a} -- {b} -- {c}")
print(f"asd asd asd {maximum_new(1000,150)}")
# f" asdasda {variable} aasasdasda" 


list_new = [1,2,3]
list_final=[]

def squaring_list(list_param):
    for i in list_param:
        list_final.append(i*i)
    return list_final

print(squaring_list(list_new)) #[1,4,9]

# map(func,iteratable)

print("lambda ", list(map(lambda x:x*x, list_new)))

list_new = ["guru","rahul","sham"]

print("STRING lambda", list(map(lambda x:x, ["guru","rahul","sham"])))
#['g','r','s']]

def last_element(str_value):
    return str_value[-1]


print("STRING no lambda", list(map(last_element, ["guru","rahul","sham"])))

print(list_new[0])

list_new = ["guru","rahul","sham"]
print(list_new[0])

def firstele(list_new):
    return list_new[0]
print("non lambda", firstele(list_new))  

firstelemlambda = lambda x:x[0] 
print("lambda", firstelemlambda(list_new))  
list_new = [1,2,3]
print(list(filter(lambda x:x > 1, list_new))) # [2,3]


list_new = [1,2,3]
list_final=[]
def add_5(list_param):
    for i in list_param:
        list_final.append(i+5)
    print(list_final) # [6,7,8]
    
    
add_5(list_new)

print([i+5 for i in list_new])
# [expression loop]


print(range(10))
ist_final=[]
for i in range(10):
    list_final.append(i)
print(list_final)

print([str(i)+" is a number" for i in range (10)])

new_list_var = [str(i)+" is a number" for i in range (10)]
print(new_list_var)

text_list_final = []
text_list = ["lists","are","IMPORTANT","data","TYPE"]
def to_make_uppercase(text_list):
    for word in text_list:
        if word.islower():
            text_list_final.append(word.upper())
        else:
            text_list_final.append(word.lower())
    return text_list_final
    
print(to_make_uppercase(text_list))



final_list_comp = [word.upper() if word.islower() else word.lower() for word in text_list]
print("method1 ",final_list_comp)
final_list_comp = [word.upper() for word in text_list if word.islower()]
print("method2 ",final_list_comp)


final_list_comp = [word.upper() if word.islower() else word.lower() for word in text_list]

