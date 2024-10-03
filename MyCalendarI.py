class MyCalendar:

	def __init__(self):
		self.events = []

	def book(self, start:int, end:int) -> bool:
		for s, e in self.events:
			if not (e <= start or end <= s):
				return False

		self.events((start, end))
		return True
