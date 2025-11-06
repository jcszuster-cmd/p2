import streamlit as st
import PyPDF2
import re
import matplotlib.pyplot as plt

st.title('Perfil dos Advogados - Página 34')

pdf_path = 'perfil1.pdf'

try:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        page = reader.pages[33]
        text = page.extract_text()
except Exception as e:
    st.error(f'Erro ao abrir o PDF: {e}')
    st.stop()

homens = re.search(r"([0-9]+)\s+homens", text)
homens_count = int(homens.group(1)) if homens else 0

mulheres = re.search(r"([0-9]+)\s+mulheres", text)
mulheres_count = int(mulheres.group(1)) if mulheres else 0

filhos = re.search(r"([0-9]+)\s+advogados com filhos", text)
filhos_count = int(filhos.group(1)) if filhos else 0

labels = ['Homens', 'Mulheres', 'Com Filhos']
values = [homens_count, mulheres_count, filhos_count]

fig, ax = plt.subplots()
ax.bar(labels, values, color=['blue', 'pink', 'green'])
ax.set_ylabel('Quantidade')

st.pyplot(fig)
