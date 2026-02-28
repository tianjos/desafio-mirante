from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

from desafio_mirante.core.format import Format


@dataclass(frozen=True)
class Arguments:
    file: Path
    format: Format
    start: datetime | None = field(default=None)
    end: datetime | None = field(default=None)
