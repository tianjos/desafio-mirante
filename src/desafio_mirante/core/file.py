from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class File:
    path: Path

    def __post_init__(self):
        if not self.path.is_file():
            raise ValueError(f'File not found: {self.path}')
