class Solution:
	def removeSubFolders(self, folder:list[str]) -> list[str]:
		folder_set = set(folder)
		res = []

		for f in folder:
			res.append(f)
			for i in range(len(f)):
				if f[i] == "/" and f[:i] in folder_set:
					res.pop()
					break

		return res