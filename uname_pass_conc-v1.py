print(r"""
======================================================================================================================================

 __      __                .___.__  .__           _      ________                                   _
/  \    /  \___________  __| _/|  | |__| ______ _/ |_   /  _____/  ____   ____   _______________  _/ |__  ____  _____
\   \/\/   /  _ \_  __ \/ __ | |  | |  |/  ___/ |  __| /   \  ____/ __ \ /    \_/ __ \_  __ \__ \ |   __|/  _ \|  ___|
 \        (  <_> )  | \/ /_/ | |  |_|  |\___ \  |  |   \    \_\  \  ___/|   |  \  ___/|  | \// _ \|  |  (  <_> )  |
  \__/\  / \____/|__|  \____ | |____/__/____  > |__|    \______  /\___  >___|  /\___  >__|  (____/|__|   \____/|__|
       \/                   \/              \/                 \/     \/     \/     \/          	      version 1

															by @rugbedbugg
=======================================================================================================================================
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
