class Solution:
 	def findChampion(self, n:int, edges:list[list[int]]) -> int:
 		incoming = [0] * n

 		for src, dst in edges:
 			incoming[dst] += 1

 		champions = []
 		for i, incoming_count in enumerate(incoming):
 			if not incoming_count:
 				champions.append(i)

 		if len(champions) > 1:
 			return -1

 		return champions[0]
