from unittest import TestCase


class TestSolution(TestCase):
    def test_solution(self):
        from build import solution

        x = [45, 38, 52, 48, 25, 39, 51, 46, 55, 46]
        y = [34, 22, 15, 27, 37, 41, 24, 19, 26, 36]

        self.assertTrue(solution(x, y, 0.05))