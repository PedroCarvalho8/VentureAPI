import requests as rq
import enum


class Movimentacao:
    def __init__(self, rota_base) -> None:
        self.__rota_base = rota_base
        self.status = self.Status.PARADO
        self.__timeout_time = 1

    class Status(enum.Enum):
        ANDANDOFRENTE = 'frente'
        ANDANDOTRAS = 'tras'
        PARADO = 'parado'

    class Direcoes(enum.Enum):
        FRENTE = 'frente'
        TRAS = 'tras'

    def andar(self, direcao: Direcoes) -> None:
        if not isinstance(direcao, Movimentacao.Direcoes):
            raise TypeError("A direcao deve ser do tipo Direcoes")

        direcao_oposta: Movimentacao.Direcoes = self.Direcoes.FRENTE \
            if direcao == self.Direcoes.TRAS \
            else self.Direcoes.TRAS

        if self.status == direcao_oposta:
            try:
                response: rq.Response = rq.get(self.__rota_base + direcao_oposta.value, timeout=self.__timeout_time)
                if response.status_code == 200:
                    response: rq.Response = rq.get(self.__rota_base + direcao.value, timeout=self.__timeout_time)
                    if response.status_code == 200:
                        for sts in movimentacao.Status:
                            if sts.value == direcao.value:
                                self.status = sts
            except Exception as e:
                print("Erro ao tentar inverter o sentido de movimentacao >>", str(e))
        else:
            try:
                response: rq.Response = rq.get(self.__rota_base + direcao.value, timeout=self.__timeout_time)
                if response.status_code == 200:
                    for sts in movimentacao.Status:
                        if sts.value == direcao.value:
                            self.status = sts
            except Exception as e:
                print("Erro ao tentar movimentar na direcao desejada >>", str(e))

    def parar(self) -> None:
        if self.status != self.Status.PARADO:
            try:
                response: rq.Response = rq.get(self.__rota_base + self.status.value, timeout=self.__timeout_time)
                if response.status_code == 200:
                    self.status = self.Status.PARADO
            except Exception as e:
                print("Erro ao tentar parar a movimentacao >>", str(e))


movimentacao = Movimentacao(rota_base="http://192.168.4.1/")
