def check_string(s):
    if s.startswith('The'):
        return "Found It!"
    else:
        return "Nope."
str1 = 'The'
str2 = 'Thumbs up'
str3 = 'Theatre can be boring'
print(check_string(str1))
print(check_string(str2))
print(check_string(str3))
