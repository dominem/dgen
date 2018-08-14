import os
import shutil
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


def test_tempdir_copy_files_copies_files_from_tempdir_to_existing_dir():
    tempdir.make()

    file1 = 'file1'
    file2 = 'file2'
    open(os.path.join(tempdir.path, file1), 'w').close()
    open(os.path.join(tempdir.path, file2), 'w').close()

    dst_dir = os.path.abspath('dst_dir')
    os.mkdir(dst_dir)

    tempdir.copy_files([file1, file2], dst_dir)

    assert os.path.isfile(os.path.join(dst_dir, file1))
    assert os.path.isfile(os.path.join(dst_dir, file2))

    shutil.rmtree(dst_dir)
    tempdir.remove()


def test_tempdir_copy_files_copies_files_from_tempdir_to_not_existing_dir():
    tempdir.make()

    file1 = 'file1'
    file2 = 'file2'
    open(os.path.join(tempdir.path, file1), 'w').close()
    open(os.path.join(tempdir.path, file2), 'w').close()

    dst_dir = os.path.abspath('dst_dir')

    tempdir.copy_files([file1, file2], dst_dir)

    assert os.path.isfile(os.path.join(dst_dir, file1))
    assert os.path.isfile(os.path.join(dst_dir, file2))

    shutil.rmtree(dst_dir)
    tempdir.remove()


def test_tempdir_copy_files_copies_files_from_tempdir_to_not_existing_path():
    tempdir.make()

    file1 = 'file1'
    file2 = 'file2'
    open(os.path.join(tempdir.path, file1), 'w').close()
    open(os.path.join(tempdir.path, file2), 'w').close()

    dst_dir_parent = os.path.abspath('dst_dir_parent')
    dst_dir = os.path.join(dst_dir_parent, 'dst_dir')

    tempdir.copy_files([file1, file2], dst_dir)

    assert os.path.isfile(os.path.join(dst_dir, file1))
    assert os.path.isfile(os.path.join(dst_dir, file2))

    shutil.rmtree(dst_dir_parent)
    tempdir.remove()
