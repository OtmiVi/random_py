from random import choice


class HP:
	max_hearts: int
	current_hearts: int

	def __init__(self, max_hearts: int, current_hearts: int) -> None:
		if max_hearts < current_hearts:
			raise ValueError("max_hearts must be higher then current_hearts")
		else:
			self.max_hearts = max_hearts
			self.current_hearts = current_hearts

	def heal(self) -> None:
		if self.is_full_hearts():
			print("You have full HP")
		else:
			self.current_hearts += 1

	def is_full_hearts(self) -> bool:
		return self.current_hearts >= self.max_hearts

	def __str__(self) -> str:
		return f"{self.current_hearts} / {self.max_hearts}"


class Healer:
	@staticmethod
	def if_heal_heart() -> bool:
		return choice([True, False])

	@staticmethod
	def get_healing_time(hp: HP) -> int:
		time: int = 0
		while not hp.is_full_hearts():
			time += 1
			if Healer.if_heal_heart():
				hp.heal()

		return time


player: HP = HP(20, 4)
print((Healer.get_healing_time(player) * 30) / 60)
