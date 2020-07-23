import pytest

from fb_post.utils.create_comment import create_comment

from fb_post.exceptions import InvalidCommentContent, InvalidPostException

from fb_post.models import Comment

from fb_post.exceptions import InvalidUserException


@pytest.mark.django_db
def test_create_comment_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
         create_comment(2, 1, "usha")
    #assert

@pytest.mark.django_db
def test_create_comment_post_id_invalid(user):
    #arrange
    #act
    with pytest.raises(InvalidPostException):
        create_comment(1, 1, "usha")
    #assert

@pytest.mark.django_db
def test_create_comment_comment_content_invalid(user, post):
    #arrange
    #act
    with pytest.raises(InvalidCommentContent):
        create_comment(1, 1, "")
    #assert

@pytest.mark.django_db
def test_create_comment_valid(user, post):
    #arrange
    #act
    comment_id = create_comment(1, 1, "ofcourse!!!")
    #assert
    assert Comment.objects.get(id=1).id == comment_id
