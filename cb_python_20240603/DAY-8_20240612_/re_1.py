import re 

def find_all_matches(p,s):
    matches = re.findall(p,s)
    return matches

# Variables
pattern = r'\d+'

# Variables
string = 'Welcome to C3Ops T4echnologies P6rivate Limite9d'

print(find_all_matches(pattern,string))