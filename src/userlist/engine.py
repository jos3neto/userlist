from pwd import getpwall

def fetch_users():
	users = []
	for user in getpwall():
		if user.pw_uid >= 1000 and 'home' in user.pwd_home:
			users.append(
			{
              'name': user.pw_name,
              'id': user.pw_uid,
              'home': user.pw_dir,
              'shell': user.pw_shell,
            })
	return users