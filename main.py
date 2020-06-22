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

userid = "jeongsoop0"
userpw = "Ss19751975"
#############################################################################################
#태그로 검색해서 팔로우할 숫자
gNumFollower = random.randrange(20, 40)
#태그로 검색해서 좋아요 할 숫자
gNumLike = random.randrange(20, 40)
#찾아서 언팔할 숫자
gNumUnfollow = random.randrange(20, 40)
#

#############################################################################################
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
tagModule.tagFollow(session, numFollow=gNumFollower)


#schedule.every(5).minutes.do(tagModule.tagLike, session, 1, False)
#while True:
#  schedule.run_pending()
#  time.sleep(10)