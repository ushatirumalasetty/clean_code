import pytest

from fb_post.utils.get_reaction_metrics import get_reaction_metrics

@pytest.mark.django_db
def test_get_reaction_metrices_post_invalid(user2, post, comment, reply_comment, reaction, reaction_to_comment):
    #arrange
    #act
    #assert
    assert get_reaction_metrics(1) == {"WOW":1}
