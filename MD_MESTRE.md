# MASTER — Fluxo de Execução do Projeto

Este documento define o fluxo padrão que deve ser seguido pela IA em qualquer tarefa solicitada neste projeto.

## 1. Regra principal

Antes de realizar qualquer alteração, a IA deve:

1. Analisar o contexto geral do projeto.
2. Identificar exatamente o que foi solicitado.
3. Consultar os documentos de instrução necessários.
4. Executar a tarefa seguindo rigorosamente as regras desses documentos.
5. Testar e validar as alterações realizadas.
6. Documentar ou atualizar os arquivos necessários.
7. Executar o Git Flow definido neste projeto.
8. Finalizar informando de forma objetiva o que foi realizado e o resultado dos testes.

**Não pule etapas.**

---

# 2. Fluxo geral

A execução deve seguir obrigatoriamente esta ordem:

```text
SOLICITAÇÃO
    ↓
ANÁLISE DO CONTEXTO
    ↓
IDENTIFICAÇÃO DOS DOCUMENTOS DE INSTRUÇÃO
    ↓
ANÁLISE DA ESTRUTURA DO PROJETO
    ↓
IMPLEMENTAÇÃO
    ↓
TESTES E VALIDAÇÃO
    ↓
DOCUMENTAÇÃO
    ↓
ARTIGO/OVERLEAF
    ↓
GIT FLOW
    ↓
RELATÓRIO FINAL
```

---

# 3. Etapa 1 — Analisar o contexto

Primeiro, analise:

* A solicitação atual.
* A estrutura existente do projeto.
* Os arquivos relacionados à tarefa.
* As tecnologias utilizadas.
* As regras e restrições existentes.
* Os documentos `.md` de instrução disponíveis.

Não comece a implementar antes de compreender o contexto necessário.

Se houver código existente relacionado à tarefa, **prefira adaptar e reutilizar o que já existe** em vez de criar estruturas duplicadas.

---

# 4. Etapa 2 — Consultar as instruções específicas

Cada etapa do projeto possui suas próprias regras.

Antes de executar uma atividade, consulte o documento correspondente.

### Documentos de referência

| Documento             | Finalidade                                    |
| --------------------- | --------------------------------------------- |
| `MD_OVERLEAF.md`       | Regras e chaves de acesso |
| `MD_ESTRUTURA.md`     | Estrutura e padrões que devem ser seguidos    |
| `MD_GITFLOW.md`       | Fluxo de Git, branches, commits e integração  |

**Os nomes acima são exemplos. Caso os arquivos tenham nomes diferentes, utilize os documentos equivalentes existentes no projeto.**

---

# 5. Etapa 3 — Executar a tarefa

Após compreender a solicitação e consultar as instruções necessárias:

1. Planeje brevemente a implementação.
2. Identifique os arquivos que precisam ser criados ou alterados.
3. Realize as alterações.
4. Mantenha o padrão arquitetural e estrutural existente.
5. Evite alterações que não sejam necessárias para a tarefa.
6. Não remova funcionalidades existentes sem justificativa.
7. Não introduza dependências ou tecnologias desnecessárias.

Se encontrar um problema que impeça a execução correta, investigue a causa antes de aplicar uma solução.

---

# 6. Etapa 4 — Testes e validação

Após implementar:

1. Consulte `MD_TESTES.md`,  Se não exitir, crie;
2. Execute os testes necessários.
3. Verifique erros de compilação, execução ou integração.
4. Valide se a implementação atende à solicitação original.
5. Corrija problemas encontrados.
6. Execute novamente os testes após as correções.

**Não considere a tarefa concluída apenas porque o código foi alterado.**

A implementação só está concluída quando estiver validada.

---

# 7. Etapa 5 — Documentação

Caso a tarefa exija documentação:

1. Consulte `MD_DOCUMENTACAO.md`, se não existir, crie.
2. Identifique quais documentos precisam ser criados ou atualizados.
3. Siga a estrutura definida nesse documento.
4. Não altere documentação que não esteja relacionada à tarefa.

Se a documentação fizer parte obrigatória da tarefa, ela deve ser concluída antes do Git Flow.

---

# 7.1 Etapa 5.1 — Artigo científico e publicação no Overleaf

