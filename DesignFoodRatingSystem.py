#from sortedContainers import SortedSet

class FoodRating:
	def __init__(self, foods:list[str], cuisines:list[str], ratings:list[int]):
		self.cuisines_food = defaultdict(SortedSet) #cuisine:rating, food
		self.cuisines = {} # foof:cuisine
		self.ratings = {} #food:rating

		for i in range(len(foods)):
			self.cuisines_food[cuisines[i]].add((-ratings[i], foods[i]))
			self.cuisines[foods[i]] = cuisines[i] 
			self.ratings[foods[i]] = ratings[i]

	def changeRating(self, food:str, newRating:int) -> None:

		c = self.cuisines[food]
		r = self.ratings[food]

		self.cuisines_food[c].remove((-r, food))
		self.cuisines_food[c].add((-newRating, food))

		self.ratings[food] = newRating

	def highestRated(self, cuisines:str) -> str:
		return self.cuisines_food[cuisines][0][1]
