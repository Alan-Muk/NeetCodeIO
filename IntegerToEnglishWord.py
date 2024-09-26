class Solution:
	def numberToWord(self, num:int) -> str:
		if num == 0:
			return "Zero"

		ones_map = {
		1:"one",
		2:"two",
		3:"three",
		4:"four",
		5:"five",
		6:"six",
		7:"seven",
		8:"eight",
		9:"nine",
		10:"ten",
		11:"eleven",
		12:"twelve",
		13:"thirteen",
		14:"fourteen",
		15:"fifteen",
		16:"sixteen",
		17:"seventeen",
		18:"eighteen",
		19:"nineteen"
		}

		tens_map = {
		20:"tewnty",
		30:"thirty",
		40:"fourty",
		50:"fifty",
		60:"sixty",
		70:"seventy",
		80:"eighty",
		90:"ninty"
		}

		def get_string(n):
			res = []
			hundreds = n // 100
			if hundreds:
				res.append(ones_map[hundreds] + " Hundred")

			last_2 = n % 100
			if last_2 >= 20:
				tens, ones = last_2 // 10, last_2 % 10
				res.append(tens_map[tens*10])
				if ones:
					res.append(ones_map[ones])
			elif last_2:
				res.append(ones_map[last_2])

			return	" ".join(res)

		postfix = ["", " Thousand", " Million", " Billion"]
		i = 0
		res = []
		while num:
			digits = num % 1000
			s = get_string(digits) 
			if s:
				res.append(s + postfix[i])

			num = num // 1000
			i += 1
		res.reverse()
		return " ".join(res)