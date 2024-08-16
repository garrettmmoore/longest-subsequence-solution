from typing import List


class Solution:
    def find_longest_increasing_subsequence(self, seq: List[int]) -> List[int]:
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
                if seq[i] > seq[j] and longest_lengths[j] + 1 > longest_lengths[i]:
                    longest_lengths[i] = longest_lengths[j] + 1
                    prev_indices[i] = j

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
