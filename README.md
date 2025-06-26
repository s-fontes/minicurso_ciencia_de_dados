# minicurso_ciencia_de_dados
Este repositório contém o material completo do minicurso introdutório de Ciência de Dados voltado para pesquisadores e estudantes que desejam aprender a tratar e analisar dados estruturados.
# Introdução à Ciência de Dados e Dados Públicos

A ciência de dados é uma área interdisciplinar que combina estatística, programação e conhecimento de domínio para extrair informações úteis a partir de dados. Seu objetivo é entender fenômenos, descobrir padrões e embasar decisões com base em evidências concretas.

Na prática, cientistas de dados lidam com a coleta, organização, limpeza, análise e visualização de grandes volumes de dados — que podem vir de sensores, redes sociais, pesquisas, sistemas de governo ou empresas.


## Dados públicos: um recurso valioso

No Brasil, órgãos como o IBGE, o INEP, o DATASUS e o Portal da Transparência disponibilizam grandes conjuntos de dados abertos sobre:

* População, saúde, educação, moradia
* Orçamentos públicos, transferências sociais, indicadores municipais

Esses dados são livres para uso e representam uma fonte riquíssima para:

* Pesquisas acadêmicas
* Projetos de iniciação científica
* Jornalismo de dados
* Análises políticas e sociais

## Por que isso importa?

Aprender a trabalhar com dados públicos é um passo importante para qualquer pesquisador, pois permite:

* Investigar hipóteses com dados reais
* Construir gráficos e indicadores confiáveis
* Produzir ciência aberta e transparente

Neste minicurso, vamos usar ferramentas simples e modernas (como o DuckDB) para explorar esses dados e extrair respostas para perguntas relevantes.

# Documentações

* [Python](https://docs.python.org/pt-br/3/)
* [pip](https://pip.pypa.io/en/stable/)
* [Bash](https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html)
* [DuckDB](https://duckdb.org/docs/stable/)
* [Pandas](https://pandas.pydata.org/docs/)
* [Requests](https://requests.readthedocs.io/en/latest/)
* [Jupyter](https://docs.jupyter.org/en/latest/)
* [Jupyter Widgets](https://ipywidgets.readthedocs.io/en/stable/#jupyter-widgets)
* [Matplotlib](https://matplotlib.org/stable/)
* [seaborn](https://seaborn.pydata.org/)
* [openpyxl](https://openpyxl.readthedocs.io/en/stable/)
* [Docker](https://docs.docker.com/)
* [Dev Container](https://containers.dev/implementors/json_reference/)
* [Git](https://git-scm.com/doc)
* [GitHub](https://docs.github.com/en)

## Como iniciar o ambiente no Codespaces a partir de um fork

### 1. Faça um **fork** do repositório

1. Acesse o repositório original [`s-fontes/minicurso_ciencia_de_dados`](https://github.com/s-fontes/minicurso_ciencia_de_dados).
2. Clique no botão **Fork** no canto superior direito e selecione sua conta.

### 2. Clone seu fork (opcional para uso local)

```bash
git clone https://github.com/SEU-USUARIO/minicurso_ciencia_de_dados.git
cd minicurso_ciencia_de_dados
```

### 3. Crie e abra o Codespace no GitHub

1. Na página do seu fork, clique em **Code** > aba **Codespaces**.
2. Clique em **Create codespace on main** (ou escolha uma branch específica).
3. Aguarde a inicialização do ambiente.

### 4. Ambiente já configurado

* O container é construído com base na imagem oficial do Python (3.13).
* As dependências do `requirements.txt` são instaladas automaticamente.
* Os arquivos são copiados
* Extensões recomendadas para Python, Jupyter e SQL são instaladas.
