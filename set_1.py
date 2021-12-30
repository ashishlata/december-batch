nums = {1,1,2,2,3,4}
print(len(nums))

d = {"john":40, "peter":45}
print(list(d.keys()))

a = [4,7,3,2,5,9]
for index,i in enumerate(a):
    print (index,i)



str = input("Enter a string\n")
# create a string with characters at multiples of 2
modified_string = str[::2]
print(modified_string)

str = input("Enter a string\n")
print (str[::-1])