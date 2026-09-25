# Git Workflow --- Padrão de Mercado (Gitflow)

## Objetivo

Este documento define o fluxo de versionamento padrão de mercado (Gitflow adaptado) para o projeto. 

O **OpenCode (Harness)** tem AUTONOMIA TOTAL para realizar o ciclo completo de versionamento:
1. Atualizar as ramificações locais;
2. Criar a branch de trabalho adequada (`feature/`, `bugfix/`, etc.);
3. Implementar as alterações e testes;
4. Criar os commits;
5. **Realizar o PUSH para o repositório remoto (GitHub)**.

## 1. Estrutura de Branches

Adotamos a seguinte estrutura de ramificações:

- `main`: Representa o código em produção/versão estável. Nunca recebe commits diretos.
- `develop`: Branch de integração principal que contém os próximos lançamentos.
- `feature/*`: Ramificações temporárias criadas a partir de `develop` para desenvolver novas funcionalidades.
- `bugfix/*` ou `hotfix/*`: Para correções de bugs.

```text
main
  ↑ (Pull Request)
develop
  │
  ├── feature/nova-funcionalidade
  ├── bugfix/correcao-erro
  └── refactor/melhoria-codigo
```

## 2. Fluxo Obrigatório do OpenCode

Para cada nova tarefa solicitada, o OpenCode deve seguir este fluxo autonomamente:

1. **Atualizar Develop:** 
   ```bash
   git switch develop
   git pull origin develop
   ```
2. **Criar Branch de Trabalho:** Criar a ramificação específica para a tarefa a partir da `develop`.
   ```bash
   git checkout -b feature/nome-da-tarefa
   ```
3. **Implementar e Testar:** Fazer a codificação, criar arquivos e rodar testes locais.
4. **Commit:** Agrupar lógicas concluídas em commits usando o padrão **Conventional Commits** (`feat:`, `fix:`, `docs:`, `refactor:`, etc.).
   ```bash
   git add .
   git commit -m "feat: adicionar nova arquitetura"
   ```
5. **Push Remoto:** O OpenCode deve realizar o push ativamente da branch para o GitHub.
   ```bash
   git push -u origin feature/nome-da-tarefa
   ```

*(Nota: O usuário será o responsável apenas por aprovar o Pull Request de `feature/*` para `develop` no próprio GitHub, ou pedir ao OpenCode para aplicar o merge localmente se desejar).*

## 3. Segurança

- **Push automático está PERMITIDO e é OBRIGATÓRIO** para as branches de trabalho (ex: `feature/*`, `develop`).
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

> **O OpenCode é totalmente responsável e autorizado a analisar, ramificar, codificar, commitar e FAZER O PUSH para o GitHub nas branches de feature e develop. A entrega final de uma tarefa é sinalizada pelo `push` concluído com sucesso na branch.**