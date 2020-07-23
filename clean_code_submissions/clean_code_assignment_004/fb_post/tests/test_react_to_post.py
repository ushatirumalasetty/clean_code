import pytest

from fb_post.utils.react_to_post import react_to_post

from fb_post.exceptions import InvalidUserException, InvalidPostException

from fb_post.exceptions import InvalidReactionTypeException

from fb_post.models import Reaction

@pytest.mark.django_db
def test_react_to_post_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        react_to_post(3, 1, "WOW")
    #assert

@pytest.mark.django_db
def test_react_to_post_comment_id_invalid(user):
    #arrange
    #act
    with pytest.raises(InvalidPostException):
        react_to_post(1, 3, "i too agree")
    #assert

@pytest.mark.django_db
def test_react_to_post_reaction_type_invalid(user, post):
    #arrange
    #act
    with pytest.raises(InvalidReactionTypeException):
        react_to_post(1, 1, "yep")
    #assert

@pytest.mark.django_db
def  test_react_to_post_first_time(user, post, reaction):
    #arrange
    #act
    #assert
    assert reaction.id == 1

@pytest.mark.django_db
def  test_react_to_post_already_reacted_reaction_type_same(user, post, reaction):
    #arrange
    #act
    react_to_post(1, 1, "WOW")
    #assert
    assert list(Reaction.objects.all()) == []

@pytest.mark.django_db
def  test_react_to_post_already_reacted_reaction_type_different(user, post, reaction):
    #arrange
    #act
    react_to_post(1, 1, "LIT")
    reactions = Reaction.objects.all()
    #assert
    assert reactions[0].reaction == "LIT"
