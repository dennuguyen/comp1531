import pytest


def test_example(get_new_user_detail_0):
    email, password, name_first, name_last = get_new_user_detail_0
    assert email == "ownerofslackrs@unsw.com"
    assert password == "qwetmn"
    assert name_first == "Ownerof"
    assert name_last == "Slackr"
