from utils.base_solution import BaseSolution

Q_NUM = 12
YEAR = 2021


class Cave:
    caves = {}

    def __init__(self, name: str, large: bool):
        self.name = name
        self.large = large
        self.connected_caves = set()
        Cave.caves[self.name] = self


class Solution(BaseSolution):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def load(self):
        def make_or_get_cave(name):
            if name in Cave.caves:
                return Cave.caves[name]
            if name.upper() == name:
                large = True
            else:
                large = False
            new_cave = Cave(name, large)
            return new_cave

        with open(self.filename) as f:
            for line in f.readlines():
                c1, c2 = line.rstrip().split("-")
                c1 = make_or_get_cave(c1)
                c2 = make_or_get_cave(c2)
                c1.connected_caves.add(c2)
                c2.connected_caves.add(c1)

    def solve_part_one(self):
        all_routes = []
        current = [Cave.caves["start"]]

        def travel(current_route):
            cave = current_route[-1]
            for connected_cave in cave.connected_caves:
                new_route = current_route.copy()
                if connected_cave.name == "start":
                    continue
                if connected_cave.name == "end":
                    new_route.append(connected_cave)
                    all_routes.append(new_route)
                    continue
                if (connected_cave.large == False) and (
                    connected_cave in current_route
                ):
                    continue
                new_route.append(connected_cave)
                travel(new_route)

        travel(current)

        return len(all_routes)

    def solve_part_two(self):
        all_routes = []
        current = [Cave.caves["start"]]

        def small_visit_allowed(route, cave):
            """
            Checks if the small cave 'cave' can be visited in the current route
            """
            if cave not in route:
                return True
            small_caves = [cave for cave in route if cave.large == False]

            if len(small_caves) == len(set(small_caves)):
                # no double small cave vists, so can visit this cave again
                return True
            return False

        def travel(current_route):
            cave = current_route[-1]
            for connected_cave in cave.connected_caves:
                new_route = current_route.copy()
                if connected_cave.name == "start":
                    continue
                if connected_cave.name == "end":
                    new_route.append(connected_cave)
                    all_routes.append(new_route)
                    continue
                if connected_cave.large == False:
                    if not small_visit_allowed(new_route, connected_cave):
                        continue
                new_route.append(connected_cave)
                travel(new_route)

        travel(current)

        # all_routes.sort(key=len)

        # for route in all_routes[-20:]:
        #     print([cave.name for cave in route])

        return len(all_routes)


if __name__ == "__main__":
    sol = Solution(Q_NUM, YEAR)
    sol.load()
    # for name, cave in Cave.caves.items():
    #     print(name, cave.large)

    print(sol.solve_part_one())
    sol.load()
    print(sol.solve_part_two())
