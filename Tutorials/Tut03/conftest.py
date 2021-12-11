import pytest


@pytest.fixture(scope="session")
def get_new_user_detail_0():
    email = "ownerofslackrs@unsw.com"
    password = "qwetmn"
    name_first = "Ownerof"
    name_last = "Slackr"

    return email, password, name_first, name_last