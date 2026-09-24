from task1 import print_message
import sys

def test_myoutput(capsys):  # or use "capfd" for fd-level
    print_message()
    captured = capsys.readouterr()
    assert captured.out == "Hello World!\n"
    