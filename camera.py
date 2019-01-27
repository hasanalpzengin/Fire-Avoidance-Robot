import pexpect
import time

def startCamera():
    global process
    process = pexpect.spawn("bash")
    process.expect(r'\$')
    process.sendline('python rpi_video_yedek.py')
    process.expect('\n')
    time.sleep(10)
    
def isPerson():
    global process
    process.expect('\n')
    output = process.before
    print(output)
    if("Person" in output):
        return True
    else:
        return False
    
