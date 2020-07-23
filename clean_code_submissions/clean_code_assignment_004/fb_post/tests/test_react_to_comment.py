import pytest


from fb_post.exceptions import InvalidUserException
from fb_post.exceptions import InvalidCommentException
from fb_post.exceptions import InvalidReactionTypeException

from fb_post.models import Reaction

from fb_post.utils.react_to_comment import react_to_comment

@pytest.mark.django_db
def test_react_to_comment_user_id_invalid():
    #arrange
    #act
    with pytest.raises(InvalidUserException):
        react_to_comment(3, 1, "WOW")
    #assert

@pytest.mark.django_db
def test_react_to_comment_comment_id_invalid(user):
    #arrange
    #act
    with pytest.raises(InvalidCommentException):
        react_to_comment(1, 3, "i too agree")
    #assert

@pytest.mark.django_db
def test_react_to_comment_reaction_type_invalid(user, post, comment):
    #arrange
    #act
    with pytest.raises(InvalidReactionTypeException):
        react_to_comment(1, 1, "yep")
    #assert

@pytest.mark.django_db
def  test_react_to_comment_first_time(user, post, comment, reaction_to_comment):
    #arrange
    #act
    #assert
    assert reaction_to_comment.id == 1

@pytest.mark.django_db
def  test_react_to_comment_already_reacted_reaction_type_same(user, post, comment, reaction_to_comment):
    #arrange
    #act
    react_to_comment(1, 1, "WOW")
    #assert
    assert list(Reaction.objects.all()) == []

@pytest.mark.django_db
def  test_react_to_comment_already_reacted_reaction_type_different(user, post, comment, reaction_to_comment):
    #arrange
    #act
    react_to_comment(1, 1, "LIT")
    reactions = Reaction.objects.all()
    #assert
    assert reactions[0].reaction == "LIT"
