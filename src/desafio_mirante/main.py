from desafio_mirante.infra.cli import CLI
from desafio_mirante.infra.file_parser import SaleParser
from desafio_mirante.infra.logger import setup_logger
from desafio_mirante.application.calculation_use_case import CalculationUseCase
from desafio_mirante.app import App


def main():
    setup_logger()
    cli = CLI()
    args_dto = cli.as_arguments()
    
    use_case = CalculationUseCase(parser=SaleParser())
    app = App(use_case=use_case)
    result = app.run(args_dto=args_dto)

    print(result)
    # input_parser = Input()
    # input_args = input_parser.as_arguments()
    # csv_parser = CsvParser(file_path=input_args.file)
    # calculation_service = CalculationService(
    #     csv_parser=csv_parser, input_arguments=input_args
    # )

    # results = calculation_service.execute()
    # print(results)

if __name__ == '__main__':
    main()
