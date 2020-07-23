import pytest

from fb_post.utils.reply_to_comment import reply_to_comment
from fb_post.models import Comment

from fb_post.exceptions import InvalidCommentException
from fb_post.exceptions import InvalidReplyContent
from fb_post.exceptions import InvalidUserException

@pytest.mark.django_db
def test_reply_to_comment_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        reply_to_comment(3, 1, "i too agree")
    #assert

@pytest.mark.django_db
def test_reply_to_comment_comment_id_invalid(user):
    #arrange
    #act
    with pytest.raises(InvalidCommentException):
        reply_to_comment(1, 3, "i too agree")
    #assert

@pytest.mark.django_db
def test_reply_to_comment_reply_content_invalid(user, comment, post):
    #arrange
    #act
    with pytest.raises(InvalidReplyContent):
        reply_to_comment(1, 1, "")
    # assert

@pytest.mark.django_db
def test_reply_to_comment_for_direct_comment(user, comment, post):
    #arrange
    #act
    reply_id = reply_to_comment(1, 1, "u need to accept because thats true")
    #assert
    assert Comment.objects.get(content="u need to accept because thats true").id == reply_id

@pytest.mark.django_db
def test_reply_to_comment_for_reply_comment(user2, comment, reply_comment, post):
    #arrange
    #act
    reply_to_comment(2, 2, "ofcourse thats true")
    parent_id = 1
    #assert
    assert Comment.objects.get(content="ofcourse thats true").parent_comment_id == parent_id
