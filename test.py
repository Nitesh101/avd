import os,subprocess
base = "/var/lib/jenkins/workspace/"
#base = "/home/nitesh/Documents/avd/"
base_file = os.path.join(base,"test/sample/")
for test in os.listdir(base_file):
	os.chdir(base_file)
	if test.endswith(".py"):
		process = subprocess.Popen('python {0}'.format(test), shell=True)
		status = process.communicate()

