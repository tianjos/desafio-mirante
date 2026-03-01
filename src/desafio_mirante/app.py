from desafio_mirante.application.calculation_use_case import CalculationUseCase
from desafio_mirante.core.dtos.args import ArgsDTO


class App:
    def __init__(self, use_case: CalculationUseCase):
        self.use_case = use_case

    def run(self, args_dto: ArgsDTO):
        result = self.use_case.execute(args_dto)
        return result
