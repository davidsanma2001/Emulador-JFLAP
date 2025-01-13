class NFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = {}

        for key, value in transitions.items():
            state, symbol = key.split(',')
            for new_state in value:
                if (state.strip(), symbol.strip()) not in self.transitions:
                    self.transitions[(state.strip(), symbol.strip())] = []
                self.transitions[(state.strip(), symbol.strip())].append(new_state['new_state'])

        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)

        while stack:
            state = stack.pop()
            for next_state in self.transitions.get((state, ''), []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)

        return closure

    def move(self, states, symbol):
        next_states = set()
        for state in states:
            next_states.update(self.transitions.get((state, symbol), []))
        return next_states

    def simulate(self, input_string):
        current_states = self.epsilon_closure({self.start_state})

        for symbol in input_string:
            current_states = self.epsilon_closure(self.move(current_states, symbol))

        if any(state in self.accept_states for state in current_states):
            return current_states, 'accepted'
        else:
            return current_states, 'rejected'