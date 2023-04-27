from pytest_voluptuous import S

from schemas.cats import cats_list


def test_abyssinian_cat(ninja_cats):
    response = ninja_cats.get(url="", params={"name": "abyssinian"})

    assert S(cats_list) == response.json()