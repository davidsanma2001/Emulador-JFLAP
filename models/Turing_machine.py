class Turing_machine:
    def __init__(self, states, input_string, alphabet, head, transitions, start_state, accept_states):
        self.states = states
        self.input_string = list(input_string)        
        self.alphabet = alphabet
        self.head = head
        self.transitions = {}
        for key, value in transitions.items():
            state, code = key.strip('()').split(',')
            state = state.strip()
            code = code.strip()

            new_state = value['new_state'].strip()
            write_code = value['write_code'].strip()
            action = value['action'].strip()

            self.transitions[(state, code)] = (new_state, write_code, action)

        self.start_state = start_state
        self.accept_states = accept_states

    def step(self):
        try:
            read_code = self.input_string[self.head]
            transition = self.transitions.get((self.start_state, read_code))
            if transition:
                new_state, write_code, action = transition
                self.start_state = new_state
                self.input_string[self.head] = write_code

                if action == 'L':
                    self.head -= 1
                elif action == 'R':
                    self.head += 1

                return True
            else:
                return False
        except IndexError:
            return False

    def simulate(self):
        self.head = 0

        while True:
            if self.head < 0 or self.head >= len(self.input_string):
                break

            if not self.step():
                break

        if self.start_state in self.accept_states:
            result = 'accepted'
        else:
            result = 'rejected'

        return self.start_state, self.head, ''.join(self.input_string), result
