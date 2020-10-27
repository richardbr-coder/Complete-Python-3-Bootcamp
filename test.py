x = 5
y = 7.5
z = x*y

print(x)
print(type(x))

mt_income = 100

tax_rate = .1

my_taxes = mt_income * tax_rate

print(my_taxes)


#strings
print('hello \t world')

string = 'hello'
print(len(string))


#indexing and slicing
mystring = 'hello world'

print(mystring[-1])

mystring = 'abcdefghijklmn'
mystring = 'Hello world'
print('RichardRandell'[0])


#string concatnation 
x='hello world'
print(x.title())

#formatting
print('this is a string {}'.format('INSERTED'))
print('the {2} {1} {0}'.format('fox','brown','quick'))
print('the {q} {b} {f}'.format(f='fox', b='brown', q='quick'))

result = 1.675476463
print('the result was {r:1.3f}'.format(r=result))

#f strings
name = "jose"
name1 = 'sam'
print(f'hello, his name is {name} {name1}')

#list
my_list = [1,2,3]

my_list = ['STRING', 100, 23.2]
print(len(my_list))
mylist = ['one','two', 'three']
mylist[1:]
another_list = ['one', 'ten']
new_list = my_list + another_list
print(new_list)
new_list[0] = 'ONE ALL CAPS'
print(new_list)
new_list.append('six')
print(new_list)

print(new_list.pop())
popped_item = new_list.pop(0)
print(popped_item)
mylist.sort()
print(mylist)
type(mylist)

numb_list = [4,5,234,1,8,3,89,7,0]
numb_list.sort()
print(numb_list)

numb_list.reverse()
print(numb_list)

#dictionary 
prices_lookup = {'apple':2.99, 'oranges':1.99, 'milk':5.00}
print(prices_lookup['apple'])

d = {'k1':123, 'k2':[0,1,2], 'k3':{'insideKey':100}}
print(d['k2']['insideKey'])