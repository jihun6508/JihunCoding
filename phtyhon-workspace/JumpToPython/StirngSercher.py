import re
p = re.compile("[a-z]+")
m = p.search("5python")
print(m.start())
print(m.end())
print(len("5python"))
