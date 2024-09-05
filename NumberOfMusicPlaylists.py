class Solution:
	def numMusicPlaylist(self, n:int, goal:int, k:int) -> int:
		mod = 10**9+7
		dp = {}

		def count(cur_goal, old_songs):
			if cur_goal == 0 and old_songs == n:
				return 1
			if cur_goal == 0 or old_songs > n:
				return 0
			if (cur_goal, old_songs) in dp:
				return dp[(cur_goal, old_songs)]
			#new song
			res = (n - old_songs) * count(cur_goal - 1, old_songs + 1)

			#old song
			if old_songs > k:
				res += (old_songs - k) * count(cur_goal - 1, old_songs)
			dp[(cur_goal, old_songs)] = res % mod
			return dp[(cur_goal, old_songs)]

		return count(goal, 0)