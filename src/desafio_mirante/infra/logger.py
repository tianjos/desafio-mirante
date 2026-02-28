import logging


def setup_logger(level: int = logging.INFO) -> logging.Logger:
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    )
