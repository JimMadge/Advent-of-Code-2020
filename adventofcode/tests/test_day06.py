from ..day06 import count_any_affirmative, count_all_affirmative
from textwrap import dedent

test_data = dedent("""\
   abc

   a
   b
   c

   ab
   ac

   a
   a
   a
   a

   b""")


def test_count_any_affirmative():
    assert count_any_affirmative(test_data.split("\n\n")) == 11


def test_count_all_affirmative():
    assert count_all_affirmative(test_data.split("\n\n")) == 6
