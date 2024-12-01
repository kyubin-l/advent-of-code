from functools import lru_cache
from math import lcm
from typing import Any
from pathlib import Path

import re
from base_solution import BaseSolution


class Node:
    _instances: dict[str, "Node"] = {}

    def __init__(self, name: str) -> None:
        self.name = name
        self.left: "Node" | None = None
        self.right: "Node" | None = None

    @classmethod
    def get(cls, name: str) -> "Node":
        if name in cls._instances:
            return cls._instances[name]
        new_instance = cls(name)
        cls._instances[name] = new_instance
        return new_instance

    @classmethod
    def clear(cls) -> None:
        cls._instances: dict[str, "Node"] = {}


class Solution(BaseSolution):
    def load(self, part: int = 1) -> str:
        if part == 2:
            filename = Path(str(self.filename).replace("q8_sample", "q8_sample_2"))
        else:
            filename = self.filename
        with open(filename) as f:
            directions: str = f.readline().strip()
            f.readline()
            for line in f.readlines():
                names = re.findall(r"[1-9|A-Z]+", line)
                node = Node.get(names[0])
                node.left = Node.get(names[1])
                node.right = Node.get(names[2])

        return directions

    @lru_cache(maxsize=None)
    def _traverse(self, directions: str, start: Node) -> Node:
        cur = start
        for d in directions:
            if d == "R":
                cur: Node = cur.right  # type: ignore
            elif d == "L":
                cur: Node = cur.left  # type: ignore
        return cur

    def part_one(self) -> int:
        directions = self.load()
        cur = Node.get("AAA")
        count = 0
        while cur.name != "ZZZ":
            cur = self._traverse(directions, cur)
            count += 1
        return count * len(directions)

    def directions_iterator(self, directions: str) -> Any:
        for d in directions:
            yield d

    def part_one_test(self) -> int:
        directions, cur = self.load(part=2)
        count = 0
        while cur.name != "ZZZ":
            for d in directions:
                cur = self._traverse(d, cur)
                count += 1
                if cur.name == "ZZZ":
                    break
        return count

    def part_two(self) -> int:
        """
        Only discovered that the Zs come in fixed interval for each node in testing.
        Not sure how to do this fully algorithmically without first inspecting the data
        """
        directions = self.load(part=2)
        end_in_a = [v for k, v in Node._instances.items() if k.endswith("A")]
        counts: list[int] = []
        print([n.name for n in end_in_a])
        # Traverse with one node, if that ends in Z, do that count for the next, etc

        for node in end_in_a:
            count = 0
            print(node.name)
            while not node.name.endswith("Z"):
                for d in directions:
                    node = self._traverse(d, node)
                    count += 1
                    if node.name.endswith("Z"):
                        counts.append(count)
                        print(count)
                        break

        return lcm(*counts)


if __name__ == "__main__":
    test_sol = Solution(8, test=True)
    sol = Solution(8, test=False)

    assert test_sol.part_one() == 2
    Node.clear()
    print(sol.part_one())
    Node.clear()

    # print(test_sol.part_two())
    Node.clear()
    assert test_sol.part_two() == 6
    # print(test_sol.part_two())
    Node.clear()
    print(sol.part_two())
