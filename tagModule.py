# -*- coding: utf-8 -*- 
""" Quickstart script for InstaPy usage """
# imports
from instapy import smart_run
import random

#태그로 검색한 게시물에 좋아유
def tagLike(session, numLike, bFollow, morePost=1):
    print("태그로 좋아요 누르기를 시작합니다. 태그 목록은 hashtags.txt를 이용하세요")
    taglist = session.target_list("hashtags.txt")
    print("좋아요 숫자=", numLike, "다른 포스트 좋아요 숫자=", morePost)
    #Random choose from big tag list
    print(taglist)
    with smart_run(session):
        session.set_user_interact(amount=morePost-1, randomize=True, percentage=100)
        session.set_do_follow(enabled=bFollow, percentage=100, times=1)
        session.like_by_tags(taglist, amount=numLike, interact=(bFollow or morePost > 1), skip_top_posts=False )
     
#태그로 검색한 게시물에 가서 게시자 팔로
def tagFollow(session, numFollow):
    print("태그로 팔로우하기를 시작합니다. 태그 목록은 hashtags.txt를 이용하세요")
    taglist = session.target_list("hashtags.txt")
    #Random choose from big tag list
    print("팔로어 숫자 = ", numFollow)
    print(taglist)
    with smart_run(session):
        session.follow_by_tags(taglist, amount=numFollow, skip_top_posts=False)