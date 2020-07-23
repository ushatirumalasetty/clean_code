import datetime
import factory
from .test_factory import *
import pytest

from freezegun import freeze_time

from fb_post.models import User, Post, Comment, Reaction

from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidPostException
from fb_post.exceptions import InvalidCommentException

from fb_post.utils.get_post import get_post
from fb_post.utils.get_user_posts import get_user_posts
from fb_post.utils. get_replies_for_comment import  get_replies_for_comment

@pytest.mark.django_db
def test_get_post_post_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidPostException):
        get_post(3)
    #assert

@pytest.mark.django_db
@freeze_time(str(datetime.now()))
def test_get_post():
    
    #arrange
   
    user_obj1=UserFactory.create_batch(1, name="ammu") 
    user_obj2=UserFactory.create_batch(2, name="ammudu") 
    post_obj1=PostFactory.create_batch(1, posted_by=user_obj1, content="ammu is a very good girl")
    post_obj2=PostFactory.create_batch(1, posted_by=user_obj2, content="ammudu is a very good girl")
    comment_obj1=CommentFactory.create_batch(1, commneted_by=user_objs[1],post=post_obj1, content="yes ofcourse!!!")
    comment_obj2=ReplyFactory.create_batch(1, commneted_by=user_objs[2],post=post_obj1 ,content="yes ofcourse!!!", parent_comment=comment_obj1)
    post_reaction1=PostReactionsFactory.create_batch(post=post_obj1, reacted_by=user_obj1, reaction="WOW")
    post_reaction2=PostReactionsFactory.create_batch(post=post_obj2, reacted_by=user_obj2, reaction="SAD")
    comment_reaction1=CommentReactionFactory.create_batch(comment=comment_obj1, reacted_by=user_obj1, reaction="WOW")
    
    #act

    details = get_post(1)
    
    #assert

    assert details == {
        "post_id": 1,
        "posted_by": {
            "name": "ammu",
            "user_id": 1,
            "profile_pic":None
        },
        "posted_at":str(datetime.now()),
        "post_content": "ammu is a very good girl",
        "reactions": {
            "count": 1,
            "type": ["WOW"]
        },
        "comments": [
            {
                "comment_id": 1,
                "commenter": {
                    "user_id": 1,
                    "name":"ammu",
                    "profile_pic":None
                },
                "commented_at":str(datetime.now()),
                "comment_content": "yes ofcourse!!!",
                "reactions": {
                    "count": 1,
                    "type": ["WOW"]
                },
                "replies_count": 1,
                "replies": [{
                    "comment_id": 2,
                    "commenter": {
                        "user_id": 2,
                        "name": "ammudu",
                        "profile_pic":None
                    },
                    "commented_at":str(datetime.now()),
                    "comment_content":"yes ofcourse!!!",
                    "reactions": {
                        "count": 0,
                        "type": []
                    },
                }]
            },
        ],
        "comments_count": 1,
    }


@pytest.mark.django_db
def test_get_user_posts_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        get_user_posts(3)
    #assert

@pytest.mark.django_db
@freeze_time(str(datetime.now()))
def test_get_user_posts():
    #arrange
    User.objects.create(name="ammu")
    User.objects.create(name="ammudu")
    Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    Post.objects.create(posted_by_id=2, content="ammudu is a very good girl")
    Comment.objects.create(commented_by_id=1, post_id=1, content="yes ofcourse!!!")
    Comment.objects.create(commented_by_id=2, post_id=1, content="yes ofcourse!!!", parent_comment_id=1)
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    Reaction.objects.create(comment_id=1, reaction="WOW", reacted_by_id=1)
    
    UserFactory.create_batch(1, name="ammu") 
    UserFactory.create_batch(2, name="ammudu") 
    PostFactory.create_batch(1, posted_by_id=1, content="ammu is a very good girl")
    PostFactory.create_batch(1, posted_by_id=2, content="ammudu is a very good girl")
    CommentFactory.create_batch(1, commented_by_id=1,post_id=1, content="yes ofcourse!!!")
    ReplyFactory.create_batch(1, commented_by_id=2,post_id=1 ,content="yes ofcourse!!!", parent_comment_id=1)
    PostReactionsFactory.create_batch(post_id=1, reacted_by_id=1, reaction="WOW")
    PostReactionsFactory.create_batch(post_id=2, reacted_by_id=2, reaction="SAD")
    CommentReactionFactory.create_batch(comment_id=1, reacted_by_id=1, reaction="WOW")
    
    
    #act
    
    details = get_user_posts(1)
    #assert
    assert details == [{
        "post_id": 1,
        "posted_by": {
            "name": "ammu",
            "user_id": 1,
            "profile_pic":None
        },
        "posted_at":str(datetime.now()),
        "post_content": "ammu is a very good girl",
        "reactions": {
            "count": 1,
            "type": ["WOW"]
        },
        "comments": [
            {
                "comment_id": 1,
                "commenter": {
                    "user_id": 1,
                    "name":"ammu",
                    "profile_pic":None
                },
                "commented_at":str(datetime.now()),
                "comment_content": "yes ofcourse!!!",
                "reactions": {
                    "count": 1,
                    "type": ["WOW"]
                },
                "replies_count": 1,
                "replies": [{
                    "comment_id": 2,
                    "commenter": {
                        "user_id": 2,
                        "name": "ammudu",
                        "profile_pic":None
                    },
                    "commented_at":str(datetime.now()),
                    "comment_content":"yes ofcourse!!!",
                    "reactions": {
                        "count": 0,
                        "type": []
                    },
                }]
            },
        ],
        "comments_count": 1,
    }]

@pytest.mark.django_db
def test_get_replies_for_comment_comment_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidCommentException):
        get_replies_for_comment(3)
    #assert

@pytest.mark.django_db
@freeze_time(str(datetime.now()))
def test_get_replies_for_comment():
    #arrange
    User.objects.create(name="ammu")
    User.objects.create(name="ammudu")
    Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    Post.objects.create(posted_by_id=2, content="ammudu is a very good girl")
    Comment.objects.create(commented_by_id=1, post_id=1, content="yes ofcourse!!!")
    Comment.objects.create(commented_by_id=2, post_id=1, content="yes ofcourse!!!", parent_comment_id=1)
    #act
    details = get_replies_for_comment(1)
    #assert
    assert details == [{
        "comment_id": 2,
        "commenter": {
                        "user_id": 2,
                        "name": "ammudu",
                        "profile_pic":None
                    },
        "commented_at":str(datetime.now()),
        "comment_content":"yes ofcourse!!!"}]
