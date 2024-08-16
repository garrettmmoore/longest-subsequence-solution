from typing import List


class Solution:
    def find_longest_increasing_subsequence_3(self, seq: List[int]) -> List[int]:
        """
        Given a sequence of integers, find the longest increasing subsequence.

        :param seq: A list of integers representing the input sequence.
        :return: A list of integers representing the longest increasing
        subsequence in the input sequence.
        """
        # Base case check to ensure the sequence is not empty
        if not seq:
            return []

        # Get the size of the input sequence
        seq_size = len(seq)

        # Init list to store the length of each longest increasing subsequence
        longest_lengths = [1] * seq_size

        # Init list to store the prev index of each longest increasing subsequence
        prev_indices = [0] * seq_size

        # Iterate through every subsequence to compute the longest increasing
        # lengths list and previous indices list.
        for i in range(seq_size):
            for j in range(i):
                print("\n------Beginning------")
                print("i:", i)
                print("j:", j)
                print("seq[i]:", seq[i])
                print("seq[j]:", seq[j])
                print("longest_lengths[j]+1: ", longest_lengths[j] + 1)
                print("longest_lengths[i]: ", longest_lengths[i])
                if seq[i] > seq[j] and longest_lengths[j] + 1 > longest_lengths[i]:
                    longest_lengths[i] = longest_lengths[j] + 1
                    print("------------")
                    print("modified longest_lengths[i]: ", longest_lengths[i])
                    print("------------")
                    prev_indices[i] = j
                print("current longest length", longest_lengths[i])
                print("current longest lengths:", longest_lengths)

        # Get the index of the longest increasing subsequence
        longest_index = longest_lengths.index(max(longest_lengths))

        # Get the length of the longest increasing subsequence
        longest_length = longest_lengths[longest_index]

        # Init a list to store the longest increasing subsequence result
        longest_subseq = [0] * longest_length

        # Build the longest increasing subsequence list
        for i in reversed(range(longest_length)):
            longest_subseq[i] = seq[longest_index]
            longest_index = prev_indices[longest_index]

        return longest_subseq


solution = Solution()


def run_tests(input_seq: List[int], expected_seq: List[int], test_number: int):
    print(
        f"TEST {test_number}:",
        f"\nInput:{input_seq} ",
        f"\nResult:{solution.find_longest_increasing_subsequence_3(input_seq)}",
        f"\nExpected: {expected_seq}",
        "\n------------",
    )


run_tests([6, 1, 5, 2, 3], [1, 2, 3], 1)
run_tests([5, 4, 3, 2, 1], [5], 2)
