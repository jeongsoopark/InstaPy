# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import smart_run
from instapy import InstaPy
import random

#태그로 검색한 게시물에 좋아유
def tagLike(userid, userpw, numLike, bFollow, morePost=1):
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
    try:
        session.login()
        session.set_user_interact(amount=morePost-1, randomize=True, percentage=100)
        session.set_do_follow(enabled=bFollow, percentage=100, times=1)
        session.like_by_tags(taglist, amount=numLike, interact=(bFollow or morePost > 1), skip_top_posts=False )
    except:
         print("exception occur")
         session.end()
    


#태그로 검색한 게시물에 가서 게시자 팔로
def tagFollow(userid, userpw, session, numFollow):
    
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
    print("태그로 팔로우하기를 시작합니다. 태그 목록은 hashtags.txt에서 5개 무작위추출합니다")
    taglistfull = session.target_list("hashtags.txt")
    #Random choose from big tag list
    print("팔로어 숫자 = ", numFollow)
    taglist = random.sample(taglistfull, 5)
    print(taglist)
    try:
        session.login()
        session.follow_by_tags(taglist, amount=numFollow, skip_top_posts=False)
    except:
        print("exception occur")
        session.end()