import os 
running = True 
while running: 
	delete = input('Delete or add or add to group or set group (d or a or g or s, respectively)') 
    if delete == 'a': 
        username = input('Username:') 
        try:
        		os.system(f'sudo adduser --allow-all-names {username}')
        except:
            print('Sorry, an error occured and you need to restart the script.')
    elif delete == 'd': 
        username = input('Username:') 
        sure = input("Are you sure? (y or n):") 
        if sure == "y": 
            try:
            		os.system(f'sudo deluser {username}')
            except:
                print('Sorry, an error occured and you need to restart the script.')
                running = False
                pass
    elif delete == 'g':
        username = input('Username:')
        group = input('Group to add:')
        try:
        		os.system(f'sudo usermod -aG {group} {username}')
        except:
            print('Sorry, an error occured and you need to restart the script.')
            running = False
            pass
    elif delete == 's':
        username = input('Username:')
        group = input('Group:')
        sure = ('Are you sure? (y or n) This deletes the user from existing groups!:')
        if sure == 'y':
            try:
            		os.system(f'sudo usermod -G {group} {username}')
            except:
                print('Sorry, an error occured and you need to restart the script.')
                running = False
                pass
    if input('New (y/n)') == 'y': 
        pass 
    else: 
        running = False
