import dfa

"""
Initializing a DFA.
"""
d = dfa.DFA()

"""
Add a set of symbols to the alphabet of the DFA. You can 
also add individual symbols.
"""
d.add_alphabet(1, 0)

"""
Add a set of states to the DFA. You can also add individual states.
"""
d.add_states('A', 'BEF', 'CF', 'DF', 'F', 'B', 'C', 'D')

"""
Add an accepting state. If the state is already in the DFA, 
the state is marked as an accepting state.
"""
d.add_accepting_state('A')
d.add_accepting_state('BEF')
d.add_accepting_state('DF')
d.add_accepting_state('F')
d.add_accepting_state('D')
d.add_accepting_state('CF')

"""
By default, PyAutomata sets the start state to a state called 'q0'. 
You can change this by calling the following method.
"""
d.start_state('A')

"""
By default, PyAutomata does not include a rejecting state in each DFA.
You can change this by calling the following method.
"""
d.add_reject_state('ø')

"""
You can add transitions between states by calling the following method.
"""
d.add_transition('A', 0, 'ø')
d.add_transition('A', 1, 'BEF')
d.add_transition('BEF', 1, 'ø')
d.add_transition('BEF', 0, 'CF')
d.add_transition('CF', 1, 'ø')
d.add_transition('CF', 0, 'DF')
d.add_transition('DF', 0, 'F')
d.add_transition('DF', 1, 'B')
d.add_transition('F', 1, 'ø')
d.add_transition('B', 1, 'ø')
d.add_transition('B', 0, 'C')
d.add_transition('C', 1, 'ø')
d.add_transition('C', 0, 'D')
d.add_transition('D', 0, 'ø')
d.add_transition('D', 1, 'B')

"""
You can add self transitions by calling the following method.
You can also add a self transition across the entire alphabet
of the DFA.
"""
d.add_self_transition('F', 0)

"""
Print the contents of the DFA. This shows:
Q: The set of states in DFA
∑: The alphabet, or set of symbols in DFA
∂: The transition function of the DFA
s: The start state of the DFA
F: The set of accepting states in the DFA
"""
print(d)

"""
Check if a string is in the language specified by the DFA.
"""
print(d.parse('100' * 100))