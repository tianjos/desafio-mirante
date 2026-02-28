import logging
from argparse import ArgumentParser
from pathlib import Path

from ..core.arguments import Arguments
from ..core.format import Format

logger = logging.getLogger(__name__)


def existing_file(value: str) -> Path:
    file_path = Path(value)

    if not file_path.is_file():
        logger.info(f'File not found: {file_path}')
        raise ValueError(f'File not found: {file_path}')
    return file_path


class ArgumentParser(ArgumentParser):
    def __init__(self) -> None:
        super().__init__(
            prog='desafio-mirante',
            description='Desafio Mirante - Python Developer',
        )
        self.add_argument(
            '--file',
            type=existing_file,
            required=True,
            help='Path to the CSV file containing sales data',
        )
        self.add_argument(
            '--format',
            type=Format,
            choices=list(Format),
            default=Format.TEXT,
            help='Output format (default: text)',
        )

    def as_arguments(self):
        args = self.parse_args()

        return Arguments(file=args.file, format=args.format)

    def parse_args(self) -> Arguments:
        args = super().parse_args()
        logger.info(f'Parsed arguments: {args}')
        return args
