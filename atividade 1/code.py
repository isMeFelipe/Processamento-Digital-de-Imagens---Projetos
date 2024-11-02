import numpy as np
import matplotlib.pyplot as plt

def normalizar_vetor(vetor):
    soma_total = sum(vetor)
    if soma_total == 0:
        raise ValueError("A soma dos elementos do vetor é zero; não é possível normalizar.")
    vetor_normalizado = [x / soma_total for x in vetor]
    return vetor_normalizado

def multiplicar_acumulado(vetor, fator):
    soma_acumulada = 0
    vetor_resultado = []
    for valor in vetor:
        soma_acumulada += valor
        vetor_resultado.append(soma_acumulada * fator)
    return vetor_resultado

def arredondar_personalizado(vetor):
    vetor_arredondado = []
    for valor in vetor:
        parte_inteira = int(valor)
        parte_decimal = valor - parte_inteira
        if parte_decimal == 0.5:
            valor_arredondado = int(valor)  # Arredonda para baixo se a parte decimal for 0.5
        else:
            valor_arredondado = round(valor)  # Arredonda normalmente caso contrário
        vetor_arredondado.append(valor_arredondado)
    return vetor_arredondado

def aplicar_aproximacao(vetor_original, vetor_arredondado):
    vetor_resultado = [0] * len(vetor_original)
    for indice, posicao in enumerate(vetor_arredondado):
        vetor_resultado[posicao] += vetor_original[indice]
    return vetor_resultado

def combinar_vetores(v1, v2):
    # Criar o vetor v3 com zeros, tamanho baseado no maior valor em v2
    tamanho_maximo = max(v2)
    v3 = [0] * (tamanho_maximo + 1)

    # Acumular os valores de v1 de acordo com v2
    for indice, posicao in enumerate(v2):
        # Adicionar valor de v1 na posição correspondente em v3
        v3[posicao] += v1[indice]

    return v3
def especificar_histograma(histograma_original, cdf_original, cdf_alvo):
    """
    Ajusta um histograma original para que sua distribuição siga a distribuição de um histograma alvo,
    utilizando as funções de distribuição acumulada (CDFs) fornecidas.

    Parâmetros:
    histograma_original : numpy.ndarray
        O histograma que será ajustado.
    cdf_original : numpy.ndarray
        A CDF correspondente ao histograma original.
    cdf_alvo : numpy.ndarray
        A CDF do histograma que queremos atingir.

    Retorna:
    numpy.ndarray
        O histograma ajustado para seguir a distribuição do histograma alvo.
    """
    
    # Inicializa um vetor para armazenar o mapeamento de índices
    mapeamento_indices = np.zeros_like(histograma_original, dtype=int)  
    indice_alvo = 0  # Usado para iterar sobre a CDF alvo

    # Para cada valor no histograma original, encontra o índice correspondente na CDF alvo
    for indice_original in range(len(histograma_original)):
        # Enquanto a CDF alvo não for maior que a CDF original, continue avançando
        while indice_alvo < len(cdf_alvo) and cdf_alvo[indice_alvo] < cdf_original[indice_original]:
            indice_alvo += 1
        mapeamento_indices[indice_original] = indice_alvo  # Armazena o índice correspondente na CDF alvo

    # Cria um novo histograma ajustado
    histograma_ajustado = np.zeros_like(histograma_original)
    
    # Preenche o histograma ajustado com os valores do histograma original
    for indice in range(len(histograma_original)):
        histograma_ajustado[mapeamento_indices[indice]] += histograma_original[indice]
    
    return histograma_ajustado


def plotar_graficos(vetor_original, vetor_original_equalizado, vetor_especificado, vetor_especificado_equalizado, vetor_histograma_especificado):
    # Criando um gráfico para cada vetor
    plt.figure(figsize=(12, 12))

    plt.subplot(3, 2, 1)
    plt.bar(range(len(vetor_original)), vetor_original, color='blue', alpha=0.7)
    plt.title("Vetor Original")
    plt.xlabel("Índices")
    plt.ylabel("Valores")

    plt.subplot(3, 2, 2)
    plt.bar(range(len(vetor_original_equalizado)), vetor_original_equalizado, color='green', alpha=0.7)
    plt.title("Vetor Original Equalizado")
    plt.xlabel("Índices")
    plt.ylabel("Valores")

    plt.subplot(3, 2, 3)
    plt.bar(range(len(vetor_especificado)), vetor_especificado, color='orange', alpha=0.7)
    plt.title("Vetor Especificado")
    plt.xlabel("Índices")
    plt.ylabel("Valores")

    plt.subplot(3, 2, 4)
    plt.bar(range(len(vetor_especificado_equalizado)), vetor_especificado_equalizado, color='red', alpha=0.7)
    plt.title("Vetor Especificado Equalizado")
    plt.xlabel("Índices")
    plt.ylabel("Valores")

    plt.subplot(3, 2, 6)
    plt.bar(range(len(vetor_histograma_especificado)), vetor_histograma_especificado, color='cyan', alpha=0.7)
    plt.title("Histograma Original Especificado")
    plt.xlabel("Índices")
    plt.ylabel("Valores")

    plt.tight_layout()
    plt.show()

# Exemplo de uso
vetor_original = [1200, 800, 600, 400, 300, 200, 100, 100, 50, 50, 50, 50, 50, 50, 0, 0]
vetor_especificado = [0, 0, 0, 100, 100, 100, 300, 300, 400, 800, 1200, 300, 200, 100, 50, 50]

print("========== PROCESSAMENTO DO VETOR ORIGINAL ==========")
print("Vetor Original:", vetor_original)

# Normalizando o vetor
vetor_normalizado = normalizar_vetor(vetor_original)

# Multiplicando os valores acumulados
fator_multiplicacao = len(vetor_original) - 1
vetor_multiplicado = multiplicar_acumulado(vetor_normalizado, fator_multiplicacao)

# Aproximando os valores do vetor multiplicado
vetor_aproximado = arredondar_personalizado(vetor_multiplicado)

# Aplicando a aproximação ao vetor original
vetor_original_equalizado = aplicar_aproximacao(vetor_original, vetor_aproximado)
print("Vetor Equalizado Final:", vetor_original_equalizado)

print("\n\n========== PROCESSAMENTO DO VETOR ESPECIFICADO ==========")
print("Vetor Especificado:", vetor_especificado)

# Normalizando o vetor especificado
vetor_especificado_normalizado = normalizar_vetor(vetor_especificado)

# Multiplicando os valores acumulados no vetor especificado
vetor_especificado_multiplicado = multiplicar_acumulado(vetor_especificado_normalizado, fator_multiplicacao)

# Aproximando os valores do vetor especificado multiplicado
vetor_especificado_aproximado = arredondar_personalizado(vetor_especificado_multiplicado)
# Aplicando a aproximação ao vetor especificado
vetor_especificado_equalizado = aplicar_aproximacao(vetor_especificado, vetor_especificado_aproximado)
print("Vetor Especificado Equalizado:", vetor_especificado_equalizado)

# feito manualmente
vetor_histograma_especificado = [0,0,0,0,0,0,0,1200,0,800,600,250,0,150,0,0]
# Plotar os gráficos
plotar_graficos(vetor_original, vetor_original_equalizado, vetor_especificado, vetor_especificado_equalizado, vetor_histograma_especificado)


print(vetor_aproximado)
print(vetor_especificado_aproximado)
