import logging

from desafio_mirante.infra.input_options import InputOptions

from ..core.arguments import Arguments

logger = logging.getLogger(__name__)


class Input:
    def __init__(self):
        self.options = InputOptions()

    def as_arguments(self) -> Arguments:
        return Arguments(**self.options.as_dict())
