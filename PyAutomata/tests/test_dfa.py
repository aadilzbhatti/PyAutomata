from unittest import TestCase
from .. import PyAutomata

class TestDFA(TestCase):
	def test_add_state(self):
		d = PyAutomata.DFA()