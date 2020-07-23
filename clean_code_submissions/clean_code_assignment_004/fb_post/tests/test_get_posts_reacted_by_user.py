import pytest

from fb_post.utils.get_posts_reacted_by_user import get_posts_reacted_by_user

from fb_post.exceptions import InvalidUserException

@pytest.mark.django_db
def test_get_posts_reacted_by_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        get_posts_reacted_by_user(3)
    #assert

@pytest.mark.django_db
def test_get_posts_reacted_valid(user2, post2, reaction2):
    #arrange
    #act
    posts_reacted_by_user = [1]
    #assert
    assert list(get_posts_reacted_by_user(1)) == posts_reacted_by_user
