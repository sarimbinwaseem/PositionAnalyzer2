from dataclasses import dataclass, field

@dataclass
class Result:
	results: list = field(default_factory = list)
	position: int = 0
	noOfNumber: int = 0
