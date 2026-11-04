# flx · Carlos Eduardo Ribeiro

> folha do artefato [fluxograma e arquitetura](../3-fluxograma-e-arquitetura.md). siga o guia passo
> a passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia e o que eu medi

**Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e exigindo que o aluno justifique a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas da turma.

**o que eu medi no tec:** O modelo rodou local na CPU em uma máquina de 8GB de RAM, levando cerca de 5 a 20 segundos por resposta. Na transcrição, o Whisper small errou a fonética ("estore" em vez de "estoure"). Na avaliação semântica, o Qwen 1.5B (via Ollama) acertou o mérito técnico, mas inventou a palavra "abrições" em vez de "aberturas".

## 1 · o fluxograma

**o diagrama:** [cole aqui o link do seu arquivo arquitetura.md no GitHub após o commit]

| nº | passo | IA, regra ou pessoa | por que IA, e não uma regra (sem IA) |
|:--|:--|:--|:--|
| 1 | Aluno salva o arquivo ou faz o commit com uma alteração no código. | pessoa | |
| 2 | A extensão lê o diff do Git e extrai a Árvore de Sintaxe Abstrata (AST) do código. | regra | |
| 3 | Filtro de mudança vital: compara a AST para ver se há mudança de arquitetura (se não houver, o fluxo segue normal). | regra | |
| 4 | Se houver mudança vital, a IDE pausa e abre o microfone para o aluno justificar a escolha. | pessoa | |
| 5 | O áudio é transcrito para texto (Whisper local). | IA | Nem todo tom de voz é igual (sotaque, velocidade, timbre), o que geraria palavras incorretas se usássemos uma comparação exata de ondas sonoras. |
| 6 | A extensão empacota a transcrição, o trecho da AST e a rubrica do professor num prompt. | regra | |
| 7 | O modelo local (Qwen) avalia se a justificativa prova que o aluno entendeu aquela estrutura. | IA | Buscar palavras-chave fixas não prova entendimento, pois elas podem ser facilmente copiadas ou decoradas. O sistema precisa interpretar a semântica de todo o contexto. |
| 8 | A extensão exibe o veredito na IDE e atualiza o relatório local de evolução do aluno. | regra | |
| 9 | O dashboard consolidado das lacunas é gerado para o professor. | regra | |

