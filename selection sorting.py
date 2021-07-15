'''enter len of list=5
element1=1
element2=3
element3=6
element4=9
element5=0
user entered list: [1,3,6,9,0]
ascending order sorted list: [0,1,3,6,9]
descending order sorted list: [9,6,3,1,0]'''
n=int(input("enter len of list="))
list=[]
for i in range(n):
    list_element=int(input("enter element="))
    list.append(list_element)
print("normal list:",list)
for i in range(n):
    min_element=min(list[i:])
    index=list.index(min_element)
    list[i],list[index]=list[index],list[i]
print("ascending order sorted list:",list)
for i in range(n):
    max_element=max(list[i:])
    index=list.index(max_element)
    list[i],list[index]=list[index],list[i]
print("descending order sorted list:",list)