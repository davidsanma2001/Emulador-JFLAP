class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = {}

        for key, value in transitions.items():
            state, symbol = key.strip('()').split(',')
            self.transitions[(state.strip(), symbol.strip())] = value['new_state']

        self.start_state = start_state
        self.accept_states = accept_states

    def simulate(self, input_string):
        current_state = self.start_state
        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                current_state = self.transitions[(current_state, symbol)]
            else:
                return current_state, False  
        
        if current_state in self.accept_states:
            return current_state, 'accepted'  
        else:
            return current_state, 'rejected'  

