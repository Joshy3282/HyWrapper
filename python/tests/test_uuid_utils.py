from hywrapper.uuid_utils import UuidUtils


def test_undash():
    dashed = "550e8400-e29b-41d4-a716-446655440000"
    undashed = "550e8400e29b41d4a716446655440000"
    assert UuidUtils.undash(dashed) == undashed
    assert UuidUtils.undash(undashed) == undashed


def test_dash():
    dashed = "550e8400-e29b-41d4-a716-446655440000"
    undashed = "550e8400e29b41d4a716446655440000"
    assert UuidUtils.dash(undashed) == dashed
    assert UuidUtils.dash(dashed) == dashed


def test_is_valid():
    dashed = "550e8400-e29b-41d4-a716-446655440000"
    undashed = "550e8400e29b41d4a716446655440000"
    assert UuidUtils.is_valid(dashed) is True
    assert UuidUtils.is_valid(undashed) is True
    assert UuidUtils.is_valid("invalid-uuid") is False
    assert UuidUtils.is_valid("550e8400-e29b-41d4-a716-44665544000g") is False
