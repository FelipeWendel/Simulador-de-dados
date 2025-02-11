import random

def lancar_dado():
    """Simula o lançamento de um dado e retorna o resultado"""
    return random.randint(1, 6)

def main():
    print("Simulador de Dados")
    print("------------------")

    num_lancamentos = int(input("Quantos lançamentos deseja realizar? "))

    resultados = []
    for i in range(num_lancamentos):
        resultado = lancar_dado()
        print(f"Lançamento {i+1}: {resultado}")
        resultados.append(resultado)

    print("\nResultados:")
    print("-----------")
    print(f"Média: {sum(resultados) / len(resultados)}")
    print(f"Maior valor: {max(resultados)}")
    print(f"Menor valor: {min(resultados)}")

if __name__ == "__main__":
    main()