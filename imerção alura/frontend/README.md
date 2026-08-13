# 🏆 Alura Album - Copa do Mundo Tech

O **Alura Album** é uma aplicação web interativa desenvolvida como parte da Imersão de IA da Alura (Edição Julho de 2026). Trata-se de um tributo interativo à história e evolução do desenvolvimento de software, reunindo personalidades influentes da tecnologia nacional e internacional — desde os pioneiros da Inteligência Artificial e criadores de linguagens, até educadores proeminentes da comunidade brasileira.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é criar uma experiência digital rica e imersiva de um álbum de figurinhas clássico. Utilizando técnicas de animação 3D de páginas virando e geração de som sintético via código, os usuários podem "folhear" o álbum e colecionar figurinhas que são carregadas dinamicamente a partir de um servidor backend (API).

---

## 📂 Arquivos do Projeto e Suas Funcionalidades

O projeto é construído em uma arquitetura limpa de frontend baseada em **HTML5**, **CSS3** e **JavaScript (ES6)**:

### 1. 📄 [index.html](index.html)
* **Função**: Define a estrutura semântica e todo o conteúdo do álbum.
* **Componentes Principais**:
  * Estruturação das páginas do álbum (Capa, Categorias de Tecnologia, Destaques do Brasil e Contracapa).
  * Marcação dos espaços reservados para cada figurinha (`.sticker-slot`), contendo o número do slot, nome da personalidade e sua breve descrição ou papel.
  * Elementos de interface como os botões de navegação lateral (Página Anterior/Próxima) e botão de alternância de áudio (Mudo/Ativo).
  * Importação da biblioteca externa **St.PageFlip** via CDN e inicialização do arquivo script principal.

### 2. 🎨 [style.css](style.css)
* **Função**: Controla toda a estilização, design de interface (UI) e experiência visual (UX).
* **Componentes Principais**:
  * **Design System**: Definição de variáveis customizadas (`--color-blue-universe`, `--color-deep-blue`, `--color-tech-blue`, etc.) criando uma paleta de cores futurista e coesa.
  * **Tipografia**: Integração com as fontes do Google Fonts (*Inter* para textos comuns e *Outfit* para títulos de destaque).
  * **Estética Premium**: Efeitos de neon no hover, efeito de distorção de texto (*glitch*) na capa, gradientes de cor sutis e sombras 3D realistas nas páginas do livro.
  * **Layouts**: Uso de Flexbox e Grid CSS para organizar os slots de figurinhas de forma limpa e responsiva.

### 3. ⚙️ [app.js](app.js)
* **Função**: Orquestra toda a lógica de comportamento e interatividade da aplicação.
* **Componentes Principais**:
  * **Biblioteca PageFlip**: Configura e inicializa o componente de animação das páginas, controlando dimensões, sombras, suporte a scroll de dispositivos móveis e velocidade de virada de páginas.
  * **Consumo de API (`preencherFigurinhas`)**: Faz uma requisição assíncrona (`fetch`) para a API backend (`http://localhost:8000/figurinhas`), obtendo dinamicamente a listagem de figurinhas, mapeando-as por ID e injetando as fotos diretamente nos slots correspondentes do HTML.
  * **Áudio Sintético (`playPaperTurnSound`)**: Utiliza a tecnologia nativa **Web Audio API** do navegador para simular em tempo real um som de folheamento físico (ruído branco modulado por filtros passa-banda e passa-baixa).
  * **Eventos de Navegação**: Escuta as interações do usuário nas setas de tela, suporte a cliques e arrastes manuais para folhear e atalhos de teclado (setas para a esquerda e para a direita).

---

## 🛠️ Como Executar o Projeto

Para visualizar a aplicação completa com as figurinhas preenchidas, certifique-se de que a API do backend está ativa:

1. **Iniciar o Servidor Backend (se aplicável)**:
   ```bash
   cd backend/dia-3
   uvicorn main:app --reload
   ```
   *Isso disponibilizará a API em `http://localhost:8000`.*

2. **Abrir o Frontend**:
   * Abra o arquivo `index.html` diretamente no seu navegador, ou utilize uma extensão como o *Live Server* no VS Code para servir os arquivos estáticos.
