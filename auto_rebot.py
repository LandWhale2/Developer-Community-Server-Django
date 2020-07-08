import os


output = os.popen('docker-compose up').read()

print(output)