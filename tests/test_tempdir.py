import os
from dgen.tempdir import tempdir


def test_tempdir_make_creates_empty_temp_dir():
    tempdir.make()
    assert os.path.exists(tempdir.path)
    assert not os.listdir(tempdir.path)     # assert is-empty
    tempdir.remove()


def test_tempdir_make_removes_existing_temp_dir_with_content_and_creates_new_one():
    tempdir.make()
    os.mkdir(os.path.join(tempdir.path, 'aDir'))
    assert os.listdir(tempdir.path)         # assert is-not-empty

    tempdir.make()
    assert not os.listdir(tempdir.path)     # assert is-empty
    tempdir.remove()


def test_tempdir_make_removes_existing_temp_file_and_creates_new_dir():
    with open(tempdir.dirname, 'w'):
        pass
    assert os.path.isfile(tempdir.path)
    tempdir.make()
    assert os.path.isdir(tempdir.path)
    tempdir.remove()
