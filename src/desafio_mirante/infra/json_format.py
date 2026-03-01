import json

from desafio_mirante.core.entities.report import Report
from desafio_mirante.infra.domain_encoder import DomainEncoder


class JsonFormat:
    def __init__(self, report: Report):
        self.report = report

    def format(self) -> str:
        return json.dumps(self.report.to_dict(), cls=DomainEncoder)
