grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

def out_put(any_list):
    for elem in any_list:
        print('*',elem)


grocery_list.append('rice')
out_put(grocery_list)

print(len(grocery_list))

banana_count = grocery_list.count('bananas') 
if banana_count == 0:
    print("You need to get bananas")
else:
    print("You don't need to pick up bananas today")

#print(grocery_list[1])

#out_put(sorted(grocery_list))

grocery_list.pop(3)
out_put(sorted(grocery_list))



