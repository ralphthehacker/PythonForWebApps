import re
line = "From rblanes31@gmail.com at Saturday 19:35:21"

#extracting email
email = re.findall("^From (\S+@\S+)",line)

#extracting just the domain
domain = re.findall("^From .*(@[^ ]*)",line)

print(email)
print(domain)

#Other way
a = line.split()
email = a[1]
domain = email.split('@')[1]
print(email)
print(domain)