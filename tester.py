import subprocess

t = 35
z = 80
y = 0.4
l = 2.0
v = '-vv'

subprocess.call('python Capstone.py Images/hello.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 5', shell=True)
subprocess.call('python Capstone.py Images/immediate.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 9', shell=True)
subprocess.call('python Capstone.py Images/peak.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 4', shell=True)
subprocess.call('python Capstone.py Images/people.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 6', shell=True)
subprocess.call('python Capstone.py Images/same.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 4', shell=True)
subprocess.call('python Capstone.py Images/school.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 6', shell=True)
subprocess.call('python Capstone.py Images/sore.png -t '+str(t)+' '+str(v)+' -z '+str(z)+' -y '+str(y)+' -l '+str(l)+' -x 4', shell=True)
