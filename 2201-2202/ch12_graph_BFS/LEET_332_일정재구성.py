from copy import deepcopy
from typing import List


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        ticket_dic = {}
        result = []

        for F, T in sorted(tickets, reverse=True):
            if F in ticket_dic:
                ticket_dic[F].append(T)
            else:
                ticket_dic[F] = [T]

        def dfs(node):
            if node not in ticket_dic:
                result.append(node)
                return
            while ticket_dic[node]:
                dfs(ticket_dic[node].pop())
            result.append(node)

        dfs("JFK")

        return result[::-1]


s = Solution()
print(s.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
print(s.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))

# # runtime error
# class Solution:
#     def findItinerary(self, tickets: List[List[str]]) -> List[str]:
#         ticket_dic = {}
#         max = 0
#         result = []
#         start = "JFK"
#
#         for ticket in tickets:
#             if ticket[0] in ticket_dic:
#                 ticket_dic[ticket[0]] += [ticket[1]]
#                 ticket_dic[ticket[0]] = sorted(ticket_dic[ticket[0]])
#                 max += 1
#             else:
#                 ticket_dic[ticket[0]] = [ticket[1]]
#                 max += 1
#
#         def dfs(node, remain_tickets, path):
#             if node not in remain_tickets and len(path) - 1 == max:
#                 result.append(path)
#                 return
#             elif node not in remain_tickets:
#                 return
#             elif len(remain_tickets[node]) == 0 and len(path) - 1 == max:
#                 result.append(path)
#                 return
#             elif len(remain_tickets[node]) == 0 and len(path) - 1 < max:
#                 return
#
#             for next in remain_tickets[node]:
#                 remained = deepcopy(remain_tickets)
#                 remained[node].remove(next)
#                 dfs(next, remained, path + [next])
#
#         dfs(start, ticket_dic, ['JFK'])
#
#         return result[0]