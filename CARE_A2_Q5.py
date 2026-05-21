arr = ['a', 'b', 'c', 'b', 'c', 'c', 'a']

found = False

for i in arr:
    if arr.count(i) % 2 != 0:
        print(i)
        found = True
        break

if found == False:
    print("All are even")
