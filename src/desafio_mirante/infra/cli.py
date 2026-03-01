import logging

from desafio_mirante.infra.cli_options import CLIOptions
from desafio_mirante.core.dtos.args import ArgsDTO

logger = logging.getLogger(__name__)


class CLI:
    def __init__(self):
        self.options = CLIOptions()

    def as_arguments(self) -> ArgsDTO:
        return ArgsDTO(**self.options.as_dict())