Todo projeto (`projeto_N/`) que envolva artigo de referência deve produzir o **artigo
científico próprio** em LaTeX (template LNCS) e publicá-lo no Overleaf. Essa etapa é
obrigatória e sempre executada pela IA:

1. Consultar `MD_OVERLEAF.md` (token, clone, lista de documentos publicados).
2. **Criar/atualizar** o `.tex` do artigo do projeto vigente a partir do relatório
   técnico (`projeto_N/report/relatorio_tecnico.md`) e das figuras
   (`projeto_N/results/figs/`), seguindo o padrão do artigo já publicado do projeto
   anterior.
3. **Compilar localmente** com Latex (pdflatex/latexmk) e corrigir erros até gerar PDF
   sem erros.
4. **Validar** o PDF (páginas, conteúdo, sem `[?]` de citações não resolvidas).
5. **Dar push no Overleaf**: adicionar/atualizar `.tex` e figuras, commitar e enviar
   para o repositório do Overleaf com o token.
6. Se o projeto vigente já possuir artigo publicado e ele for **alterado** (ex.: novos
   resultados, figuras ou métricas), repetir os passos 2–5 para atualizar o mesmo
   artigo no Overleaf.

A publicação no Overleaf é independente do Git Flow do repositório local (que segue
`MD_GITFLOW.md`).

---

# 8. Etapa 6 — Git Flow

Depois que a implementação e os testes estiverem concluídos:

1. Consulte obrigatoriamente `MD_GITFLOW.md`.
2. Verifique o estado atual do Git.
3. Analise as alterações realizadas.
4. Crie ou utilize a branch definida pelo fluxo.
5. Faça o commit seguindo o padrão estabelecido.
6. Não faça `push` caso o `MD_GITFLOW.md` determine que essa etapa é responsabilidade do usuário.
7. Não altere ou sobrescreva o histórico do Git sem autorização explícita.

O Git Flow deve ser executado **somente depois que a implementação estiver validada**.

---

# 9. Responsabilidade da IA

A IA é responsável por:

* Analisar o projeto.
* Implementar as alterações.
* Criar e modificar arquivos necessários.
* Executar testes.
* Corrigir erros encontrados.
* Atualizar documentação quando necessário.
* Criar commits conforme o Git Flow definido.
* Informar claramente o resultado da execução.

A IA não deve:

* Fazer `push` sem autorização/regra explícita.
* Alterar configurações fora do escopo sem necessidade.
* Apagar arquivos sem justificativa.
* Criar commits de alterações não relacionadas à tarefa.
* Ignorar instruções presentes nos documentos de referência.
* Considerar uma tarefa concluída sem validação.

---

# 10. Regra para conflitos entre instruções

Caso existam instruções conflitantes:

1. Priorize a solicitação atual do usuário.
2. Depois, considere as regras deste `MASTER.md`.
3. Depois, considere os documentos específicos da etapa.
4. Preserve as regras e padrões existentes do projeto sempre que possível.

Se houver uma ambiguidade que possa causar uma alteração destrutiva ou incompatível, **pare e solicite esclarecimento antes de prosseguir**.

---

# 11. Escopo

A IA deve trabalhar exclusivamente no escopo necessário para atender à solicitação.

Antes de alterar qualquer arquivo, pergunte:

> "Esta alteração é necessária para concluir a tarefa solicitada?"

Se a resposta for não, não faça a alteração.

---

# 12. Relatório final

Ao terminar, apresente um resumo contendo:

### Alterações

* O que foi criado.
* O que foi alterado.
* O que foi removido, caso aplicável.

### Validação

* Testes executados.
* Resultado dos testes.
* Eventuais problemas encontrados e corrigidos.

### Git

* Branch utilizada/criada.
* Commit realizado.
* Se o `push` foi ou não realizado.

O relatório deve ser objetivo e não deve repetir detalhes desnecessários da implementação.

---

# 13. Regra final

Sempre siga este princípio:

```text
ENTENDER → CONSULTAR INSTRUÇÕES → IMPLEMENTAR → TESTAR → DOCUMENTAR → COMMITAR → INFORMAR
```

**Nunca implemente antes de analisar o contexto.**

**Nunca finalize antes de validar.**

**Nunca faça o Git Flow antes de concluir os testes.**

**Sempre consulte o documento específico antes de executar uma etapa que possua regras próprias.**
