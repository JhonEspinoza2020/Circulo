class Circulo:
    def __init__(self, radio):
        self.PI = 3.1416
        self.radio = radio

    def circunferencia(self):
        return 2 * self.PI * self.radio


if __name__ == "__main__":
    instancia_circulo = Circulo(10)
    print(f"La circunferencia es: {instancia_circulo.circunferencia()}")