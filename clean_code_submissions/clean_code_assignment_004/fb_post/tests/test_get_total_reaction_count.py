import pytest

from fb_post.utils.get_total_reaction_count import get_total_reaction_count

@pytest.mark.django_db
def test_get_total_reaction_count(user, post, comment, reaction, reaction_to_comment):
    #arrange
    #act
    #assert
    assert get_total_reaction_count() == {'count':2}
