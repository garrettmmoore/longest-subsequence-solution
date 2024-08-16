import unittest

from src.LongestSubsequence import Solution


class TestLongestSubsequence(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_empty_list(self):
        self.assertEqual(self.solution.find_longest_increasing_subsequence([]), [])

    def test_single_element_list(self):
        self.assertEqual(self.solution.find_longest_increasing_subsequence([1]), [1])

    def test_two_element_increasing_list(self):
        self.assertEqual(
            self.solution.find_longest_increasing_subsequence([1, 2]), [1, 2]
        )

    def test_two_element_decreasing_list(self):
        self.assertEqual(self.solution.find_longest_increasing_subsequence([2, 1]), [2])

    def test_multi_element_increasing_list(self):
        self.assertEqual(
            self.solution.find_longest_increasing_subsequence([1, 2, 3, 4, 5]),
            [1, 2, 3, 4, 5],
        )

    def test_multi_element_decreasing_list(self):
        self.assertEqual(
            self.solution.find_longest_increasing_subsequence([5, 4, 3, 2, 1]), [5]
        )

    def test_multi_element_longest_subsequence_list_with_gap(self):
        self.assertEqual(
            self.solution.find_longest_increasing_subsequence([0, 1, 5, 2, 3]),
            [0, 1, 2, 3],
        )

    def test_multi_element_longest_subsequence_in_the_beginning(self):
        self.assertEqual(
            self.solution.find_longest_increasing_subsequence([1, 2, 3, 1]), [1, 2, 3]
        )


if __name__ == "__main__":
    unittest.main()
