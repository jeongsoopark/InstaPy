# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
import random
from instapy import smart_run

def unfollow(session, numUnfollow):
    with smart_run(session):
        session.unfollow_users(amount=numUnfollow, nonFollowers=True, style="RANDOM", unfollow_after=42*60*60, sleep_delay=random.randrange(500, 800))
