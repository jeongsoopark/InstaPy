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

userid = "jeongsoop0"
userpw = "Ss19751975"

PROCNAME_DRIVER = "geckodriver.exe"
PROCNAME_BROWSER="firefox.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME_DRIVER:
        proc.kill()
    elif proc.name() == PROCNAME_BROWSER:
      proc.kill()


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
gNumFollower=random.randint(20, 50)
gNumLike=random.randint(20, 50)
gNumUnfollow=random.randint(20, 50)

def setNumbers():
    #############################################################################################
    #태그로 검색해서 팔로우할 숫자
    global gNumFollower 
    gNumFollower = random.randint(20, 40)
    #태그로 검색해서 좋아요 할 숫자
    global gNumLike
    gNumLike = random.randint(20, 40)
    #찾아서 언팔할 숫자
    global gNumUnfollow 
    gNumUnfollow= random.randint(20, 40)
    #

print("좋아요 초기값 = ", gNumLike, "팔로우 초기값", gNumFollower, "언팔 초기값", gNumUnfollow)

#시간은 반드시 앞에 0으로 시작하는 세트여야함, 6시면 06, 9분이면 09, 7시 2분이면 07:02 이런 식으로
schedule.every().day.at("06:00").do(setNumbers)
schedule.every().day.at("09:03").do(tagModule.tagLike, session, gNumLike, False)
schedule.every().day.at("13:03").do(tagModule.tagFollow, session, gNumFollower)
schedule.every().day.at("16:14").do(followModule.unfollow, session, gNumUnfollow)

while True:
  schedule.run_pending()
  time.sleep(10)
#schedule.every(5).minutes.do(tagModule.tagLike, session, 1, False)