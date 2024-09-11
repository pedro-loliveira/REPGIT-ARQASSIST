import os
import tkinter as tk
from tkinter import messagebox

# DIC VLC REAL PL2
velocidade_variavel_real = {
    "1,5": {"Laranja": 5200.000, "Azul": 4160.000, "Rosa": 3120.000, "Verde": 2080.000},
    "2,65": {"Laranja": 5200.000, "Azul": 4160.000, "Rosa": 3120.000, "Verde": 2080.000},
    "3": {"Laranja": 4350.000, "Azul": 3480.000, "Rosa": 2611.000, "Verde": 1740.000},
    "3,75": {"Laranja": 4000.000, "Azul": 3200.000, "Rosa": 2400.000, "Verde": 1600.000},
    "4,75": {"Laranja": 3100.000, "Azul": 2480.000, "Rosa": 1860.000, "Verde": 1240.000},
    "6,35": {"Laranja": 3000.000, "Azul": 2400.000, "Rosa": 1800.000, "Verde": 1200.000},
    "8": {"Laranja": 2000.000, "Azul": 1600.000, "Rosa": 1200.000, "Verde": 800.000},
    "9": {"Laranja": 1000.000, "Azul": 800.000, "Rosa": 600.000, "Verde": 400.000},
}
# Velocidades fixas CNC
velocidades_fixas = {
    "Laranja": 2610.000,
    "Azul": 2088.000,
    "Rosa": 1566.000,
    "Verde": 1044.000
}


def substituir_valores(nome_arquivo, espessura):
    # Func PRA LER O ARQ, subst, e salvar
    if espessura not in velocidade_variavel_real:
        messagebox.showerror("Erro", f"Espessura {espessura} não configurada.")
        return
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
    for cor, valor_fixo in velocidades_fixas.items():
        valor_real = velocidade_variavel_real[espessura][cor]
        conteudo = conteudo.replace(str(valor_fixo), str(valor_real))
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo)
    messagebox.showinfo("Sucesso", f"Arquivo {
                        nome_arquivo} modificado com sucesso.")


def verificar_arquivos(nomes_arquivos, diretorio):
    # verifica se os arquivos existem no diretorio
    arquivos_validos = []
    arquivos_invalidos = []
    for nome_arquivo in nomes_arquivos:
        caminho_completo = os.path.join(diretorio, f"{nome_arquivo}.cnc")
        if os.path.exists(caminho_completo):
            arquivos_validos.append(caminho_completo)
        else:
            arquivos_invalidos.append(nome_arquivo)
    return arquivos_validos, arquivos_invalidos


def processar():
    # realiza as subst
    diretorio = "P:/MicroEdge105"
    nomes_arquivos = entrada_arquivos.get().split(',')
    espessura = entrada_espessura.get().strip()
    # corrigir tirando os espaços
    nomes_arquivos = [nome.strip() for nome in nomes_arquivos]
    arquivos_validos, arquivos_invalidos = verificar_arquivos(
        nomes_arquivos, diretorio)
    if arquivos_invalidos:
        messagebox.showerror(
            "Erro", f"Os seguintes arquivos não foram encontrados:\n" + "\n".join(arquivos_invalidos))
        return
    if espessura not in velocidade_variavel_real:
        messagebox.showerror("Erro", f"Espessura {espessura} não configurada.")
        return

    # Informa oq sera alterado
    trocas = "\n".join([f"{cor}: {velocidades_fixas[cor]} -> {velocidade_variavel_real[espessura][cor]}"
                        for cor in velocidades_fixas])
    confirmar = messagebox.askyesno("Confirmação", f"Substituições para espessura {
                                    espessura} mm:\n{trocas}\n\nEstá correto?")
    if confirmar:
        for caminho_completo in arquivos_validos:
            substituir_valores(caminho_completo, espessura)


def criar_interface():
    # janelinha
    janela = tk.Tk()
    janela.title("Substituição de Velocidades de CNC")
    janela.geometry("400x200")

    label_arquivos = tk.Label(
        janela, text="CNC's (separados por vírgula)", font=("Arial", 10))
    label_arquivos.pack(pady=10)

    global entrada_arquivos
    entrada_arquivos = tk.Entry(janela, width=50, font=("Arial", 10))
    entrada_arquivos.pack(pady=5)

    label_espessura = tk.Label(janela, text="Espessura", font=("Arial", 10))
    label_espessura.pack(pady=5)

    global entrada_espessura
    entrada_espessura = tk.Entry(janela, width=20, font=("Arial", 10))
    entrada_espessura.pack(pady=5)

    # botaozao de processar
    botao_processar = tk.Button(
        janela, text="Processar", font=("Arial", 10), command=processar)
    botao_processar.pack(pady=15)

    # loop da janela
    janela.mainloop()


if __name__ == "__main__":
    criar_interface()
