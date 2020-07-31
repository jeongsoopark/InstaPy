# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import smart_run
from instapy import InstaPy

import random



# 내가 팔로보냈는데 나 팔로 안하는 사람 언팔
def unfollow(userid, userpw, numUnfollow):
      
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
    with smart_run(session, threaded=True):
        session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=random.randrange(500, 800))
