# Chapter 9
# Exercise 5: This program records the domain name (instead of the address) where
# the message was sent from instead of who the mail came from (i.e., the whole email
# address). At the end of the program, print out the contents of your dictionary.
#
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}
domain_dict =dict()
fname = input('Enter a file name:')
fopen = open(fname)
for line in fopen:
    line = line.strip()
    if line.startswith('From '):
        s = line.split()
        email = s[1]
        pos = email.find('@')
        domain = email[pos+1:]
        if domain not in domain_dict:
            domain_dict[domain] = 1
        else:
            domain_dict[domain] = domain_dict[domain] + 1
print(domain_dict)
