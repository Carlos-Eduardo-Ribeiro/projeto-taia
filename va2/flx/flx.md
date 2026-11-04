# flx · Carlos Eduardo Ribeiro

> folha do artefato [fluxograma e arquitetura](../3-fluxograma-e-arquitetura.md). siga o guia passo
> a passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia e o que eu medi

**Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e exigindo que o aluno justifique a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas da turma.

**o que eu medi no tec:** O modelo rodou local na CPU em uma máquina de 8GB de RAM, levando cerca de 5 a 20 segundos por resposta. Na transcrição, o Whisper small errou a fonética ("estore" em vez de "estoure"). Na avaliação semântica, o Qwen 1.5B (via Ollama) acertou o mérito técnico, mas inventou a palavra "abrições" em vez de "aberturas".

## 1 · o fluxograma

**o diagrama:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/blob/main/va2/flx/arquitetura.md

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

## 2 · as peças: o que entra, o que sai, onde roda e quanto custa

**a escala do custo por mês:** 1 aluno, programando 5 dias por semana, fazendo cerca de 4 mudanças estruturais por dia: 80 justificativas por mês, uns 30 segundos de áudio cada, 40 minutos de áudio mensais.

| peça | entra | sai | onde roda, e por quê | tempo e máquina por uso | R$ por mês na escala | medido ou estimado · fonte e data |
|:--|:--|:--|:--|:--|:--|:--|
| VS Code / Extensão Rastro Cognitivo | alterações no código (diff/AST) e o áudio gravado | veredito exibido na tela e relatórios locais | no PC do aluno: é onde ele já estuda e programa | menos de 1 s, sem usar modelo | 0 | **estimado**: o processamento de regras (AST) é instantâneo |
| Whisper local (modelo small) | o áudio do aluno (~30s) | a justificativa em texto transcrito | no PC do aluno: para proteger a privacidade, funcionar offline de qualquer lugar e não exigir custos em dólar. | 5 a 20 s (junto com a carga do Qwen) em CPU e 8GB de RAM. | 0 | tempo **medido** no tec. RAM **estimada**: o small exige ~2 GB de memória ([tabela oficial do whisper](https://github.com/openai/whisper#available-models-and-languages), 04/11/2026) |
| Qwen2.5-Coder 1.5B (via Ollama) | o texto transcrito, o trecho da AST e a rubrica | o veredito avaliando a compreensão | no PC do aluno: pelos mesmos motivos de privacidade e democratização do acesso. | medido junto ao Whisper (5-20 s na CPU). | 0 | tempo **medido** no tec. RAM **estimada**: ~1.5 GB de memória no disco/RAM. |
| alternativa, não escolhida: nuvem da OpenAI (Whisper API + gpt-4o-mini) | o áudio e a AST | a justificativa transcrita e o veredito | servidor da OpenAI | dependeria 100% da velocidade da internet do aluno | ~US$ 0,25 (40 min de whisper a US$ 0,006 + ~80k tokens a US$ 0,150/1M): menos de R$ 2 por mês. | **estimado**: [openai.com/api/pricing](https://openai.com/api/pricing/), 04/11/2026. A cobrança é por minuto e token; provando que o motivo da IA local é a privacidade, não o custo. |

## 3 · a arquitetura: onde roda cada peça e para onde vão os dados

**o diagrama, com as caixas de onde cada peça roda:** [cole o link do commit do arquitetura.md aqui]

| dado pessoal | de quem é | onde fica | quem vê | por quanto tempo | quando é apagado |
|:--|:--|:--|:--|:--|:--|
| áudio da justificativa (voz) | do aluno | memória RAM do PC do aluno | ninguém (só o Whisper processa) | segundos | imediatamente após a transcrição |
| código-fonte (diff/AST) | do aluno | PC do aluno | o modelo local (Qwen) | segundos (durante o prompt) | apagado da extensão logo após gerar o veredito |
| métricas de desempenho (lacunas, entendimento, tempo) | do aluno | arquivo local e e-mail do professor | o aluno e o professor | até o fim da disciplina/semestre | no final do ciclo letivo |

**o que sai do aparelho de quem usa, e para onde:** O que sai são apenas as métricas obtidas através das análises da resposta do aluno (nível de entendimento, tempo, dificuldades mapeadas). Elas vão para o e-mail configurado do professor (que pode dar acesso a uma plataforma). O áudio da voz e o código-fonte do aluno nunca saem do PC.

**o mínimo que a ideia precisa guardar:** Apenas os dados relativos ao desempenho e progresso de aprendizagem do aluno para compor o relatório.