# Git Workflow — Padrão de Versionamento

## 1. Objetivo

Este documento define o padrão de versionamento utilizado no projeto, incluindo:

* branches;
* commits;
* Pull Requests;
* merge;
* sincronização com o GitHub;
* organização do histórico;
* regras específicas para o Harness.

O objetivo é manter um histórico limpo, rastreável e padronizado, garantindo que todas as alterações realizadas pelo Harness sejam registradas no Git.

---

# 2. Estrutura de Branches

O desenvolvimento do projeto será realizado diretamente na branch `develop`.

```text
main
 │
 └── develop
       │
       ├── desenvolvimento
       ├── correções
       ├── refatorações
       ├── documentação
       └── testes
```

## Branch `main`

Branch principal e estável do projeto.

Não realizar desenvolvimento diretamente nela.

Alterações devem chegar à `main` por meio de Pull Request a partir da `develop`.

## Branch `develop`

Branch principal de desenvolvimento e integração do projeto.

**O Harness deve realizar suas alterações diretamente na `develop`.**

Não é necessário criar uma branch `feature/*`, `fix/*`, `refactor/*` ou equivalente para alterações realizadas pelo Harness, salvo quando o usuário solicitar explicitamente.

---

# 3. Fluxo padrão de desenvolvimento

```text
main
 ↓
develop
 ↓
analisar
 ↓
implementar alteração
 ↓
testar
 ↓
git diff
 ↓
commit
 ↓
push
 ↓
próxima alteração
```

O desenvolvimento realizado pelo Harness deve permanecer na `develop`.

Quando uma alteração estiver concluída e a `develop` estiver pronta para publicação, poderá ser aberto um Pull Request:

```text
develop
   ↓
Pull Request
   ↓
Code Review
   ↓
main
```

---

# 4. Iniciando uma tarefa

Antes de iniciar uma nova tarefa, o Harness deve garantir que está na `develop` atualizada:

```bash
git switch develop
git pull origin develop
```

Depois deve verificar o estado do repositório:

```bash
git status
git branch
git diff
```

Se existirem alterações locais não realizadas pelo Harness, elas devem ser preservadas.

O Harness não deve sobrescrever alterações existentes sem autorização.

---

# 5. Antes de modificar arquivos

O Harness deve:

1. analisar o estado atual do projeto;
2. verificar a branch atual;
3. verificar alterações pendentes;
4. ler os arquivos de contexto relevantes;
5. entender a tarefa;
6. identificar os arquivos que precisam ser alterados;
7. evitar sobrescrever alterações existentes.

Comandos mínimos:

```bash
git status
git branch
git diff
```

---

# 6. Durante o desenvolvimento

O Harness deve:

* trabalhar diretamente na `develop`;
* preservar alterações existentes;
* evitar alterações desnecessárias;
* modificar somente arquivos relacionados à tarefa;
* executar testes quando disponíveis;
* informar problemas encontrados;
* criar um commit após cada alteração lógica concluída;
* realizar `push` após cada commit realizado.

### Regra obrigatória

**Toda vez que o Harness realizar uma alteração no projeto, essa alteração deve ser registrada em um commit e enviada para o GitHub.**

Fluxo:

```text
Modificar
   ↓
Testar
   ↓
git diff
   ↓
git status
   ↓
git add
   ↓
git commit
   ↓
git push
```

O Harness **não deve acumular diversas alterações independentes sem commit e push**.

---

# 7. Commits

Utilizar **Conventional Commits**.

Formato:

```text
tipo: descrição
```

Tipos permitidos:

```text
feat      → nova funcionalidade
fix       → correção de bug
refactor  → refatoração
docs      → documentação
test      → testes
chore     → manutenção/configuração
build     → alterações de build/dependências
perf      → melhoria de desempenho
ci        → configuração de CI/CD
```

Exemplos:

```bash
git commit -m "feat: adicionar processamento de dados"
```

```bash
git commit -m "fix: corrigir validação dos dados"
```

```bash
git commit -m "docs: atualizar documentação do projeto"
```

```bash
git commit -m "test: adicionar testes para processamento"
```

```bash
git commit -m "refactor: reorganizar serviço de processamento"
```

---

# 8. Regras para commits

Os commits devem:

* representar uma alteração lógica;
* ser pequenos e objetivos;
* utilizar mensagens claras;
* não misturar alterações não relacionadas;
* não incluir arquivos desnecessários;
* ser realizados após cada alteração significativa feita pelo Harness.

Evitar:

```text
update
mudanças
teste
coisas
final
final2
corrigido
```

Preferir:

```text
feat: adicionar processamento de dados

fix: corrigir tratamento de valores nulos

test: adicionar testes de validação

docs: documentar instalação do projeto
```

---

# 9. Antes de cada commit

Sempre verificar:

```bash
git status
```

Depois:

```bash
git diff
```

O Harness deve verificar se somente os arquivos esperados foram modificados.

Executar os testes disponíveis.

Somente depois:

```bash
git add .
```

Criar o commit:

```bash
git commit -m "tipo: descrição"
```

E imediatamente realizar:

```bash
git push origin develop
```

---

# 10. Regra de Commit e Push do Harness

Esta é uma regra obrigatória do workflow.

Sempre que o Harness modificar o projeto:

```text
ALTERAÇÃO
   ↓
TESTE
   ↓
REVISÃO DO DIFF
   ↓
COMMIT
   ↓
PUSH PARA DEVELOP
```

