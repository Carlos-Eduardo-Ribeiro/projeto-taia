# flx · Carlos Eduardo Ribeiro

> folha do artefato [fluxograma e arquitetura](../3-fluxograma-e-arquitetura.md). siga o guia passo
> a passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia e o que eu medi

**Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e emitindo um alerta não-intrusivo para o aluno justificar a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas e dos alertas ignorados da turma.

**o que eu medi no tec:** O modelo rodou local na CPU em uma máquina de 8GB de RAM, levando cerca de 5 a 20 segundos por resposta. Na transcrição, o Whisper small errou a fonética ("estore" em vez de "estoure"). Na avaliação semântica, o Qwen 1.5B (via Ollama) acertou o mérito técnico, mas inventou a palavra "abrições" em vez de "aberturas".

## 1 · o fluxograma

**o diagrama:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/blob/main/va2/flx/arquitetura.md

| nº | passo | IA, regra ou pessoa | por que IA, e não uma regra (sem IA) |
|:--|:--|:--|:--|
| 1 | Aluno salva o arquivo ou faz o commit com uma alteração no código. | pessoa | |
| 2 | A extensão lê o diff do Git e extrai a Árvore de Sintaxe Abstrata (AST) do código. | regra | |
| 3 | Filtro de mudança vital: compara a AST para ver se há mudança de arquitetura (se não houver, o fluxo segue normal). | regra | |
| 4 | Se houver mudança vital, a IDE emite um alerta solicitando o áudio. O aluno pode gravar ou ignorar. | pessoa | |
| 5 | O áudio é transcrito para texto (Whisper local). | IA | Nem todo tom de voz é igual (sotaque, velocidade, timbre), o que geraria palavras incorretas se usássemos uma comparação exata de ondas sonoras. |
| 6 | A extensão empacota a transcrição, o trecho da AST e a rubrica do professor num prompt. | regra | |
| 7 | O modelo local (Qwen) avalia se a justificativa prova que o aluno entendeu aquela estrutura. | IA | Buscar palavras-chave fixas não prova entendimento, pois elas podem ser facilmente copiadas ou decoradas. O sistema precisa interpretar a semântica de todo o contexto. |
| 8 | A extensão exibe o veredito na IDE e atualiza o relatório local de evolução do aluno (contabilizando também alertas ignorados). | regra | |
| 9 | O dashboard consolidado das lacunas e de alertas ignorados é gerado para o professor. | regra | |

## 2 · as peças: o que entra, o que sai, onde roda e quanto custa

**a escala do custo por mês:** 1 aluno, programando 5 dias por semana, fazendo cerca de 4 mudanças estruturais por dia: 80 justificativas por mês, uns 30 segundos de áudio cada, 40 minutos de áudio mensais.

