import pytest

from src.extract_flashes import read_glm_file


@pytest.mark.parametrize("input_file", ["test.n", "test.h5", "test.nc4"])
def test_incorrect_glm_extension_caught(input_file):
    with pytest.raises(ValueError):
        read_glm_file(input_file)


def test_glm_file_not_found(mocked_os):
    mocked_os.path.exists.return_value = "False"

    with pytest.raises(FileNotFoundError):
        read_glm_file("test.nc")


def test_data_ingest_call(mocked_os, mocked_xarray):
    mocked_os.path.exists.return_value = "True"
    read_glm_file("test.nc")
    assert mocked_xarray.called_once_with("test.nc")
