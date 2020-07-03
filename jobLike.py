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

nLike = 20
randomOffset = 5
numLike = random.randint(nLike-randomOffset, nLike+randomOffset)
morePost = 2

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

ignoreList = session.target_list("ignore.txt")
session.set_ignore_if_contains(ignoreList)
print("태그로 좋아요 누르기를 시작합니다. 태그 목록은 hashtags.txt에서 5개 무작위추출합니다")
taglistfull = session.target_list("hashtags.txt")
print("좋아요 숫자=", numLike, "다른 포스트 좋아요 숫자=", morePost)
#Random choose from big tag list
taglist = random.sample(taglistfull, 5)
print(taglist)
with smart_run(session):
    #session.set_user_interact(amount=morePost-1, randomize=True, percentage=100)
    session.set_do_follow(enabled=False, percentage=100, times=1)
    session.like_by_tags(taglist, amount=numLike, interact=False, skip_top_posts=False )

