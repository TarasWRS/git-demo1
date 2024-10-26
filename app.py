print("I'm learning Git merge conflicts")
name = input('Please enter your name: ')
last_name = input('Please enter your last name: ')
nick = input('Please enter your nickname: ')
print('Hi, {} {}! a.k.a. {}!'.format(name, last_name, nick))
<<<<<<< HEAD
name = input('Please enter your name: ')
last_name = input('Please enter your last name: ')
print('Hi, {} {}!'.format(name, last_name))
=======
nick = input('Please enter your nickname: ')
print('Hi, {}!'.format(nick))
>>>>>>> room15
print("I'm learning Git merge conflicts")
