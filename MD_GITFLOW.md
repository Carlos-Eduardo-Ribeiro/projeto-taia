# Git Workflow --- Fluxo Simplificado (develop → main)

## Objetivo

Este documento define o fluxo de versionamento do projeto: **todo o trabalho é feito diretamente na `develop`** e a entrega à `main` ocorre por **Pull Request (PR)**, analisado e aprovado pelo usuário no GitHub.

**NÃO são criadas branches por recurso/atualização** (`feature/`, `bugfix/`, `refactor/` etc.).

O **OpenCode (Harness)** tem AUTONOMIA para:
1. Atualizar a `develop` local;
2. Implementar as alterações e testes diretamente na `develop`;
3. Criar os commits;
4. **Realizar o PUSH da `develop` para o GitHub**;
5. **Abrir/solicitar o Pull Request `develop` → `main`** para o usuário analisar.

## 1. Estrutura de Branches

Apenas duas branches permanentes:

- `main`: Código em produção/versão estável. **Nunca recebe commits diretos**; só recebe merge via PR aprovado pelo usuário.
- `develop`: Branch de trabalho e integração. Todas as modificações são feitas aqui.

```text
main
  ↑ (Pull Request aprovado pelo usuário no GitHub)
develop   ← todos os commits são feitos diretamente aqui
```

## 2. Fluxo Obrigatório do OpenCode

Para cada tarefa solicitada, o OpenCode deve seguir este fluxo autonomamente:

1. **Atualizar Develop:**
   ```bash
   git switch develop
   git pull origin develop
   ```
2. **Implementar e Testar:** Fazer a codificação, criar arquivos e rodar testes locais **na própria `develop`** (sem criar nova branch).
3. **Commit:** Agrupar lógicas concluídas em commits usando o padrão **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, etc.).
   ```bash
   git add <arquivos-relevantes>
   git commit -m "feat: adicionar nova arquitetura"
   ```
4. **Push Remoto:** Enviar a `develop` ao GitHub.
   ```bash
   git push origin develop
   ```
5. **Solicitar Merge para a Main:** Abrir um Pull Request `develop` → `main` (pelo GitHub ou `gh pr create --base main --head develop`), com título e descrição resumindo as alterações. Se já houver um PR aberto, o novo push o atualiza automaticamente.

*(Nota: O usuário é o responsável por analisar as alterações e **aprovar o merge** do PR `develop` → `main` no próprio GitHub. O OpenCode nunca faz merge na `main` por conta própria.)*

## 3. Segurança

- **Push automático está PERMITIDO e é OBRIGATÓRIO** para a branch `develop`.
- **Push direto na `main` é PROIBIDO**: a `main` só é atualizada via merge de PR aprovado pelo usuário.
- O OpenCode continua NÃO devendo executar, salvo solicitação explícita:
  ```bash
  git reset --hard
  git push --force
  git branch -D
  ```

- Arquivos pesados, credenciais e lixo local nunca devem ser commitados:
  ```text
  .env*
  *.key
  __pycache__/
  .venv/
  data/raw/
  ```

## 4. Regra Principal Atualizada

> **O OpenCode trabalha somente na `develop`: analisa, codifica, commita, FAZ O PUSH para o GitHub e solicita o Pull Request `develop` → `main`. A aprovação do merge na `main` é exclusiva do usuário. A entrega de uma tarefa é sinalizada pelo `push` concluído na `develop` e pelo PR aberto/atualizado.**