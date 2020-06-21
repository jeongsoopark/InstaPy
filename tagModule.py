# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random

def tagLike(session, numLike, bFollow, morePost=1):
    taglist = session.target_list("hashtags.txt")
    print(taglist)
    with smart_run(session):
        session.set_user_interact(amount=morePost-1, randomize=True, percentage=100)
        session.set_do_follow(enabled=bFollow, percentage=50, times=1)
        session.like_by_tags(taglist, amount=numLike, interact=(bFollow or morePost > 1) )
     
def tagFollow(session, numFollow):
    taglist = session.target_list("hashtags.txt")
    print(taglist)
    with smart_run(session):
        session.follow_by_tags(taglist, amount=numFollow)