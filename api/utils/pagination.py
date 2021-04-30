from dataclasses import dataclass

@dataclass(frozen=True)
class Pagination:
  next_offset: int
  limit: int