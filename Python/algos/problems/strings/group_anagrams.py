# https://leetcode.com/problems/group-anagrams/

def group_anagrams(arr):
    ang_dict = {}

    for i in arr:
        sorted_str = ''.join(sorted(i))
        if sorted_str in ang_dict:
            ang_dict[sorted_str].append(i)
        else:
            ang_dict[sorted_str] = [i]

    return list(ang_dict.values())


print(group_anagrams(["eat", "tea", "tan", "nat"]))
print(group_anagrams(["cat", "dog", "tac", "edoc", "god", "tacact",
              "act", "code", "deno", "node", "ocde", "done", "catcat"]))
