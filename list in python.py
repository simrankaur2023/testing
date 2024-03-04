list1 = [ 1,3,5,6,7,8,"simran","diya",14.56, 34.56]
list2 = [10,20,30,49]
list3 = [11.2,3]

print("list1[2]:",list1[2])
# indexing

print("list2[1:3]:",list2[1:3])
# slicing

print("Number of elements in list1 -", len(list1))
# count elements in list


print(list1.append("harleen"),list1)
#  append elements


list1.pop(5)
print(list1)
# pop


list1.remove(1)
print(list1)
#remove

list3.insert(0,2)
print(list3)
#insert

list2.extend(["simmi", "harshi"])
print(list2)
#extend

list3.sort()
print(list3)
#sort





