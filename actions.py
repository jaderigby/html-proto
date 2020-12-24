import sys, addAction, status, helpers
import newPage
import messages as msg
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

args = sys.argv[2:]

# try:
# 	name = str(sys.argv[2])
# except:
# 	name = None

if action == None:
	msg.statusMessage()

elif action == '-action':
	addAction.execute(args)

elif action == '-profile':
	helpers.profile()

elif action == "-":
    newPage.execute(args)
# new actions start here
