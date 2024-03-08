import os
import tkinter as tk
from tkinter import filedialog
import subprocess

def split_text_into_words(input_text, max_words):
    words = input_text.split()
    word_chunks = []

    current_chunk = ""
    current_word_count = 0

    for word in words:
        if current_word_count + len(word) <= max_words:
            current_chunk += word + " "
            current_word_count += len(word) + 1  # considera o espaço após a palavra
        else:
            word_chunks.append(current_chunk.strip())
            current_chunk = word + " "
            current_word_count = len(word) + 1

    if current_chunk.strip():
        word_chunks.append(current_chunk.strip())

    return word_chunks

def extract_and_save_chunks(file_path, output_folder, max_words, result_var):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        word_chunks = split_text_into_words(content, max_words)

        for i, word_chunk in enumerate(word_chunks, 1):
            output_file_path = os.path.join(output_folder, f"output_chunk_{i}.txt")

            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(word_chunk)

        result_var.set(f"Trechos extraídos e salvos na pasta: {output_folder}")

    except Exception as e:
        result_var.set(f"Erro ao processar o arquivo: {str(e)}")
        raise  # Adicionado para imprimir a traceback completa no console

def main():
    # Interface gráfica
    root = tk.Tk()
    root.title("Extrair Trechos e Dividir em Chunks")

    entry_var = tk.StringVar()
    result_var = tk.StringVar()

    # Defina o arquivo padrão como "fagner.txt"
    input_file = "rerer.txt"

    try:
        output_folder = filedialog.askdirectory(title="Selecionar Pasta de Saída")
        if not output_folder:
            raise ValueError("Operação cancelada.")

        max_words_per_chunk = 4096
        extract_and_save_chunks(input_file, output_folder, max_words_per_chunk, result_var)

    except Exception as e:
        print(f"Erro durante o processamento: {str(e)}")
        result_var.set(f"Erro durante o processamento: {str(e)}")

    tk.Label(root, textvariable=result_var, fg="green").pack()

    root.mainloop()

if __name__ == "__main__":
    main()
