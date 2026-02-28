from desafio_mirante.infra.input import Input
from desafio_mirante.parser.csv_parser import CsvParser
from desafio_mirante.infra.logger import setup_logger
from desafio_mirante.core.services.calculation_service import CalculationService


def main():
    setup_logger()
    input_parser = Input()
    input_args = input_parser.as_arguments()
    csv_parser = CsvParser(file_path=input_args.file)
    calculation_service = CalculationService(
        csv_parser=csv_parser, input_arguments=input_args
    )

    results = calculation_service.execute()
    print(results)

if __name__ == '__main__':
    main()
