class NFA_DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def epsilon_closure(self, states):
        closure = set(states)
        stack = list(states)
        while stack:
            current = stack.pop()
            for next_state in self.transitions.get(f"{current},lambda", []):
                if next_state not in closure:
                    closure.add(next_state)
                    stack.append(next_state)
        return closure

    def move(self, states, symbol):
        next_states = set()
        for state in states:
            next_states.update(self.transitions.get(f"{state},{symbol}", []))
        return next_states

    def to_dfa(self):
        dfa_states = []
        dfa_transitions = {}
        empty_set = "None"  # Representación del conjunto vacío como "None"
        dfa_states.append(empty_set)

        # Aplicamos el cierre épsilon al estado inicial
        dfa_start_state = tuple(sorted(self.epsilon_closure([self.start_state])))
        dfa_states.append(dfa_start_state)

        unmarked_states = [dfa_start_state]

        while unmarked_states:
            current = unmarked_states.pop()
            for symbol in self.alphabet:
                if symbol == "lambda":
                    continue
                next_states = self.move(current, symbol)
                if next_states:
                    # Aplicamos el cierre épsilon a los estados alcanzables
                    next_states = tuple(sorted(self.epsilon_closure(next_states)))
                else:
                    next_states = empty_set  # Si no hay estados alcanzables, usamos "None"

                # Registrar la transición
                dfa_transitions[(current, symbol)] = next_states

                if next_states not in dfa_states:
                    dfa_states.append(next_states)
                    if next_states != empty_set:  # No agregar "None" a la lista de no marcados
                        unmarked_states.append(next_states)

        # Añadir transiciones para el conjunto vacío
        for symbol in self.alphabet:
            if symbol != "lambda":
                dfa_transitions[(empty_set, symbol)] = empty_set

        # Filtrar los estados de aceptación
        dfa_accept_states = [
            state for state in dfa_states if state != empty_set and set(state).intersection(self.accept_states)
        ]

        # Formato de salida ajustado
        return {
            "states": [
                ', '.join(state) if state != empty_set else empty_set for state in dfa_states
            ],
            "alphabet": [symbol for symbol in self.alphabet if symbol != "lambda"],
            "transitions": {
                f"{', '.join(key[0]) if key[0] != empty_set else empty_set} - {key[1]}": (
                    f"{', '.join(value)}" if value != empty_set else empty_set
                )
                for key, value in dfa_transitions.items()
            },
            "start_state": ', '.join(dfa_start_state) if dfa_start_state != empty_set else empty_set,
            "accept_states": [
                ', '.join(state) if state != empty_set else empty_set for state in dfa_accept_states
            ]
        }


