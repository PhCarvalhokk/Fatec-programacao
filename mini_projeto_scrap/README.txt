# Novel Scraper - CentralNovel

Este projeto é um simples **web scraper em Python** para baixar capítulos de novels do site [CentralNovel](https://centralnovel.com/) e salvar o conteúdo em **arquivos .txt** (bloco de notas).  

O script identifica automaticamente a área de texto do capítulo (mesmo que varie de uma novel para outra) e salva com título + conteúdo em uma pasta local.

---

## Funcionalidades

- Busca e baixa capítulos de novels por **slug e número do capítulo**.  
- Extrai o texto do capítulo mesmo que a estrutura HTML varie.  
- Salva o capítulo em um arquivo `.txt` dentro da pasta `novels_pdfs`.  
- Simula um navegador para evitar bloqueios simples do site.  

---

## Requisitos

- Python 3.8+
- Dependências listadas no `requirements.txt`

---

## Instalação

## Crie um ambiente virtual (opcional)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

## Instale as dependências

pip install -r requirements.txt

## Uso

Execute o arquivo webscrap.py
Você será solicitado a digitar:

O slug da novel (exemplo: lord-of-mysteries)

O número do capítulo (exemplo: 34)





