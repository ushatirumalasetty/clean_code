import pytest

from fb_post.exceptions import InvalidPostException

from fb_post.utils.get_reactions_to_post import get_reactions_to_post

@pytest.mark.django_db
def test_get_reactions_to_post_post_id_invalid(user, post):
    #arrange
    #act
    with pytest.raises(InvalidPostException):
        get_reactions_to_post(3)
    #assert

@pytest.mark.django_db
def test_get_reactions_to_post_valid(user2, post2, reaction2):
    #arrange
    #act
    post_reactions = [{"user_id": 1, "name": "ammu", "profile_pic": None, "reaction": "WOW"},]
    #assert
    assert get_reactions_to_post(1) == post_reactions