Exemplo:

```bash
git add arquivo.py
git commit -m "feat: adicionar processamento de avaliações"
git push origin develop
```

Após o `push`, o Harness deve verificar novamente o estado do repositório:

```bash
git status
```

O objetivo é manter o GitHub constantemente sincronizado com o estado válido mais recente do desenvolvimento.

---

# 11. Push para o GitHub

Como o desenvolvimento ocorre diretamente na `develop`, o push padrão será:

```bash
git push origin develop
```

Após o primeiro push da branch, caso necessário:

```bash
git push -u origin develop
```

Nas próximas atualizações:

```bash
git push origin develop
```

O Harness não deve realizar `push --force`.

---

# 12. Pull Request

O desenvolvimento cotidiano não exige Pull Request entre branches.

As alterações realizadas pelo Harness são enviadas diretamente para:

```text
develop
```

Quando a versão da `develop` estiver pronta para integração com a versão estável:

```text
develop
   ↓
Pull Request
   ↓
Code Review
   ↓
main
```

O Pull Request deve informar:

### O que foi feito?

Descrição objetiva das alterações.

### Por que foi feito?

Problema ou objetivo da alteração.

### Como foi testado?

Informar os testes executados.

### Principais alterações

Listar os arquivos ou componentes relevantes.

---

# 13. Merge

Não realizar merge diretamente de alterações de desenvolvimento para `main` sem revisão.

Fluxo:

```text
develop
   ↓
Pull Request
   ↓
Code Review
   ↓
main
```

Antes do merge:

* verificar testes;
* verificar conflitos;
* revisar alterações;
* revisar commits;
* confirmar que a funcionalidade está funcionando.

---

# 14. Sincronização

Antes de iniciar uma nova tarefa:

```bash
git switch develop
git pull origin develop
```

Antes de continuar um trabalho:

```bash
git status
git fetch origin
```

Caso existam atualizações remotas relevantes, sincronizar a `develop` antes de continuar.

---

# 15. Arquivos que NÃO devem ser versionados

Nunca adicionar:

```text
.env
.env.*
*.key
*.pem
credentials.*
secrets.*
__pycache__/
.venv/
venv/
node_modules/
dist/
build/
```

Informações sensíveis nunca devem ser enviadas para o GitHub.

---

# 16. `.gitignore`

O projeto deve possuir um `.gitignore` adequado à tecnologia utilizada.

Exemplo para Python:

```gitignore
__pycache__/
*.py[cod]

.venv/
venv/
env/

.env
.env.*

.pytest_cache/
.mypy_cache/

dist/
build/
*.egg-info/

.vscode/
.idea/

.DS_Store
Thumbs.db
```

---

# 17. Regras específicas para o Harness

O Harness deve considerar este documento como referência obrigatória para o processo de versionamento.

### O Harness DEVE:

* trabalhar na branch `develop`;
* verificar `git status` antes de iniciar alterações;
* verificar a branch atual;
* preservar alterações existentes;
* analisar o `git diff`;
* testar as alterações quando possível;
* criar um commit após cada alteração lógica realizada;
* utilizar Conventional Commits;
* realizar `push` para `origin develop` após cada commit;
* verificar o estado do repositório após o push;
* manter o GitHub sincronizado com as alterações realizadas.

### O Harness NÃO DEVE:

* criar branches de trabalho sem autorização;
* apagar branches sem autorização;
* sobrescrever alterações locais;
* criar commits com alterações não relacionadas;
* acumular alterações independentes sem commit;
* fazer force push;
* alterar histórico sem autorização;
* enviar credenciais ou secrets;
* executar operações destrutivas sem autorização.

---

# 18. Comandos perigosos

Não executar automaticamente:

```bash
git reset --hard
git clean -fd
git push --force
git push --force-with-lease
git branch -D
```

Esses comandos somente devem ser utilizados quando o usuário autorizar explicitamente.

---

# 19. Fluxo completo do Harness

```text
1. git switch develop
        ↓
2. git pull origin develop
        ↓
3. git status
        ↓
4. Analisar projeto
        ↓
5. Planejar alteração
        ↓
6. Implementar
        ↓
7. Executar testes
        ↓
8. git diff
        ↓
9. git status
        ↓
10. git add
        ↓
11. git commit
        ↓
12. git push origin develop
        ↓
13. git status
        ↓
14. Continuar próxima alteração
```

Caso a tarefa envolva várias alterações lógicas independentes:

```text
Alteração 1
   ↓
Commit
   ↓
Push

Alteração 2
   ↓
Commit
   ↓
Push

Alteração 3
   ↓
Commit
   ↓
Push
```

---

# 20. Regra principal

```text
ANALISAR
   ↓
PLANEJAR
   ↓
IMPLEMENTAR
   ↓
TESTAR
   ↓
REVISAR
   ↓
COMMITAR
   ↓
PUSH PARA DEVELOP
   ↓
CONTINUAR
```

A regra central é:

> **O Harness desenvolve diretamente na `develop` e toda alteração realizada por ele deve ser registrada em um commit e enviada imediatamente para o GitHub através de `push` para `origin develop`.**

O histórico do Git deve permitir entender claramente:

* o que foi alterado;
* por que foi alterado;
* quando foi alterado;
* qual alteração originou o commit;
* quais mudanças foram realizadas pelo Harness.
