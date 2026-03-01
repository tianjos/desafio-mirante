import json

from desafio_mirante.core.sale import Sale
from desafio_mirante.infra.domain_encoder import DomainEncoder


class JsonFormat:
    def __init__(self, sale: Sale):
        self.sale = sale

    def format(self) -> str:
        return json.dumps(self.sale, cls=DomainEncoder)
