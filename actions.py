import sys, action, status, helpers
import newPage
# new imports start here

# settings = helpers.get_settings()

try:
	action = str(sys.argv[1])
except:
	action = None

try:
	name = str(sys.argv[2])
except:
	name = None

if action == 'status' or action == None:
	status.execute()

elif action == 'action':
	# You will want to change the name to something specific, when developing
	action.execute()

elif action == "create":
    newPage.execute(name)
# new actions start here
