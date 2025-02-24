RED = "\033[1;31m"
YELLOW = "\033[1;93m"
PURPLE = "\033[35m"
RESET = "\033[0m"


print(fr"""
======================================================================================================================================
{RED}
 __      __                .___.__  .__           _      ________                                   _
/  \    /  \___________  __| _/|  | |__| ______ _/ |_   /  _____/  ____   ____   _______________  _/ |__  ____  _____
\   \/\/   /  _ \_  __ \/ __ | |  | |  |/  ___/ |  __| /   \  ____/ __ \ /    \_/ __ \_  __ \__ \ |   __|/  _ \|  ___|
 \        (  <_> )  | \/ /_/ | |  |_|  |\___ \  |  |   \    \_\  \  ___/|   |  \  ___/|  | \// _ \|  |  (  <_> )  |
  \__/\  / \____/|__|  \____ | |____/__/____  > |__|    \______  /\___  >___|  /\___  >__|  (____/|__|   \____/|__|
       \/                   \/              \/                 \/     \/     \/     \/          	      {YELLOW}version 1{RESET}

															by {PURPLE}@rugbedbugg{RESET}
=======================================================================================================================================
This is a wordlist generator that takes in the file names of the username and passowrd files.
For best experience, try running this program in the same directory as the username and password files!!

{RED}[IMPORTANT]{RESET}
The output format of the resulting wordlist is
{YELLOW}"username:password"{RESET}

This is my first wordlist I've made, updates will be made in future! 💪 💪 💪
Other output formats will be supported in subsequent versions 😉



Use this tool at your own discretion!!!
I will NOT be responsible for any illegal actions facilitated by this tool 💀💀💀

""")

uname_file = input("Enter username file: ")
password_file = input("Enter password file: ")
combined_file = input("Enter final wordlist name: ")


with open(uname_file, "r") as uname, open(password_file, "r") as passwd:
	usernames = uname.read().splitlines()
	passwords = passwd.read().splitlines()

length = None
extra = None
if len(usernames) > len(passwords):
	length = len(passwords)
	print("More usernames than passwords! Creating separate file.")

	extra_file = input("Enter name for remaining usernames file: ")
	with open(extra_file, "w") as extra:
		extra.write("\n".join(usernames[length:] + "\n"))
elif len(usernames) < len(passwords):
	length = len(usernames)
	print("More passwords than usernames! Creating separate file.")

	extra_file = input("Enter name for remaining passwords file: ")
	with open(extra_file, "w") as extra:
		extra.write("\n".join(passwords[length:] + "\n"))
else:
	length = len(usernames)


with open(combined_file, "w") as final:
	for i in range(length):
       		final.write(f"{usernames[i]}:{passwords[i]}\n")

print(f"Successful created {combined_file} with {length} usernames and passwords")

