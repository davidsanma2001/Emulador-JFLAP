class PDA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states, stack_alphabet):
        self.states = states
        self.alphabet = alphabet
        self.transitions = {}
        for key, value in transitions.items():
            state, symbol, action = key.split(',')
            state = state.strip()
            symbol = symbol.strip()
            action = action.strip()

            if (state, symbol) not in self.transitions:
                self.transitions[(state, symbol)] = []
            self.transitions[(state, symbol)].append({"action": action, "new_state": value['new_state']})

        self.start_state = start_state
        self.accept_states = accept_states
        self.stack_alphabet = stack_alphabet
        self.stack = []

    def simulate(self, input_string):
        self.stack = []
        current_state = self.start_state
        processed_length = 0

        for symbol in input_string:
            if (current_state, symbol) in self.transitions:
                found_transition = False
                for transition in self.transitions[(current_state, symbol)]:
                    action = transition["action"]
                    new_state = transition["new_state"]

                    if action == 'push':
                        self.stack.append(symbol)
                    elif action == 'pop':
                        if self.stack:
                            self.stack.pop()
                        else:
                            return self._reject(current_state, input_string, processed_length)

                    current_state = new_state
                    found_transition = True

                if not found_transition:
                    return self._reject(current_state, input_string, processed_length)
            else:
                return self._reject(current_state, input_string, processed_length)

            processed_length += 1

        # Aceptación por vaciado de pila
        if not self.stack:
            return self._accept(current_state)
        else:
            return self._reject(current_state, input_string, processed_length)

    def _accept(self, current_state):
        return {
            "final_state": current_state,
            "final_stack": self.stack,
            "result": "accepted",
            "remaining_input": ""
        }

    def _reject(self, current_state, input_string, processed_length):
        remaining_input = input_string[processed_length:]
        return {
            "final_state": current_state,
            "final_stack": self.stack,
            "result": "rejected",
            "remaining_input": remaining_input
        }
