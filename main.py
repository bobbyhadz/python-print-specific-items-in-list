# Print specific items in a List in Python

my_list = ['bobby', 'hadz', '.', 'com']

# ✅ print the first item in a list
first = my_list[0]
print(first)  # 👉️ 'bobby'

# ✅ print the last item in a list
last = my_list[-1]
print(last)  # 👉️ 'com'

# ✅ print slice containing multiple list items
result = my_list[1:3]
print(result)  # 👉️ ['hadz', '.']