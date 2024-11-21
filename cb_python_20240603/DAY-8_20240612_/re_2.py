import re

pattern = '^C.........y$'
test_string = 'CloudBinary'

result = re.match(pattern, test_string)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
