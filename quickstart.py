# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
import tagModule
import followModule

userid = "jeongsoop0"
userpw = "Ss19751975"


# set workspace folder at desired location (default is at your home folder)
set_workspace(path=None)
# get an InstaPy session!

session = InstaPy(username=userid, password=userpw)

session.set_action_delays(  enabled=True,
                            randomize=True,
                            random_range_from=60,
                            random_range_to=130,
                            like=3,
                            comment=5,
                            follow=4.17,
                            unfollow=28,
                            story=10)

tagModule.tagLike(session, numLike=10, bFollow=True)
#tagModule.tagFollow(session, numFollow=4)

session.end()