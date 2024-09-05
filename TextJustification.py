class Solution:
	def fullJustify(self, words:list[str], maxWidth:int) -> list[str]:
		res = []
		line, length = [], 0
		i = 0

		while i < len(words):
			#line is complete
			if length + len(line) + len(words[i]) > maxWidth:
				extra_space = maxWidth - length


				spaces = extra_space // max(1, len(line) - 1)
				remainder = extra_space % max(1, len(line) -1)

				for j in range(max(1, len(line) -1)):
					line[j] += " " * spaces
					if remainder:
						line[j] += " "
						remainder -= 1

				res.append("".join(line))
				line, length = [], 0

			#line is not complete
			line.append(words[i])
			length += len(words[i])
			i += 1

		#last line
		last_line = " ".join(line)
		trail_space = maxWidth - len(last_line)
		return res.append(last_line + " " * trail_space)