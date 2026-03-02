from datetime import datetime
from zoneinfo import ZoneInfo

import factory
import factory.fuzzy
from faker import Faker

fake = Faker()


PRODUCT_NAMES = [
    'Notebook',
    'Mouse',
    'Teclado',
    'Monitor',
    'Cadeira Gamer',
    'Headset',
    'Webcam',
    'Impressora',
    'Roteador',
    'Pen Drive',
    'HD Externo',
    'Smartphone',
]


class ProductFactory(factory.Factory):
    class Meta:
        model = dict

    name = factory.fuzzy.FuzzyChoice(PRODUCT_NAMES)
    price = factory.fuzzy.FuzzyDecimal(low=10.0, high=5000.0, precision=2)
    sold_at = factory.fuzzy.FuzzyDateTime(
        start_dt=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
        end_dt=datetime(2025, 12, 31, tzinfo=ZoneInfo('UTC')),
    )
    quantity = factory.fuzzy.FuzzyInteger(1, 100)

    def __post_generation__(self, create, extracted, **kwargs):
        if not create:
            return

        self.sold_at = self.sold_at.isoformat()
        self.price = str(self.price)


class ArgumentsFactory(factory.Factory):
    class Meta:
        model = dict

    file = None
    format = factory.fuzzy.FuzzyChoice(['json', 'text'])
    start = None
    end = None

    class Params:
        with_end = factory.Trait(
            end=factory.fuzzy.FuzzyDateTime(
                start_dt=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
                end_dt=datetime(2025, 12, 31, tzinfo=ZoneInfo('UTC')),
            )
        )
        with_start = factory.Trait(
            start=factory.fuzzy.FuzzyDateTime(
                start_dt=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
                end_dt=datetime(2025, 12, 31, tzinfo=ZoneInfo('UTC')),
            )
        )

        with_start_and_end = factory.Trait(
            start=factory.fuzzy.FuzzyDateTime(
                start_dt=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
                end_dt=datetime(2025, 12, 31, tzinfo=ZoneInfo('UTC')),
            ),
            end=factory.fuzzy.FuzzyDateTime(
                start_dt=datetime(2025, 1, 1, tzinfo=ZoneInfo('UTC')),
                end_dt=datetime(2025, 12, 31, tzinfo=ZoneInfo('UTC')),
            ),
        )

    def __post_generation__(self, create, extracted, **kwargs):
        if not create:
            return

        if self.start and self.end and self.start > self.end:
            self.start, self.end = self.end, self.start

        if self.start:
            self.start = self.start.isoformat()
        if self.end:
            self.end = self.end.isoformat()


def make_product_for_date(year: int, month: int, day: int) -> dict:
    product = ProductFactory()
    product['sold_at'] = datetime(
        year, month, day, tzinfo=ZoneInfo('UTC')
    ).isoformat()
    return product


def make_arguments_for_date_range(year: int, month: int, day: int) -> dict:
    start = datetime(year, month, day, tzinfo=ZoneInfo('UTC')).isoformat()
    end = datetime(year, month, day, tzinfo=ZoneInfo('UTC')).isoformat()

    arguments = ArgumentsFactory(with_start_and_end=True)
    arguments['start'] = start
    arguments['end'] = end
    return arguments
