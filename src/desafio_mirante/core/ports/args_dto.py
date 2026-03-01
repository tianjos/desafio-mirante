from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from desafio_mirante.core.entities.format import Format


@dataclass(frozen=True, kw_only=True)
class ArgsDTO:
    file: Path
    format: Format
    start: datetime | None = field(default=None)
    end: datetime | None = field(default=None)
