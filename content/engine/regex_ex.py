# 2 engines: NFA/DFA       RegEx-Art
# FA -> Finite Automation

class Regex:
    """
    Can only support a-z
    """
    def __init__(self):
        self.fsm = []

    def _char_to_int(self, char):
        """
        Returns 0 for a, 1 for b, 2 for c, ... 25 for z
        """
        return ord(char) - 97

    def create_state(self, default_value=0, step=1):
        return [(default_value, step)] * 26

    def compile(self, regex_string):
        self.fsm = []
        # add state 0 as default failure state
        self.fsm.append(self.create_state())

        prev = None
        iter_ = iter(regex_string)
        for char in iter_:
            next_valid_state = len(self.fsm) + 1
            if char == ".":
                self.fsm.append(self.create_state(next_valid_state))
            elif char == "*":
                # modify last state
                n = len(self.fsm)
                self.fsm[-1] = self.create_state(n, step=0)
                self.fsm[-1][self._char_to_int(prev)] = (n -1, 1)
            elif char == "[":
                allow = []
                try:
                    while (next_ := next(iter_)) != "]":
                        allow.append(next_)
                except StopIteration:
                    raise Exception("Invalid Regex. Expected ]")
                state = self.create_state()
                for c in allow:
                    state[self._char_to_int(c)] = next_valid_state
                self.fsm.append(state)
            else:
                state = self.create_state()
                # add valid transition
                state[self._char_to_int(char)] = next_valid_state, 1
                self.fsm.append(state)
            prev = char

    def match(self, text):
        # start from state 1, fail state is 0
        current_state = 1
        current_position = 0
        while True:
            try: 
                input_char = text[current_position]
                current_state, step = self.fsm[current_state][self._char_to_int(input_char)]
                if current_state == 0:
                    return False
                current_position += step

            except IndexError:
                return current_state == len(self.fsm)


    def __str__(self):
        result = "  States\n"
        result += "  " + " ".join(str(i) for i in range(len(self.fsm))) + "\n"
        result += "--" * 2 * len(self.fsm) + "\n"
        for i, row in enumerate(zip(*self.fsm), start=97):
            result += chr(i) + "|" + " ".join(str(x) for x in row) + "\n"
        return result


    __repr__ = __str__

r = Regex()
r.compile("ab*c")
r.match("abc")
