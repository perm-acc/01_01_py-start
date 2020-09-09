my_list = [22, 34.32, 'str', True, [1,2], dict(param1= 'value1' , param2= 'value2'), b'byte array']
print(type(my_list))
i = 0
for element in my_list:
    print(type(my_list[i]))
    i+=1