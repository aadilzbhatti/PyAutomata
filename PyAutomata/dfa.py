class DFA:
	def __init__(self):
		self.states = ['q0']
		self.sigma = []
		self.transition = {'q0': {}}
		self.start = 'q0'
		self.accepting = []
		self.reject = None

	def __str__(self):
		ret = 'Q: {' + ', '.join(self.states) + '}\n'
		ret += '∑: {' + ', '.join([str(self.sigma[i]) for i in range(len(self.sigma))]) + '}\n'
		ret += '∂: \n{\n'
		for i in range(len(self.states)):
			for j in range(len(self.sigma)):
				ret += '\t∂(' + self.states[i] + ', ' + str(self.sigma[j]) + ') = ' 
				ret += str(self.transition[self.states[i]][self.sigma[j]])
				ret += '\n'
		ret += '}\n'
		ret += 's: ' + self.start + '\n'
		ret += 'F: {' + ', '.join(self.accepting) + '}'
		return ret
 
	def add_state(self, state):
		if state not in self.states:
			self.states.append(state)
			self.transition[state] = {}
			for i in range(len(self.sigma)):
				for j in range(len(self.states)):
					self.transition[self.states[j]][self.sigma[i]] = ''

	def add_states(self, states):
		for state in states:
			self.add_state(state)

	def add_transition(self, state, symbol, output):
		self.transition[state][symbol] = output

	def add_self_transition(self, state, symbol):
		for i in self.sigma:
			self.transition[state][i] = state

	def add_symbol(self, symbol):
		self.sigma.append(symbol)

	def add_alphabet(self, alphabet):
		for symbol in alphabet:
			self.add_symbol(symbol)

	def add_accepting_state(self, state):
		self.accepting.append(state)
		self.add_state(state)

	def add_reject_state(self, state='reject'):
		self.add_state(state)
		self.reject = state
		self.add_self_transition(self.reject, 1)
		self.add_self_transition(self.reject, 0)

	def self_transition_all(self, state):
		for symbol in alphabet:
			self.add_self_transition(state, symbol)

d = DFA()
d.add_alphabet([1, 0])

d.add_states(['q1', 'reject', 'accept'])

d.add_accepting_state('accept')

d.add_transition('q0', 1, 'q1')
d.add_transition('q1', 1, 'accept')
d.add_self_transition('q0', 0)
d.add_transition('q1', 0, 'q0')
d.add_self_transition('accept', 1)
d.add_self_transition('accept', 0)
d.add_self_transition('reject', 1)
d.add_self_transition('reject', 0)

print(d)