| peça | entra | sai | onde roda, e por quê | tempo e máquina por uso | R$ por mês na escala | medido ou estimado · fonte e data |
|:--|:--|:--|:--|:--|:--|:--|
| VS Code / Extensão Rastro Cognitivo | alterações no código (diff/AST) e o áudio gravado | veredito exibido na tela e relatórios locais | no PC do aluno: é onde ele já estuda e programa | menos de 1 s, sem usar modelo | 0 | **estimado**: o processamento de regras (AST) é instantâneo |
| Whisper local (modelo small) | o áudio do aluno (~30s) | a justificativa em texto transcrito | no PC do aluno: para proteger a privacidade, funcionar offline de qualquer lugar e não exigir custos em dólar. | 5 a 20 s (junto com a carga do Qwen) em CPU e 8GB de RAM. | 0 | tempo **medido** no tec. RAM **estimada**: o small exige ~2 GB de memória ([tabela oficial do whisper](https://github.com/openai/whisper#available-models-and-languages), 04/11/2026) |
| Qwen2.5-Coder 1.5B (via Ollama) | o texto transcrito, o trecho da AST e a rubrica | o veredito avaliando a compreensão | no PC do aluno: pelos mesmos motivos de privacidade e democratização do acesso. | medido junto ao Whisper (5-20 s na CPU). | 0 | tempo **medido** no tec. RAM **estimada**: ~1.5 GB de memória no disco/RAM. |
| alternativa, não escolhida: nuvem da OpenAI (Whisper API + gpt-4o-mini) | o áudio e a AST | a justificativa transcrita e o veredito | servidor da OpenAI | dependeria 100% da velocidade da internet do aluno | ~US$ 0,25 (40 min de whisper a US$ 0,006 + ~80k tokens a US$ 0,150/1M): menos de R$ 2 por mês. | **estimado**: [openai.com/api/pricing](https://openai.com/api/pricing/), 04/11/2026. A cobrança é por minuto e token; provando que o motivo da IA local é a privacidade, não o custo. |

## 3 · a arquitetura: onde roda cada peça e para onde vão os dados

**o diagrama, com as caixas de onde cada peça roda:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/blob/main/va2/flx/arquitetura.md

| dado pessoal | de quem é | onde fica | quem vê | por quanto tempo | quando é apagado |
|:--|:--|:--|:--|:--|:--|
| áudio da justificativa (voz) | do aluno | memória RAM do PC do aluno | ninguém (só o Whisper processa) | segundos | imediatamente após a transcrição |
| código-fonte (diff/AST) | do aluno | PC do aluno | o modelo local (Qwen) | segundos (durante o prompt) | apagado da extensão logo após gerar o veredito |
| métricas de desempenho (lacunas, entendimento, tempo, alertas ignorados) | do aluno | arquivo local e e-mail do professor | o aluno e o professor | até o fim da disciplina/semestre | no final do ciclo letivo |

**o que sai do aparelho de quem usa, e para onde:** O que sai são apenas as métricas obtidas através das análises da resposta do aluno (nível de entendimento, tempo, dificuldades mapeadas e alertas ignorados). Elas vão para o e-mail configurado do professor (que pode dar acesso a uma plataforma). O áudio da voz e o código-fonte do aluno nunca saem do PC.

**o mínimo que a ideia precisa guardar:** Apenas os dados relativos ao desempenho e progresso de aprendizagem do aluno para compor o relatório.

## 4 · o que mudou na ideia, sem IA

No meu brw.md, eu ainda estava decidindo como avaliar a mudança do código. Desenhando o fluxograma hoje (Passo 1), percebi que extrair a AST e achar a mudança estrutural virou uma REGRA determinística (Passos 2 e 3) em vez de gastar processamento de IA. Além disso, cravei que a voz e o código não são guardados, morrem no PC, e só a "métrica" sai por e-mail para o professor.

## 5 · auditoria cega

> uma conversa nova, que não ajudou a fazer esta folha, julga cada item de verificação começando
> de "não passa", abre os links de preço e tenta trocar cada IA por uma regra (prompt no passo 5 do
> guia). você cola o veredito dela aqui, sem editar, e responde, sem IA, item por item.

**o veredito da conversa nova** (a tabela item | passa ou não passa | trecho que prova | o que encontrei, colada como veio):

| item | passa ou não passa | trecho que prova | o que encontrei (links abertos, regras tentadas) |
|:--|:--|:--|:--|
| 1 · fluxograma (IA, regra ou pessoa) | passa | § 1 e `arquitetura.md`: fluxo começa em `"1. Aluno salva/commita"` e vai até `"8. Exibe veredito..."` e `"9. Gera dashboard..."`. Passos IA (5 e 7) possuem justificativas claras. | Tentei criar regras para os passos IA. Regra de comparação de ondas sonoras para o Passo 5 não passa porque, como a folha aponta: `"Nem todo tom de voz é igual (sotaque, velocidade, timbre)"`. Regra de regex/palavras-chave para o Passo 7 não passa pois: `"Buscar palavras-chave fixas não prova entendimento"`. As justificativas sustentam a necessidade de IA. |
| 2 · entradas, saídas, onde roda e custo | passa | § 2: A escala está clara (`"80 justificativas por mês, uns 30 segundos..."`). Custos detalham origem: `"tempo medido no tec"`, `"RAM estimada"`, `"estimado: openai.com/api/pricing"`. | Abri `github.com/openai/whisper#available-models-and-languages`: bate corretamente, o modelo `small` exige ~2 GB de RAM. Abri `openai.com/api/pricing`: a estimativa da alternativa em nuvem de ~US$ 0,25 está correta (US$ 0,006/min no Whisper). A justificativa de local vs nuvem não usa preço falso, baseia-se corretamente na necessidade de privacidade e uso offline. |
| 3 · arquitetura, dados e privacidade | passa | § 3 e `arquitetura.md`: O diagrama tem as caixas separando o `"PC do Aluno"` e o `"Servidor"`. A tabela mapeia `"áudio"`, `"código-fonte"` e `"métricas"`, com destinações exatas (`"RAM"`, `"e-mail"`) e tempos de retenção (`"segundos"`, `"final do ciclo"`). | O texto explicita que `"o áudio da voz e o código-fonte do aluno nunca saem do PC"`, enviando só as métricas para o professor. A folha não cai na armadilha do exemplo raso de usar termos vazios como "os dados estão seguros". A retenção é condizente com a operação. |

**a minha resposta, sem IA** (uma linha por item: o que mudei por causa da auditoria, e onde; ou por que discordo dela):
1. Concordo com a auditoria, as justificativas para usar IA estão corretas e necessárias, logo, não precisei mudar o fluxograma;
2. Concordo com a auditoria, os custos e a escala de uso foram acessadas e checadas, estão corretas;
3. Concordo, o diagrama e a tabela de dados garantem a privacidade do estudante. Nenhum dado além dos necessários(as métricas) saem do pc.
