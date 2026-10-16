# Instruções Pessoais — Lembrete

> ⚠️ ESTE ARQUIVO É APENAS UM LEMBRETE PESSOAL.
>
> O HARNESS/AGENTE DEVE IGNORAR COMPLETAMENTE ESTE ARQUIVO.
> NÃO LEIA, NÃO ANALISE, NÃO MODIFIQUE E NÃO UTILIZE AS INFORMAÇÕES DESTE ARQUIVO COMO CONTEXTO DO PROJETO.

---

## Fluxo de execução do Harness

### 1. Abrir o projeto

Abrir no VS Code:

`OneDrive/Documentos/projeto_taia`

### 2. Abrir o terminal

Utilizar o terminal **Ubuntu (WSL)** dentro do VS Code.

### 3. Confirmar a pasta

```bash
pwd
```

### 4. Verificar o Git

```bash
git status
```

### 5. Executar o Harness

```bash
opencode
```

### 6. O Harness carrega o projeto

O OpenCode utiliza o workspace e os arquivos de contexto, como:

- `AGENTS.md`
- `CONTEXT.md`
- `README.md`
- `src/`
- `tests/`

### 7. Enviar a tarefa para o agente

Exemplo:

> Analise o projeto, leia AGENTS.md e CONTEXT.md, identifique o que precisa ser feito e execute a tarefa. Antes de alterações importantes, explique o que pretende fazer e execute os testes disponíveis.

### 8. Fluxo interno

```text
USUÁRIO
   ↓
OpenCode
(HARNESS)
   ↓
OpenCode Zen
(PROVIDER)
   ↓
Big Pickle
(MODELO)
   ↓
Análise
   ↓
Planejamento
   ↓
Alteração dos arquivos
   ↓
Execução dos testes
   ↓
Resultado
```

### 9. Encerrar o Harness

```text
Ctrl + C
```

### 10. Verificar alterações

```bash
git status
```

### 11. Visualizar diferenças

```bash
git diff
```

### 12. Versionar as alterações

```bash
git add .
git commit -m "feat: alteração realizada com auxílio de IA"
```

---

## Configuração atual

```text
Sistema: Windows + WSL2
IDE: VS Code

Harness:
OpenCode

Provider:
OpenCode Zen

Modelo:
Big Pickle

Versionamento:
Git
```

---

## Lembrete do fluxo

```text
Abrir VS Code
      ↓
Abrir terminal Ubuntu (WSL)
      ↓
Entrar na pasta do projeto
      ↓
git status
      ↓
opencode
      ↓
Enviar tarefa
      ↓
IA analisa
      ↓
IA planeja
      ↓
IA modifica
      ↓
IA testa
      ↓
Ctrl + C
      ↓
git status
      ↓
git diff
      ↓
git add .
      ↓
git commit
```

> **IMPORTANTE:** Este arquivo é exclusivamente para consulta pessoal e deve ser ignorado pelo Harness.
