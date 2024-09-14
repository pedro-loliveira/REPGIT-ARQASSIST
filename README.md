# Substituição de Velocidades de CNC

Este projeto é uma ferramenta em Python com uma interface gráfica criada com `Tkinter`, para substituir automaticamente valores de velocidade fixos por valores reais em arquivos .CNC.

### Funcionalidades
- Interface gráfica simples para a substituição de valores em arquivos CNC.
- Substituição automática dos valores de velocidade.
- Validação de arquivos e espessura.
- Confirmação visual antes de realizar as modificações.

- ### Requisitos
- Python 3.x
- Bibliotecas:
  - `tkinter` (incluída por padrão no Python)
  - `os`
  - `time`

### Instalação
1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   cd nome-do-repositorio
   python --version
   python nome_do_arquivo.py

### Como Usar
1. Ao iniciar a aplicação, será aberta uma janela gráfica.
2. Insira os nomes dos arquivos CNC e a espessura correspondente.
3. Revise os valores de substituição e clique em "Confirmar" para aplicar as mudanças.
4. O programa substituirá os valores de velocidade nos arquivos CNC selecionados e exibirá uma mensagem de sucesso.

### Compilação para Executável
Se você quiser compilar este projeto para um executável utilizando o `auto-py-to-exe`, siga estas etapas:

1. Instale o `auto-py-to-exe`:

   ```bash
   pip install auto-py-to-exe

   auto-py-to-exe

### Contribuição
Sinta-se à vontade para abrir pull requests ou issues caso deseje sugerir melhorias ou encontrar bugs.

### Licença
Este projeto está licenciado sob a [MIT License](LICENSE).

### Estrutura do Código
```plaintext
  ├── README.md
  ├── nome_do_arquivo.py  # Código principal com interface Tkinter
  └── outros_arquivos  # Se houver arquivos auxiliares, eles devem ser listados aqui

