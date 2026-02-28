from dataclasses import dataclass

from desafio_mirante.core.sale import Sale


@dataclass(frozen=True)
class Report:
    sale: Sale
    header: str

    def as_text(self) -> str:
        return self.sale.as_text()

    def as_json(self) -> str:
        return self.sale.as_json()
