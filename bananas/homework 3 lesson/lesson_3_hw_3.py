a = input()
'Taras Shevchenko*1814-03-09*1861-03-10'
list = a.split("*")
list
["'Taras Shevchenko", '1814-03-09', "1861-03-10'"]
list.insert(1,1814)
list.insert(2,1861)
list.remove('1814-03-09')
list.remove("1861-03-10'")
list
["'Taras Shevchenko", 1814, 1861]
Name = list[0]
age = list[2] - list[1]
Name
"'Taras Shevchenko"
age
47