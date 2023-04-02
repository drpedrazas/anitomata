from maquina_finita import finite_machine

class afd(finite_machine):

    def __init__(self, *args):
       super().__init__(*args)

    def transition_step(self, state, character):
        return self.transition[state][character]

    def process_string(self, string):
        l_string = list(string)
        curr_char = l_string.pop(0)
        curr_state = self.initial
        process_stack = [curr_state]
        while len(l_string) > 0:
            try:
                curr_state = self.transition_step(curr_state, curr_char)
                process_stack.append(curr_state)
                curr_char = l_string.pop(0)
            except KeyError:
                return False, process_stack
        return curr_state in self.final, process_stack
