# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import smart_run
from instapy import InstaPy
import psutil
import random



# 내가 팔로보냈는데 나 팔로 안하는 사람 언팔
def unfollow(userid, userpw, numUnfollow):
      
    #이전 작업이 있으면 삭제 
    PROCNAME_DRIVER = "geckodriver.exe"
    PROCNAME_BROWSER="firefox.exe"
    for proc in psutil.process_iter():
        # check whether the process name matches
        if proc.name() == PROCNAME_DRIVER:
            proc.kill()
        elif proc.name() == PROCNAME_BROWSER:
            proc.kill()

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

    print("언팔 숫자 = ", numUnfollow)
    with smart_run(session):
        session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=random.randrange(500, 800))
