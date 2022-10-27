import unittest

from mysutils.file import remove_files
from mysutils.git import GitMonitor


class MyTestCase(unittest.TestCase):
    def test_something(self):
        monitor = GitMonitor(self.update,
                             'git-test',
                             'https://github.com/jmgomezsoriano/mysmallutils.git',
                             'test-branch')
        monitor.monitor(False)

    def update(self, *files: str) -> None:
        self.assertTupleEqual(files, ('test3.txt', 'test4.txt'))


if __name__ == '__main__':
    unittest.main()
