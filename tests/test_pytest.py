import pytest
import hanger

def test_fill_base_from_file():
    f=open("test.txt", "w")
    test_text = ['test1', 'test2', 'test3', 'test4', 'test5']
    for word in test_text:
        f.write("{}\n".format(word))
    f.close()
    empty = hanger.fill_base_from_file("test.txt")
    assert empty == test_text

def test_init():
    test_base = hanger.fill_base_from_file("test.txt")
    test_bot = hanger.AI(test_base, 4)
    assert test_bot.attempts_count == hanger.attempts
    assert test_bot.wb == test_base

def test_check(test_bot):
    assert test_bot.check_letter("t")
    assert test_bot.check_letter("d")
    assert test_bot.attempts_count < 4

def test_print(test_bot):
    assert test_bot.print_word()
    assert test_bot.print_word("t")
    assert test_bot.print_word("d")
    assert test_bot.current_word == "t__t"