# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import tagModule
import followModule
import schedule
import time                             
import random
import psutil
from pathlib import Path
import os.path

##############################
randomOffset = 5
#태그로 좋아요 누를 포스트 수
nLike = 20
#좋야오 하나당 1분 정도 걸리니까 예약시간 잘 계산해서 넣어야함
#태그 좋야요 실행할 예약 시간
timeLike = [
    "09:00",
    "15:00",
    "21:00"
]
nFollow = 50
timeFollow = []
#언팔 수
nUnfollow = 20
timeUnfollow = [
    "12:00",
    "18:00"
]
###############################
isTestMode = False
###############################
userid = ""
userpw = ""

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

#tagModule.tagLike(session, numLike=gNumLike, bFollow=True)
#tagModule.tagFollow(session, numFollow=gNumFollower)

""" 
with smart_run(session):
    myUnfollowers = session.pick_nonfollowers("jeongsoop0", live_match=True, store_locally=True)
print(myUnfollowers)
"""
if isTestMode == False:
    print("동작할 숫자를 설정합니다. 각 숫자는 입력값의 -30, +30사이에서 랜덤으로 생성됩니다.")
#    nFollow = int(input("태그로 검색/팔로우시 한 태그당 좋아요 누를 수:"))
#    nLike = int(input("태그로 검색/좋아요시 한 태그당 좋아요 누를 수:"))
#    nUnfollow = int(input("언팔할 사람 수: "))
    gNumFollower=random.randint(nFollow-randomOffset ,nFollow+randomOffset)
    gNumLike=random.randint(nLike-randomOffset, nLike+randomOffset)
    gNumUnfollow=random.randint(nUnfollow-randomOffset, nUnfollow+randomOffset)
    gMinuteFollower=random.randint(0, 59)
    gMinuteLike=random.randint(0, 59)
    gMinuteUnfollower=random.randint(0, 59)

    print("좋아요 초기값 = ", gNumLike, "팔로우 초기값", gNumFollower, "언팔 초기값", gNumUnfollow)

    #시간은 반드시 앞에 0으로 시작하는 세트여야함, 6시면 06, 9분이면 09, 7시 2분이면 07:02 이런 식으로
    print("예약시간을 설정합니다. 각 시간은 0을 포함한 시각이어야 합니다. 예로 6시면 06:00, 7시 2분이면 07:02로 입력해주세요")
#    timeTagLike = input("태그로 좋아요 예약시간: 좋아요 후 3초간의 딜레이가 발생합니다. ")
#    timeTagFollow = input("태그로 follow 예약시간: ")
#    timeUnfollow = input("Unfollow 예약시간: ")

def setNumbers(nFollow, nLike, nUnfollow):
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

    
session.set_ignore_if_contains(['glutenfree', 'french', 'tasty'])
if isTestMode == False:
    schedule.every().day.at("01:00:00").do(setNumbers)
    for t in timeLike:
        print("좋아요 작업 예약 : ", t, "횟수", gNumLike)
        schedule.every().day.at(t).do(tagModule.tagLike, session, gNumLike, False)
    #schedule.every().day.at("13:03").do(tagModule.tagFollow, session, gNumFollower)
    for t in timeUnfollow:
        print("언팔 작업 예약 : ", t, "횟수", gNumUnfollow)
        schedule.every().day.at(t).do(followModule.unfollow, session, gNumUnfollow)
    while True:
        schedule.run_pending()
        time.sleep(10)
        #schedule.every(5).minutes.do(tagModule.tagLike, session, 1, False)
else:
#    start = time.time()
#    tagModule.tagLike(session, nLike, False)
#    end = time.time()
#    print(nLike, " taglike 걸린시간: ", (end-start), "초")
    start = time.time()
    followModule.unfollow(session, nUnfollow)
    end = time.time()
    print(nUnfollow, " unfollow 걸린시간: ", (end-start), "초")


