import pytest

from fb_post.utils.get_posts_with_more_positive_reactions import get_posts_with_more_positive_reactions

@pytest.mark.django_db
def test_get_posts_with_positive_reactions(user2, post2, reaction2):
    #arrange
    #act
    #assert
    assert list(get_posts_with_more_positive_reactions()) == [1]

@pytest.mark.django_db
def test_get_posts_with_positive_reactions_reactions_positive_none(user4,
                                                                   post3,
                                                                   reaction5):
    #arrange
    #act
    #assert
    assert list(get_posts_with_more_positive_reactions()) == []

@pytest.mark.django_db
def test_get_posts_with_positive_reactions_positive_and_negitive_equal(user2,
                                                                       post2,
                                                                       reaction2
                                                                       ):
    #arrange
    #act
    #assert
    assert list(get_posts_with_more_positive_reactions()) == [1]
