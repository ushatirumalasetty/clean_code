import pytest

from fb_post.utils.delete_post import delete_post

from fb_post.exceptions import InvalidUserException, InvalidPostException

from fb_post.exceptions import UserCannotDeletePostException

from fb_post.models import Post

@pytest.mark.django_db
def test_delete_post_user_id_invalid(user, post):

    #arrange
    #act
    with pytest.raises(InvalidUserException):
        delete_post(3, 1)
    #assert

@pytest.mark.django_db
def test_delete_post_post_id_invalid(user, post):
    #arrange
    #act
    with pytest.raises(InvalidPostException):
        delete_post(1, 3)
    #assert

@pytest.mark.django_db
def test_delete_post_user_id_not_creator_of_post(user2, post2):
    #arrange
    #act
    with pytest.raises(UserCannotDeletePostException):
        delete_post(1, 2)
    #assert

@pytest.mark.django_db
def test_delete_post_valid(user2, post2):
    #arrange
    #act
    delete_post(1, 1)
    #assert
    assert list(Post.objects.filter(id=1, posted_by_id=1)) == []
