#Exercise Python 46

#Make a program that shows on screen a countdown to the fireworks burst, going from 10 to 0, with a 1-second pause between them.
from time import sleep
from style import red, green, blue, none
print('COUNTDOWN!!!')
sleep(0.5)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(f'''{blue}BOOOOM!
{red}BOOOOM!
{green}BOOOOM! {none}''')
