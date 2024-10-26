import numpy as np
import matplotlib.pyplot as plt

def equalize_histogram(hist):
    """
    Equaliza um histograma dado.

    Parâmetros:
        hist (list ou np.array): Histograma de entrada.
    
    Retorna:
        np.array: Histograma equalizado.
    """
    total_pixels = np.sum(hist)
    cdf = hist.cumsum()
    cdf_normalized = (cdf - cdf.min()) * (len(hist) - 1) / (total_pixels - cdf.min())
    cdf_normalized = cdf_normalized.astype(np.uint8)

    equalized_hist = np.zeros_like(hist)
    for i in range(len(hist)):
        equalized_hist[cdf_normalized[i]] += hist[i]
    
    return equalized_hist

def specify_histogram(hist, target_hist):
    """
    Especifica um histograma dado para seguir um histograma alvo.

    Parâmetros:
        hist (list ou np.array): Histograma de entrada.
        target_hist (list ou np.array): Histograma alvo.
    
    Retorna:
        np.array: Histograma especificado.
    """
    total_pixels = hist.sum()
    target_total_pixels = target_hist.sum()

    cdf_original = hist.cumsum() / total_pixels
    cdf_target = target_hist.cumsum() / target_total_pixels

    mapping = np.zeros_like(hist)
    g_j = 0
    for rk in range(len(hist)):
        while g_j < len(target_hist) and cdf_target[g_j] < cdf_original[rk]:
            g_j += 1
        mapping[rk] = g_j

    specified_hist = np.zeros_like(hist)
    for i in range(len(hist)):
        specified_hist[mapping[i]] += hist[i]
    
    return specified_hist

# Função para imprimir histogramas com espaçamento uniforme
def print_histogram(label, histogram):
    # Imprime o label e os valores formatados
    print(f"{label}:\n", end="")
    print(" ".join(f"{value:5d}" for value in histogram))

# Função para gerar gráficos dos histogramas
def plot_histograms(original, equalized, specified):
    plt.figure(figsize=(15, 5))

    # Histograma original
    plt.subplot(1, 3, 1)
    plt.bar(range(len(original)), original, color='gray')
    plt.title("Histograma Original")
    plt.xlabel("Níveis de Intensidade")
    plt.ylabel("Frequência de Pixels")

    # Histograma equalizado
    plt.subplot(1, 3, 2)
    plt.bar(range(len(equalized)), equalized, color='blue')
    plt.title("Histograma Equalizado")
    plt.xlabel("Níveis de Intensidade")
    plt.ylabel("Frequência de Pixels")

    # Histograma especificado
    plt.subplot(1, 3, 3)
    plt.bar(range(len(specified)), specified, color='green')
    plt.title("Histograma Especificado")
    plt.xlabel("Níveis de Intensidade")
    plt.ylabel("Frequência de Pixels")

    # Mostrar os gráficos
    plt.tight_layout()
    plt.show()
    

# Ambiente de Execução --------------------------------------------------
# Histograma original, obtido no passo 1 do método de equalização
original_histogram = np.array([1200, 800, 600, 400, 300, 200, 150, 100, 50, 50, 50, 50, 50, 50, 50, 50])

# Histograma alvo, fornecido para a especificação
target_histogram = np.array([50, 50, 50, 100, 150, 200, 300, 400, 600, 800, 1200, 400, 300, 200, 100, 50])

# Equalização do histograma original
equalized_histogram = equalize_histogram(original_histogram)

# Especificação do histograma para o histograma alvo
specified_histogram = specify_histogram(equalized_histogram, target_histogram)

# Resultados        ------------------------------------------------------    
print_histogram("Histograma Original", original_histogram)
print_histogram("Histograma Equalizado", equalized_histogram)
print_histogram("Histograma Especificado", specified_histogram)

plot_histograms(original_histogram, equalized_histogram, specified_histogram)

