# https://leetcode.com/problems/restore-ip-addresses/#/description


from itertools import product


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(segment):
            return (0 < int(segment) < 256 and segment[0] != '0') or segment == '0'

        len_map = {4: {1}, 5: {1, 2}, 11: {2, 3}, 12: {3}}
        product_vals = len_map.get(len(s), {1, 2, 3})
        results = set()
        for segment_lengths in product(product_vals, repeat=4):
            if sum(segment_lengths) != len(s):
                continue
            result = []
            segment_offsets = [sum(segment_lengths[:i]) for i in range(0, 4)]
            for start, length in zip(segment_offsets, segment_lengths):
                seg = s[start:start + length]
                if not is_valid(seg):
                    result = []
                    break
                result.append(seg)
            if result:
                results.add('.'.join(result))
        return list(results)
