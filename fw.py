
import itertools
import copy

def kiem_tra_rang_buoc(assignments):
    values = list(assignments.values())
    if len(values) != len(set(values)):
        return False
    for (r1, c1), (r2, c2) in itertools.combinations(values, 2):
        if r1 == r2 or c1 == c2:
            return False
    return True

def tu_dong_CSP_forward_checking_generator():
    variables = [f"X{i}" for i in range(8)]
    domain_all = [(r, c) for r in range(8) for c in range(8)]
    domains = {var: list(domain_all) for var in variables}

    stack = [({}, domains, 0)]
    while stack:
        assignments, doms, idx = stack.pop()

        if idx == len(variables):
            yield list(assignments.values())
            return

        var = variables[idx]
        for value in doms[var]:
            new_assign = assignments.copy()
            new_assign[var] = value

            if kiem_tra_rang_buoc(new_assign):
    
                new_doms = copy.deepcopy(doms)
                r_val, c_val = value
                for other_var in variables[idx + 1:]:
                    new_doms[other_var] = [
                        (r, c)
                        for (r, c) in new_doms[other_var]
                        if r != r_val and c != c_val
                    ]
                yield list(new_assign.values())  
                stack.append((new_assign, new_doms, idx + 1))

class FW:
    def __init__(self):
        self.variables = [f"X{i}" for i in range(8)]
        self.generator_instance = None

    def generator(self):
        self.generator_instance = tu_dong_CSP_forward_checking_generator()
        return self.generator_instance
