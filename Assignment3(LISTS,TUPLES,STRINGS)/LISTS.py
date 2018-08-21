
#Q.1- Create a list with user defined inputs.
print('Question no.1\nCreate a list with user defined inputs.\n')
our_list = [] 
 
first_v = (input('Enter first value: '))
second_v = (input('Enter second value: '))
third_v = (input('Enter third value: '))
 
our_list.append(first_v)
our_list.append(second_v)
our_list.append(third_v)

print('The list thus created is', our_list)
print('__________________________________________________')
#__________________________________________________
#Q.2- Add the following list to above created list:[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
#__________________________________________________
print('\nQuestion no.2\n')
list = [] # create empty list
list2 = ['google','apple','facebook','microsoft','tesla'] #predefined list

firstv = (input('Enter first value: '))
secondv = (input('Enter second value: '))
thirdv = (input('Enter third value: '))
 
list.append(firstv)
list.append(secondv)
list.append(thirdv)

print('our_list=', our_list)
print('\n Adding this following list to a predefined list...which is\n,')
print('list2=',list2)
final=our_list+list2
print('\n\nANSWER\t',final)
print('__________________________________________________')
#_____________________________________________
#Q3. The no. of times an object appears in a list
#-----------------------------------------------
print('\nQ3.')
print('Question no. 3\nThe no. of times an object appears in a list\n')

list3=['hello','hi','google','apple','orange','hello','hi','hi','what','is','the','problem']
print('\n')
print("The no of times 'hi' comes in the LIST :",list3.count('hi'))
print("\nThe no of times 'hello' comes in the LIST :",list3.count('hello'))
print("\nThe no of times 'is' comes in the LIST :",list3.count('is'))
print("\nThe no of times 'orange' comes in the LIST :",list3.count('orange'))
print('__________________________________________________')

#__________________________________________________________
#Q.4 - create a list with numbers and sort it in ascending order.
#_________________________________________________________
print('\nQ4.')
print('\n create a list with numbers and sort it in ascending order.\n')
#vowel list
list4 = ['o','i','a','u','e']
print('The list to be sorted : ',list4)
list4.sort()
print('\nSorted list :',list4)
print('__________________________________________________')



#_____________________________________________________________
# Q.5 Given are two one-dimensional arrays A and B which are sorted in ascending order.Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]
#_____________________________________________________________
print('\nQ5.')
print('Given are two one-dimensional arrays A and B which are sorted in ascending order.')
print('Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order. [List]\n\n')
print('The 2 lists to be sorted and merged are\n')
print("a = [2,1,3,4,5]\nb = [9,8,6,7,10]")
a = [2,1,3,4,5]
b = [9,8,7,6,10]
a.sort()
b.sort()
print('\nSorted lists :')
print(a,b)

print('merging the two arrays into 1 single array')
c=a+b
print(c)
c.sort()
print('SORTED ARRAY  C :',c)

#__________________________________________________________________
#Q.6 - Count even and odd numbers in that list.
#______________________________________________________
print('\nQ6.')
print('Count even and odd numbers in that list.')
count_even=0
count_odd=0
for i in c:
    if not i % 2:
        count_even+=1
    else:
        count_odd+=1
print('Number of even numbers : ',count_even)
print('Number of odd numbers : ',count_odd)



#________________________________________________________
