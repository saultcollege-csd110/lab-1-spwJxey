# WARNING! WARNING! WARNING!
# Feel free to look, but do not touch!

import pytest
from src.lab1_question1 import main

def test_question1(capsys):
    main()
    out, err = capsys.readouterr()
    assert out == "4\nHello, world!\n", "Script prints two lines of text: '4' and 'Hello, world!'"
