import PyPDF2
import re
import matplotlib.pyplot as plt

# Caminho do arquivo do PDF
pdf_path = 'perfil1.pdf'

# Abre o PDF e extrai o texto da página 34 (lembrando que o índice começa em 0)
with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    page = reader.pages[33]  # Página 34 = índice 33
    text = page.extract_text()

# Exemplos de como capturar os dados. Adapte os padrões conforme o PDF.
# Busca número de homens advogados
homens = re.search(r"([0-9]+)\s+homens", text)
homens_count = int(homens.group(1)) if homens else 0

# Busca número de mulheres advogadas
mulheres = re.search(r"([0-9]+)\s+mulheres", text)
mulheres_count = int(mulheres.group(1)) if mulheres else 0

# Busca número de advogados com filhos
filhos = re.search(r"([0-9]+)\s+advogados com filhos", text)
filhos_count = int(filhos.group(1)) if filhos else 0

# Monta o gráfico
labels = ['Homens', 'Mulheres', 'Com Filhos']
values = [homens_count, mulheres_count, filhos_count]

plt.bar(labels, values, color=['blue', 'pink', 'green'])
plt.title('Perfil dos Advogados - Página 34')
plt.ylabel('Quantidade')
plt.show()
