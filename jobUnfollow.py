# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import schedule
import time                             
import random
import psutil
from pathlib import Path
import os.path

nUnfollow = 20
randomOffset = 5
numUnfollow = random.randint(nUnfollow-randomOffset, nUnfollow+randomOffset)

PROCNAME_DRIVER = "geckodriver.exe"
PROCNAME_BROWSER="firefox.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME_DRIVER:
        proc.kill()
    elif proc.name() == PROCNAME_BROWSER:
      proc.kill()

userid=""
userpw=""
#command line interface로 가즈아
# 
idpwFileExist = os.path.isfile("idpw.txt")
if idpwFileExist == True: 
    idpwFile = open("idpw.txt", "r")
    credential = idpwFile.read().split('\n')
    userid = credential[0]
    userpw = credential[1]
    #userpw = idpwFile.read().split('\n')
else:
    print("id/password 파일이 없습니다\n")
    userid = input("ID :")
    userpw = input("PW :")
    idpwFile = open("idpw.txt", "w")
    idpwFile.write(userid)
    idpwFile.write("\n")
    idpwFile.write(userpw)
    idpwFile.write("\n")
    idpwFile.close()
    print("새 idpw.txt를 저장했습니다")

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)
# get an InstaPy session!

session = InstaPy(username=userid, password=userpw)
session.set_action_delays(  enabled=True,
                             randomize=True,
                                random_range_from=50,
                                random_range_to=130,
                                like=3,
                                comment=5,
                                follow=4.17,
                                unfollow=28,
                                story=10)

print("이만큼 언팔 할거임  = ", numUnfollow)
with smart_run(session):
    session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=random.randrange(500, 800))