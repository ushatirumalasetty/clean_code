import pytest

from fb_post.models import Post

from fb_post.utils.create_post import create_post

from fb_post.exceptions import InvalidUserException, InvalidPostContent

@pytest.mark.django_db
def test_create_post_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        create_post(2, "usha")
    #assert

@pytest.mark.django_db
def test_create_post_post_content_invalid(user):
    #arrange
    #act
    with pytest.raises(InvalidPostContent):
        create_post(1, "")
    #assert

@pytest.mark.django_db
def test_create_post_valid(user):
    #arrange
    #act
    post = create_post(1, "usha")
    #assert
    assert Post.objects.get(id=1).id == post
