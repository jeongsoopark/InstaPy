# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import random

userid = "jeongsoop0"
userpw = "Ss19751975"

def unfollow(username, userpassword, numUnfollow):
    session = InstaPy(username=userid, password=userpw)
    with smart_run(session):
        session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=655)
    session.end()

# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)

unfollow(userid, userpw, 10)