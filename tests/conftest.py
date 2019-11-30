import pytest


@pytest.fixture()
def mocked_os(mocker):
    return mocker.patch("src.extract_flashes.os")


@pytest.fixture()
def mocked_xarray(mocker):
    return mocker.patch("src.extract_flashes.xr")

