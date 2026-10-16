import pytest


@pytest.fixture
def posts_url():
    return "https://jsonplaceholder.typicode.com/posts"


@pytest.fixture
def post_by_id_url():
    return "https://jsonplaceholder.typicode.com/posts/1"
