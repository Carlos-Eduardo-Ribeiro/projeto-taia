# MD_TESTES — Regras de Testes e Validação

Documento de instrução do workspace `projeto_taia`. Define como a IA deve testar e
validar alterações antes de concluir qualquer tarefa.

## 1. Princípio

> Nenhuma implementação é considerada concluída sem validação executável.

A IA deve **sempre**:

1. Executar os testes relevantes ao que foi modificado.
2. Verificar erros de compilação/importação, execução ou integração.
3. Validar que a alteração atende à solicitação original.
4. Corrigir problemas e **re-executar** os testes após as correções.

## 2. O que testar

### Código Python / pipelines

- Importação de módulos sem erro.
- Execução do script/fluxo de entrada até o fim.
- Shapes/dtypes das saídas coerentes com o esperado.
- Consistência de métricas calculadas por partes independentes.
- Ausência de dependências faltantes no `.venv` global.

### Dados

- Containers existem e têm as dimensões descritas.
- Ausência de NaN onde não é esperado.
- Divisões treino/validação/teste sem sobreposição (quando garantida por índices).
- Domínio das variáveis alvo (ex.: binário 0/1).

### Experimentos / modelo

- Reprodução roda com seed fixa.
- Números reportados são recuperáveis de artefatos salvos (`.npz`/`.json`).
- Métricas do artigo X métricas da reprodução são diferenciadas no relatório.

### Git

- O MD_GITFLOW define as etapas de versionamento — **neste projeto a etapa de
  Git Flow é executada somente quando solicitada pelo usuário**.

## 3. Estruturas de teste recomendadas

- Scripts executáveis em `projeto_N/experiments/` com saída reproduzível.
- Validação por *smoke test* (ex.: shape forward) em cada modelo novo.
- Validação cruzada de métricas: recomputar células a partir dos `.npz`.

## 4. Registro

Resultados de teste devem ser registrados no relatório técnico da tarefa
(seção Validação) com:

- testes executados;
- resultado de cada teste;
- problemas encontrados e como foram corrigidos.

## 5. Regras anti-fraude

- Não reportar números que não aparecem nos arquivos de resultado.
- Não "passar" um teste que depende de caminho de arquivo não existente.
- Se não for possível executar, escrever explicitamente: *não verificado*.