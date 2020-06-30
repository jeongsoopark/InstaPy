# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import smart_run
import random


#def likeMyFollower(userid, userpw, numLike):
    #with smart_run(session):

# 나를 팔로하는 사람 중 내가 팔로 하지 않은 사람들을 팔로
def sendFollow(session):
    print("sendFollow")

# 내가 팔로보냈는데 나 팔로 안하는 사람 언팔
def unfollow(session, numUnfollow):
    print("언팔 숫자 = ", numUnfollow)
    with smart_run(session):
        session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=random.randrange(500, 800))
