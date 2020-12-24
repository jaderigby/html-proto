import json
from settings import settings

profilePath = settings['profile_url'] + settings['profile']

def load_profile():
	return json.loads(read_file(profilePath))

def get_settings():
	profile = load_profile()
	return profile['settings']

def read_file(FILEPATH):
	FILE = open(FILEPATH, 'r')
	data = FILE.read()
	FILE.close()
	return data

def write_file(FILEPATH, DATA):
	FILE = open(FILEPATH, 'w')
	FILE.write(DATA)
	FILE.close()

def run_command(CMD):
	import subprocess
	subprocess.call(CMD, shell=True)

def clone_repo(DESTINATION, USER, NAME):
	cloneCommand = 'cd {destination} && git clone https://github.com/{user}/{name}.git'.format(destination = DESTINATION, user = USER, name = NAME)
	run_command(cloneCommand)