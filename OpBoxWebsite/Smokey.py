#!/usr/bin/env python

import random, time
import subprocess, thread

random.seed()

#dedicated to Chris Tucker's performance in 'Friday'
flavor = [
        "it's Friday; you ain't got no job... and you ain't got shit to do.",
        "you just got knocked the fugg-out",
	"You've got to be one stupid motherfucker to get fired on your day off."
]

def pollForScript():

    with open("scripts/script_queue", 'r') as f:
        for l in f.readlines():
            return l.strip()

def clearQueue():
    with open("scripts/script_queue", 'w') as f:
        f.write('')

if __name__ == "__main__":

    print "starting smokey"
    print random.choice(flavor)

    pid = None
    t_thread = None
    while 1:
        time.sleep(.5)
        s = pollForScript()

        if s:
            clearQueue()
            if s == "kill":
                break;
            if pid:
                print "killing current process"
                pid.kill()

            print "running " + s
            pid = subprocess.Popen(["python", "scripts/" + s], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            tee = subprocess.Popen(['tee', "-a", "logs/" + s + ".log"], stdin=pid.stdout)
            t_thread = thread.start_new_thread(tee.communicate, ())

    print "smokey going down"
    random.seed()
    print random.choice(flavor)
