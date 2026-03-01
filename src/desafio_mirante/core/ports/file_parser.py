from typing import Generic, Protocol, TypeVar

T = TypeVar('T')

class FileParser(Protocol, Generic[T]):
    def from_csv(self, file_path: str) -> T: ...
