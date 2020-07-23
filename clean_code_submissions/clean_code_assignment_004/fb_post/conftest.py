import pytest

from fb_post.models import User, Post, Reaction, Comment

from fb_post.tests.test_factory import *

@pytest.fixture
def populate_database():
    user=UserFactory.create_batch(1, name="ammu")
    user1=UserFactory.create_batch(1, name="ammudu")
    user2=UserFactory.create_batch(1, name="usha")
    user3=UserFactory.create_batch(1, name="usha tirumalasetty")
    post1=PostFactory.create_batch(1, posted_by=user,content="ammu is a very good girl")
    post2=PostFactory.create_batch(1, posted_by=user1,content="ammudu is a very good girl")
    post3=PostFactory.create_batch(1, posted_by=user2,content="usha is a very good girl")
    comment_obj1=CommentFactory.create_batch(1, commneted_by=user_objs[1],post=post_obj1)
    comment_obj2=CommentFactory.create_batch(1, commneted_by=user_objs[2],post=post_obj1)
    post_reaction1=PostReactionsFactory.create_batch(post=post_obj1, reacted_by=user_objs[1])
    post_reaction2=PostReactionsFactory.create_batch(post=post_obj2, reacted_by=user_objs[2])
    comment_reaction1=CommentReactionFactory.create_batch(comment=comment_obj1, reacted_by=user_objs[1])
    
    


@pytest.fixture
def post3():
    Post.objects.create(posted_by_id=1, content="ammu is a very good girl")
    Post.objects.create(posted_by_id=2, content="ammudu is a very good girl")
    post_obj3 = Post.objects.create(posted_by_id=3, content="usha is a very good girl")
    return post_obj3

@pytest.fixture
def comment():
    comment_obj = Comment.objects.create(commented_by_id=1, post_id=1, content="yes ofcourse!!!")
    return comment_obj

@pytest.fixture
def reply_comment():
    reply_comment_obj = Comment.objects.create(commented_by_id=2, post_id=1, content="yes ofcourse!!!", parent_comment_id=1)
    return reply_comment_obj

@pytest.fixture
def reaction():
    reaction_obj = Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    return reaction_obj

@pytest.fixture
def reaction2():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    reaction_obj2 = Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    return reaction_obj2

@pytest.fixture
def reaction3():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    reaction_obj3 = Reaction.objects.create(post_id=3, reaction="WOW", reacted_by_id=3)
    return reaction_obj3

@pytest.fixture
def reaction4():
    Reaction.objects.create(post_id=1, reaction="WOW", reacted_by_id=1)
    Reaction.objects.create(post_id=2, reaction="SAD", reacted_by_id=2)
    Reaction.objects.create(post_id=3, reaction="WOW", reacted_by_id=3)
    reaction_obj4 = Reaction.objects.create(post_id=3, reaction="SAD", reacted_by_id=4)
    return reaction_obj4

@pytest.fixture
def reaction_to_comment():
    reaction_obj = Reaction.objects.create(comment_id=1, reaction="WOW", reacted_by_id=1)
    return reaction_obj



def reaction5():
    reaction_obj4 = Reaction.objects.create(post_id=3, reaction="SAD", reacted_by_id=4)
    return reaction_obj4