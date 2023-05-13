import collections

def group_anagrams(strs):
    anagrams = collections.defaultdict(list)

    for str in strs:
        anagrams["".join(sorted(str))].append(str)

    print(list(anagrams.values()))


group_anagrams(["eat","tea","tan","ate","nat","bat"])