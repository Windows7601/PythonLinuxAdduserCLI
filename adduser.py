import os
running = True
while running:
    delete = input('Delete or add (d or a)')
    if delete == 'a':
        username = input('Username')
        os.system(f'sudo adduser --allow-all-names {username}')
    elif delete == 'd':
        username = input('Username')
        os.system(f'sudo deluser {username}')
    if input('New') == 'yes':
        pass
    else:
        running = False
