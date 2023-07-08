# def counter(s):  # O(n**2)
#     for i in set(s):
#         count = 0
#         for j in s:
#             if i == j:
#                 count += 1
#         print(i, count)
#

def counter(s):  # O(n)
    syms = {}
    for i in s:
        syms[i] = syms.get(i, 0) + 1
    for i, count in syms.items():
        print(i, count)


s = 'abaaabbba'

counter(s)
