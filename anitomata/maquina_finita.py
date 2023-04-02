class finite_machine():

    def __init__(self, states, initial, alphabet, final, transition):
        self.states = states
        self.alphabet = alphabet
        self.final = final
        self.transition = transition
        self.initial = initial

    def get_states(self):
        return self.states

    def get_final(self):
        return self.final

    def add_state(self, state):
        self.states.add(state)

    def add_final(self, n_final):
        self.final.add(n_final)

    def rm_state(self, state):
        self.states.remove(state)
        if state in self.final:
            self.final.remove(state)

    def rm_final(self, state):
        self.final.remove(state)

    def add_transition(self, *n_tran):
        self.transition[n_tran[:-1]] = n_tran[-1]

