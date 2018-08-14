import os
import shutil
from dgen.tempdir import tempdir


class TestMake(object):
    def test_creates_empty_tempdir(self):
        tempdir.make()
        assert os.path.exists(tempdir.path)
        assert not os.listdir(tempdir.path)     # assert is-empty
        tempdir.remove()

    def test_removes_existing_tempdir_with_its_content_and_creates_new_one(self):
        tempdir.make()
        os.mkdir(os.path.join(tempdir.path, 'aDir'))
        assert os.listdir(tempdir.path)         # assert is-not-empty

        tempdir.make()
        assert not os.listdir(tempdir.path)     # assert is-empty
        tempdir.remove()

    def test_removes_existing_file_that_has_name_of_tempdir_and_creates_tempdir(self):
        open(tempdir.dirname, 'w').close()
        assert os.path.isfile(tempdir.path)
        tempdir.make()
        assert os.path.isdir(tempdir.path)
        tempdir.remove()


class TestCopyFiles(object):
    def test_copies_files_from_tempdir_to_existing_dir(self):
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

    def test_copies_files_from_tempdir_to_not_existing_dir(self):
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

    def test_copies_files_from_tempdir_to_not_existing_path(self):
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
