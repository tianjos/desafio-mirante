import logging
from argparse import ArgumentParser
from datetime import datetime
from pathlib import Path
from typing import TypedDict

from desafio_mirante.core.entities.format import Format

logger = logging.getLogger(__name__)


class Arguments(TypedDict):
    file: Path
    format: Format


def existing_file(value: str) -> Path:
    file_path = Path(value)

    if not file_path.is_file():
        logger.info(f'File not found: {file_path}')
        raise ValueError(f'File not found: {file_path}')
    return file_path


def parse_date(value: str) -> datetime:
    try:
        return datetime.fromisoformat(value)
    except ValueError:
        logger.info(f'Invalid date format: {value}. Expected YYYY-MM-DD.')
        raise ValueError(f'Invalid date format: {value}. Expected YYYY-MM-DD.')


class CLIOptions:
    def __init__(self):
        self._parser = ArgumentParser(
            prog='desafio-mirante',
            description='Desafio Mirante - Python Developer',
        )

        self._parser.add_argument(
            '--file',
            type=existing_file,
            required=True,
            help='Path to the CSV file containing sales data',
        )
        self._parser.add_argument(
            '--format',
            type=Format,
            choices=list(Format),
            default=Format.TEXT,
            help='Output format (default: text)',
        )
        self._parser.add_argument(
            '--start',
            type=parse_date,
            help='Start date for filtering sales data (YYYY-MM-DD)',
        )
        self._parser.add_argument(
            '--end',
            type=parse_date,
            help='End date for filtering sales data (YYYY-MM-DD)',
        )

    def as_dict(self) -> Arguments:
        args = self._parser.parse_args()
        return vars(args)
