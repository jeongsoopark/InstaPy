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

#custom module
import tagModule
import followModule
##############################
randomOffset = 5
#태그로 좋아요 누를 포스트 수
nLike = 20
#좋야오 하나당 1분 정도 걸리니까 예약시간 잘 계산해서 넣어야함
#태그 좋야요 실행할 예약 시간
timeLike = [
   "09:02",
    "13:58",
    "16:21",
    "20:11", 
    "22:01"
]
nFollow = 20
timeFollow = []
#언팔 수
nUnfollow = 20
timeUnfollow = [
    "12:00",
    "18:00",
    "00:50"
]
###############################
isTestMode = False
###############################
userid = ""
userpw = ""

def setNumbers():
    #############################################################################################
    #태그로 검색해서 팔로우할 숫자
    global gNumFollower 
    gNumFollower=random.randint(nFollow-randomOffset ,nFollow+randomOffset)
    #태그로 검색해서 좋아요 할 숫자
    global gNumLike
    gNumLike=random.randint(nLike-randomOffset, nLike+randomOffset)
    #찾아서 언팔할 숫자
    global gNumUnfollow 
    gNumUnfollow=random.randint(nUnfollow-randomOffset, nUnfollow+randomOffset)
    global gMinuteFollower
    gMinuteFollower=random.randint(0, 59)
    global gMinuteLike
    gMinuteLike=random.randint(0, 59)
    global gMinuteUnfollower
    gMinuteUnfollower=random.randint(0, 59)
    print("새숫자, 좋아요: ", gNumLike, "팔로어 : ", gNumFollower, "언팔 : ", gNumUnfollow)


PROCNAME_DRIVER = "geckodriver.exe"
PROCNAME_BROWSER="firefox.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME_DRIVER:
        proc.kill()
    elif proc.name() == PROCNAME_BROWSER:
      proc.kill()

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
setNumbers()

if isTestMode == False:
    schedule.every().day.at("00:40").do(setNumbers)
    for t in timeLike:
        print("좋아요 작업 예약 : ", t, "횟수", gNumLike)
        schedule.every().day.at(t).do(tagModule.tagLike, userid, userpw, gNumLike, False)
    #schedule.every().day.at("13:03").do(tagModule.tagFollow, session, gNumFollower)
    for t in timeUnfollow:
        print("언팔 작업 예약 : ", t, "횟수", gNumUnfollow)
        schedule.every().day.at(t).do(followModule.unfollow, userid, userpw, gNumUnfollow)
    while True:
        schedule.run_pending()
        time.sleep(10)
        #schedule.every(5).minutes.do(tagModule.tagLike, userid, userpw, 1, False)
else:
#    start = time.time()
#    tagModule.tagLike(session, nLike, False)
#    end = time.time()
#    print(nLike, " taglike 걸린시간: ", (end-start), "초")
    start = time.time()
    followModule.unfollow(userid, userpw, nUnfollow)
    end = time.time()
    print(nUnfollow, " unfollow 걸린시간: ", (end-start), "초")
