# ArmazemDeConhecimento

Repositório pessoal dedicado ao armazenamento versionado (via **Git LFS**) de livros técnicos, apostilas, manuais e documentos de apoio para estudos em Ciência da Computação, Engenharia de Software, Matemática e áreas correlatas.

---

## Como este repositório se integra ao Cofre Obsidian

Este acervo funciona **em paralelo** ao cofre principal de estudos ([`CofreObsidian`](https://github.com/PCnaoliga/CofreObsidian)):

- **No Obsidian (`CofreLegal`):** este repositório fica montado localmente em `4-Arquivos/2.Documentos/Livros/`, caminho explicitamente ignorado pelo `.gitignore` do cofre principal para manter o repositório de notas leve e rápido.
- **Nas fichas de leitura (`4-Arquivos/1.Catalogo/`):** cada livro possui uma nota catalográfica com link interno offline (`[[Nome_Do_Arquivo.pdf]]`) e espelho externo apontando para este repositório no GitHub.
- **No GitHub (`ArmazemDeConhecimento`):** mantém apenas os arquivos PDF rastreados via Git LFS e este índice navegável.

---

## Estrutura de Pastas

```text
ArmazemDeConhecimento/
├── 1.Pessoais/                 # Documentos pessoais (não indexados no catálogo público)
├── 2.Estudos/                  # Acervo técnico organizado por área
│   ├── Algoritmos/             # Algoritmos, estruturas de dados e lógica discreta
│   ├── Banco de Dados/         # Modelagem, SQL e sistemas gerenciadores de banco de dados
│   ├── Linguagens _Prog/       # C, C++, Java, PHP, Python e Ruby
│   ├── Matemática/             # Cálculo, geometria analítica, estatística, lógica e teoria dos jogos
│   ├── Metodologia/            # Aprendizado e produtividade técnica
│   ├── Tecnologias baixo nivel/# GPU / CUDA e programação próxima ao hardware
│   └── Teorico/                # Arquitetura, engenharia de software, redes, Git e teoria da computação
├── scripts/
│   └── atualizar_readme.py     # Gerador automático do catálogo abaixo
├── .gitattributes              # Configuração de rastreamento Git LFS (*.pdf)
└── README.md
```

---

## Catálogo de Livros e Materiais

<!-- CATALOGO:INICIO -->
> **Acervo indexado:** **43 PDFs** distribuídos em **11 categorias** (790.5 MB no total).

### Algoritmos e Estruturas de Dados (`2.Estudos/Algoritmos/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Algoritmos: Teoria e Prática (CLRS)](2.Estudos/Algoritmos/Algoritmos%20-%20Teoria%20e%20Pr%C3%A1tica%20-%20Autor%20%28Thomas%20Cormen%29.pdf) | Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest e Clifford Stein | 63.4 MB |
| [Algoritmos em Linguagem C](2.Estudos/Algoritmos/Algoritmos-em-linguagem-C.pdf) | Referência Técnica / Robert Sedgewick & Paulo Feofiloff | 979 KB |
| [Matemática Discreta Aplicada à Computação](2.Estudos/Algoritmos/dm.pdf) | Material Didático / Apostila Universitária | 11.6 MB |
| [Entendendo Algoritmos: Um Guia Ilustrado Para Programadores e Outros Curiosos](2.Estudos/Algoritmos/Entendendo%20Algoritmos%20-%20Um%20Guia%20Ilustrado%20Para%20Programadores%20e%20Outros%20Curiosos%20-%20Autor%20%28Aditya%20Y.%20Bhargava%29.pdf) | Aditya Y. Bhargava | 11.9 MB |
| [Estruturas de Dados Usando C](2.Estudos/Algoritmos/Estruturas%20de%20Dados%20Usando%20C%20%28Tenenbaum%29.pdf) | Aaron M. Tenenbaum, Yedidyah Langsam e Moshe J. Augenstein | 6.8 MB |
| [Fundamentos de Programação: Algoritmos e Lógica](2.Estudos/Algoritmos/Fundamentos%20de%20Programa%C3%A7%C3%A3o.pdf) | Livro Didático Acadêmico | 9.2 MB |
| [Resumo das Estruturas de Dados Mais Importantes](2.Estudos/Algoritmos/Resumo%20das%20Estruturas%20de%20Dados%20mais%20importantes.pdf) | Guia de Consulta Técnica Rápida | 24 KB |

### Banco de Dados (`2.Estudos/Banco de Dados/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Sistemas de Banco de Dados - 6ª Edição (Ramez Elmasri, Shamkant B. Navathe)](2.Estudos/Banco%20de%20Dados/Sistemas%20de%20Banco%20de%20Dados%20%28Ramez%20Elmasri%2C%20Shamkant%20B.%20Navathe%29.pdf) | Ramez Elmasri e Shamkant B. Navathe | 13.9 MB |

### Engenharia de Software, Arquitetura e Teoria (`2.Estudos/Teorico/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Arquitetura e Organização de Computadores - 8ª Edição](2.Estudos/Teorico/Arquitetura%20e%20Organiza%C3%A7%C3%A3o%20de%20Computadores%20-%208%C2%AA%20Ed.pdf) | William Stallings | 20.1 MB |
| [Arquitetura Limpa: O Guia do Artesão para Estrutura e Design de Software](2.Estudos/Teorico/Arquitetura%20Limpa%20-%20O%20Guia%20do%20Artes%C3%A3o%20para%20Estrutura%20e%20Design%20de%20Software%20-%20Autor%20%28Robert%20C.%20Martin%29.pdf) | Robert C. Martin (Uncle Bob) | 6.7 MB |
| [The Mythical Man-Month: Essays on Software Engineering](2.Estudos/Teorico/BBservice%20147%20The%20Mythical%20Man%20Month%20Essays%20on%20Software%20--%20Frederick%20P_%20Brooks%2C%20Jr%20--%202%2C%201995%20--%20Addison-Wesley%20Professional%20--%209780132100694%20--%2062f54c3e4e9ba35cfe8622e93cceb18f%20--%20Anna%E2%80%99s%20Archive.pdf) | Frederick P. Brooks, Jr. | 19.4 MB |
| [Comparative Analysis of OSI and TCP/IP Models in Network](2.Estudos/Teorico/Comparative%20Analysis%20of%20OSI%20and%20TCPIP%20Models%20in%20Network.pdf) | Pesquisa / Documentação Técnica de Redes | 419 KB |
| [Controlando Versões com Git e GitHub](2.Estudos/Teorico/Controlando%20Vers%C3%B5es%20com%20Git%20e%20GitHub%20-%20Autor%20%28Casa%20do%20C%C3%B3digo%29.pdf) | Alexandre Aquiles (Casa do Código) | 1.9 MB |
| [Código Limpo: Habilidades Práticas do Agile Software](2.Estudos/Teorico/C%C3%B3digo%20limpo%20-%20Habilidades%20pr%C3%A1ticas%20do%20Agile%20Software%20-%20Autor%20%28Robert%20C.%20Martin%29.pdf) | Robert C. Martin (Uncle Bob) | 65.1 MB |
| [Engenharia de Software - 9ª Edição](2.Estudos/Teorico/Engenharia%20de%20Software%20-%209%20edi%C3%A7%C3%A3o.pdf) | Ian Sommerville | 17.7 MB |
| [Introduction to Theoretical Computer Science](2.Estudos/Teorico/Introduction%20to%20Theoretical%20Computer%20Science%20%28Boaz%20Barak%29.pdf) | Boaz Barak | 21.2 MB |
| [Introdução a Data Science: Algoritmos de Machine Learning e Métodos de Análise](2.Estudos/Teorico/Introdu%C3%A7%C3%A3o%20a%20data%20science%20-%20Algoritmos%20de%20machine%20learning%20e%20m%C3%A9todos%20de%20an%C3%A1lise%20-%20Autor%20%28Casa%20do%20C%C3%B3digo%29.pdf) | Casa do Código | 8.2 MB |
| [O Programador Pragmático: De Aprendiz a Mestre](2.Estudos/Teorico/O%20Programador%20Pragm%C3%A1tico%20-%20Autor%20%28Andrew%20Hunt%20e%20David%20Thomas%29.pdf) | Andrew Hunt e David Thomas | 1.3 MB |
| [Padrões de Projetos - Soluções Reutilizáveis de Software Orientados a Objetos](2.Estudos/Teorico/Padr%C3%B5es%20de%20Projetos%20-%20Solu%C3%A7%C3%B5es%20Reutiliz%C3%A1veis%20de%20Software%20Orientados%20a%20Objetos%20-%20Autor%20%28Erich%20Gamma%29.pdf) | Erich Gamma (GoF) | 5.2 MB |
| [Pro Git - 2ª Edição](2.Estudos/Teorico/progit.pdf) | Scott Chacon e Ben Straub | 17.9 MB |
| [SEO Prático: Seu Site na Primeira Página das Buscas](2.Estudos/Teorico/SEO%20Pr%C3%A1tico%20-%20Seu%20Site%20na%20Primeira%20P%C3%A1gina%20das%20Buscas%20-%20Autor%20%28Casa%20do%20C%C3%B3digo%29.pdf) | Casa do Código | 3.2 MB |
| [Structure and Interpretation of Computer Programs (SICP)](2.Estudos/Teorico/Structure_Interpretation_Computer.pdf) | Harold Abelson e Gerald Jay Sussman (MIT) | 7.1 MB |

### Linguagens de Programação — C e C++ (`2.Estudos/Linguagens _Prog/C e C++/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [C Completo e Total - 3ª Edição](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/c-completo-total.pdf) | Herbert Schildt | 37.7 MB |
| [C: A Linguagem de Programação (K&R)](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/C_A_linguagemDprograma%C3%A7%C3%A3o.pdf) | Brian W. Kernighan e Dennis M. Ritchie | 270.6 MB |
| [Programação Orientada a Objetos com C++](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/CppBorgesClinio_260904_071529.pdf) | Renato Borges e André Luiz Clinio | 325 KB |
| [Essential C: Guia da Universidade de Stanford](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/EssentialC.pdf) | Nick Parlante (Stanford CS Education Library) | 85 KB |
| [Modern C: Padrões C11 e C17](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/modernC.pdf) | Jens Gustedt (INRIA) | 3.7 MB |
| [Effective Modern C++ (Scott Meyers)](2.Estudos/Linguagens%20_Prog/C%20e%20C%2B%2B/Scott_Meyers_Effective_Modern_C%2B%2B.pdf) | Scott Meyers | 4.8 MB |

### Linguagens de Programação — Java (`2.Estudos/Linguagens _Prog/Java/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Introdução à Linguagem Java (Curso Java e OO)](2.Estudos/Linguagens%20_Prog/Java/Introdu%C3%A7%C3%A3o%20%C3%A0%20Linguagem%20Java%20%28Nelio%20Alves%29.pdf) | Prof. Dr. Nelio Alves | 1.1 MB |
| [Use a Cabeça Java: Guia do Aprendiz Para Programação no Mundo Real (3ª Edição)](2.Estudos/Linguagens%20_Prog/Java/Use%20a%20cabe%C3%A7a%20Java%20guia%20do%20aprendiz%20para%20programa%C3%A7%C3%A3o%20no%20mundo%20real%20%28Kathy%20Sierra%2C%20Bert%20Bates%2C%20Trisha%20Gee%29%20%28Z-Library%29.pdf) | Kathy Sierra, Bert Bates e Trisha Gee | 49.2 MB |

### Linguagens de Programação — PHP (`2.Estudos/Linguagens _Prog/PHP/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Mezzio e PHP 7: Uma União Poderosa para Criação de APIs](2.Estudos/Linguagens%20_Prog/PHP/Mezzio%20E%20Php%207%20Uma%20Uniao%20Poderosa%20Para%20Criacao%20De%20Apis%20%28Jhones%20S.%20Clementino%29.pdf) | Jhones S. Clementino (Casa do Código) | 3.2 MB |
| [PHP Orientado a Objetos: Princípios e Práticas](2.Estudos/Linguagens%20_Prog/PHP/phpoo.pdf) | Material Didático / Apostila de Especialização | 14.6 MB |

### Linguagens de Programação — Python (`2.Estudos/Linguagens _Prog/Python/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Python do ZERO à Programação Orientada a Objetos](2.Estudos/Linguagens%20_Prog/Python/Python%20do%20ZERO%20%C3%A0%20Programa%C3%A7%C3%A3o%20Orientada%20a%20Objetos%20%28Fernando%20Belom%C3%A9%20Feltrin%29.pdf) | Fernando Belomé Feltrin | 1.4 MB |

### Linguagens de Programação — Ruby (`2.Estudos/Linguagens _Prog/Ruby/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Conhecendo Ruby](2.Estudos/Linguagens%20_Prog/Ruby/conhecendo-ruby.pdf) | Eustáquio Rangel de Oliveira Jr. (TaQ) | 8.5 MB |

### Matemática e Lógica (`2.Estudos/Matemática/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Apostila de Lógica Matemática e Álgebra Proposicional](2.Estudos/Matem%C3%A1tica/Apostila%20L%C3%B3gica%20Matem%C3%A1tica.pdf) | Material Didático Acadêmico | 893 KB |
| [Elementos de Matemática Discreta para Computação](2.Estudos/Matem%C3%A1tica/Elementos%20de%20Matematica%20Discreta%20para%20computa%C3%A7%C3%A3o.pdf) | Livro-Texto Universitário | 1.4 MB |
| [Estatística: O que é, para que serve, como funciona](2.Estudos/Matem%C3%A1tica/Estatistica%20-%20O%20que%20e%2C%20para%20que%20serve%2C%20como%20funciona%20.pdf) | Charles Wheelan | 2.9 MB |
| [Game Theory (An open access textbook)](2.Estudos/Matem%C3%A1tica/Game%20Theory%20%28Giacomo%20Bonanno%29.pdf) | Giacomo Bonanno | 5.2 MB |
| [Um Curso de Cálculo - Volume 2](2.Estudos/Matem%C3%A1tica/Guidorizzi_v2.pdf) | Hamilton Luiz Guidorizzi | 13.0 MB |
| [Um Curso de Cálculo - Volume 1](2.Estudos/Matem%C3%A1tica/GuidorizziVol1.pdf) | Hamilton Luiz Guidorizzi | 14.1 MB |
| [Geometria Analítica: Um Tratamento Vetorial](2.Estudos/Matem%C3%A1tica/PAULO%20BOULOS%2C%20IVAN%20DE%20CAMARGO%20GEOMETRIA%20ANALITICA%20-%20UM%20TRATAMENTO%20VETORIAL.pdf) | Paulo Boulos e Ivan de Camargo | 8.3 MB |

### Metodologia de Aprendizado (`2.Estudos/Metodologia/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [Aprendendo a Aprender](2.Estudos/Metodologia/Aprendendo_a_aprender_Barbara_Oakley.pdf) | Barbara Oakley | 32.0 MB |

### Tecnologias de Baixo Nível (`2.Estudos/Tecnologias baixo nivel/`)

| Material | Autor | Tamanho |
|---|---|---:|
| [CUDA C++ Programming Guide](2.Estudos/Tecnologias%20baixo%20nivel/CUDA_C_Programming_Guide.pdf) | NVIDIA Corporation | 4.4 MB |

<!-- CATALOGO:FIM -->

---

## Como baixar e usar (Git LFS)

Os arquivos `.pdf` são armazenados com **Git LFS** (*Large File Storage*). Sem o Git LFS instalado, o clone trará apenas ponteiros de texto em vez dos PDFs reais.

```bash
# 1. Instale o git-lfs (ex.: Arch Linux) e ative os hooks
sudo pacman -S git-lfs
git lfs install

# 2. Clone o repositório
git clone git@github.com:PCnaoliga/ArmazemDeConhecimento.git

# 3. Caso já tenha clonado sem LFS e queira baixar os binários:
git lfs pull
```

---

## Fluxo de manutenção (Adicionar novos livros)

1. Adicione o PDF na subpasta temática correspondente dentro de `2.Estudos/`.
2. Atualize o índice do `README.md` automaticamente:
   ```bash
   python3 scripts/atualizar_readme.py
   ```
3. Confira o `git status` (garantindo que o `git-lfs` esteja ativo) e faça commit/push neste repositório.
4. No cofre Obsidian, crie ou atualize a ficha correspondente em `4-Arquivos/1.Catalogo/` mantendo o vínculo interno (`[[Arquivo.pdf]]`) e o link para o GitHub.
