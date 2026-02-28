from desafio_mirante.parser.csv_parser import CsvParser
from desafio_mirante.core.arguments import Arguments
from desafio_mirante.core.format import Format
from desafio_mirante.output.text_format import TextFormat
from desafio_mirante.output.json_format import JsonFormat

class CalculationService:
    def __init__(self, csv_parser: CsvParser, input_arguments: Arguments):
        self.csv_parser = csv_parser
        self.input_arguments = input_arguments

    def execute(self):
        sale = self.csv_parser.as_sales()

        if self.input_arguments.format == Format.TEXT: 
            return TextFormat(sale).format()

        return JsonFormat(sale).format()
