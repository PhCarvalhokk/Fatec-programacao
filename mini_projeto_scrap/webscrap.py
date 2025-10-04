import requests
import os
import time
import random
from bs4 import BeautifulSoup

# Cabeçalho para simular navegador
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Pasta de saída
output_folder = "novels_txt"
os.makedirs(output_folder, exist_ok=True)

def polite_sleep():
    time.sleep(random.uniform(1.0, 2.0))

def save_chapter_as_txt(title, content, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(title + "\n\n")
            f.write(content)
        print(f"[✔] Capítulo salvo em TXT: {filename}")
    except Exception as e:
        print(f"[X] Erro ao salvar {filename}: {e}")

def extract_chapter_text(soup):
    """
    Tenta encontrar o texto do capítulo em diferentes seletores.
    """
    candidates = []

    # 1) div com text-align: justify
    candidates.extend(soup.find_all("div", style=lambda v: v and "text-align: justify" in v))

    # 2) divs padrão do site
    for selector in ["div.entry-content", "div.post-content", "div.text-left"]:
        tag = soup.select_one(selector)
        if tag:
            candidates.append(tag)

    # 3) parágrafos (<p>) dentro do conteúdo
    if not candidates:
        paragraphs = soup.find_all("p")
        if paragraphs:
            return "\n\n".join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))

    # Extrair texto limpo
    text_blocks = []
    for block in candidates:
        text_blocks.append(block.get_text(separator="\n", strip=True))

    return "\n\n".join(text_blocks).strip()

# Entrada do usuário
novel_slug = input("Digite o slug da novel (ex: lord-of-mysteries): ").strip()
chapter_num = int(input("Digite o número do capítulo: "))

chapter_url = f"https://centralnovel.com/{novel_slug}-capitulo-{chapter_num}/"
print(f"\n📥 Buscando capítulo em {chapter_url}")
polite_sleep()

try:
    resp = requests.get(chapter_url, headers=headers, timeout=30)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    # Extrair título
    title_tag = soup.select_one("h1.entry-title, h1.post-title")
    title = title_tag.text.strip() if title_tag else f"Capítulo {chapter_num}"

    # Extrair texto do capítulo
    content = extract_chapter_text(soup)

    if not content:
        print("[X] Não foi possível encontrar o texto do capítulo.")
    else:
        filename = os.path.join(output_folder, f"{novel_slug}_capitulo_{chapter_num}.txt")
        save_chapter_as_txt(title, content, filename)

except Exception as e:
    print(f"[X] Erro ao processar capítulo {chapter_num}: {e}")