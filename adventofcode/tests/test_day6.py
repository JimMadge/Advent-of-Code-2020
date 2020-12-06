from ..day6 import count_groups_affirmative, count_groups_all_affirmative
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


def test_count_groups_affirmative():
    assert sum(count_groups_affirmative(test_data)) == 11


def test_count_groups_all_affirmative():
    assert sum(count_groups_all_affirmative(test_data)) == 6
    print(count_groups_all_affirmative(test_data))
    assert 0
