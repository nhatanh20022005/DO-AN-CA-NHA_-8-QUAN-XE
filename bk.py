
import itertools

class BK:
    def __init__(self, N=8):
        self.N = N
        self.variables = [f"X{i}" for i in range(self.N)]
        self.domain_all = [(r, c) for r in range(self.N) for c in range(self.N)]
        self.domains = {var: list(self.domain_all) for var in self.variables}

    def kiem_tra_rang_buoc(self, assignments):
        values = list(assignments.values())

        if len(values) != len(set(values)):
            return False

        for (r1, c1), (r2, c2) in itertools.combinations(values, 2):
            if r1 == r2 or c1 == c2:
                return False
        return True

    def backtracking(self, assignments, variables, domains):
        if len(assignments) == len(variables):
            return assignments

        var = variables[len(assignments)]
        for value in domains[var]:
            new_assignments = assignments.copy()
            new_assignments[var] = value

            if self.kiem_tra_rang_buoc(new_assignments):
                result = self.backtracking(new_assignments, variables, domains)
                if result is not None:
                    return result
        return None

    def tu_dong_CSP(self):
        variables = self.variables
        domains = self.domains

        stack = [({}, 0)]
        while stack:
            assignments, idx = stack.pop()
            if idx == len(variables):
                yield list(assignments.values())  
                return

            var = variables[idx]
            for value in domains[var]:
                new_assign = assignments.copy()
                new_assign[var] = value

                if self.kiem_tra_rang_buoc(new_assign):
                    yield list(new_assign.values()) 
                    stack.append((new_assign, idx + 1))
