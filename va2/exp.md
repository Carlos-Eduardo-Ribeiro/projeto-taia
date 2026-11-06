# exp · Carlos Eduardo Ribeiro

> folha do artefato [desenho dos experimentos](../3-desenho-dos-experimentos.md). siga o guia passo
> a passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia, e o que ficou para medir

**Rastro Cognitivo (Edge AI Edition):** Uma extensão do VS Code 100% local. Ela lê diffs do Git e a AST, detectando mudanças estruturais e exigindo que o aluno justifique a arquitetura em áudio. O Qwen2.5-Coder e o Whisper (via llama.cpp/Edge AI) transcrevem e avaliam a compreensão com uma rubrica semântica. O aluno ganha um relatório local de evolução, e o professor recebe um dashboard das lacunas da turma.

**o que eu medi no tec:** O modelo rodou local na CPU (8GB RAM), levando de 5 a 20 s por resposta. Na transcrição, o Whisper small errou a fonética ("estore" em vez de "estoure"). O Qwen 1.5B acertou o mérito técnico do áudio, mas inventou a palavra "abrições".

**o que o flx e o tec deixaram para o experimento:** A avaliação do tec não injetou a AST no prompt e testou apenas o caso positivo (aluno acertando). Falta provar se o Qwen consegue discriminar a compreensão real (se ele barra o aluno falando bobagem) e quantos falsos-negativos (barrar um aluno que entendeu, por erro do Whisper ou do Qwen) ocorrem. E o tempo de transcrição + avaliação precisa ser testado no fluxo real para ver se não quebra a experiência do usuário.

**os meus competidores mais próximos:** Codswallop (atua no Ctrl+V, mas usa texto na nuvem, permitindo fraude) e Viva (avaliação oral, mas ocorre só no fim do projeto via nuvem).

## 1 · os experimentos e a comunidade de cada um

| exp. | a pergunta que ele responde | o que é testado | a comunidade e os veículos | o experimento publicado que eu sigo (com link) |
|:--|:--|:--|:--|:--|
| E1 | O LLM consegue distinguir com precisão um entendimento real de uma fala vazia/errada, mesmo com falhas de transcrição? | A técnica (IA) | PLN e IA na Educação (ACL, BEA, EMNLP) | [Estimating LLM Grading Ability](https://aclanthology.org/2026.bea-1.19/) (Cong et al., BEA 2026): Avalia o uso de LLMs para corrigir respostas curtas de alunos, medindo as taxas de acerto e erros (falsos-positivos/negativos) em milhares de casos. |
| E2 | A interrupção para reflexão por áudio diminui os erros estruturais do aluno em relação a apenas colar o código de IA? | Uma pessoa usando no nicho (Educação) | Educação em Computação (SIGCSE, ITiCSE, CHI) | [Trial-and-error to reflection-in-action](https://dl.acm.org/doi/10.1145/971300.971312) (Edwards, SIGCSE 2004): Introduz uma "fricção/restrição" na IDE de dezenas de alunos e compara a taxa de sucesso das submissões contra o método de tentativa e erro. |

## 2 · E1 · O Qwen julga certo e rápido

### 2.1 · hipótese, linhas de base e o número que derruba

**a hipótese:** Lendo a AST e a transcrição, a extensão consegue discriminar o entendimento real sem travar o fluxo: no máximo 10% de alunos barrados injustamente (falso negativo) e resposta em até 30 segundos.

**o jeito de hoje:** Não há avaliação na IDE. O aluno cola o código, a IDE aceita, e o professor tem que ler tudo depois para tentar descobrir quem entendeu.

**o competidor mais forte:** Nuvem da OpenAI (Whisper API + gpt-4o-mini). Roda nos mesmos casos, mas depende de internet e manda o código do aluno para servidores externos.

**o número que derruba a hipótese:** Mais de 10% de falsos negativos (barrar áudio de quem entendeu) ou tempo médio de processamento acima de 30 segundos, avaliando 30 áudios.

**escrito antes de rodar:** [link do commit com a hipótese e o limiar, anterior ao do piloto]

## 3 · E2 · A feirante erra menos... digo, o aluno retém o conhecimento

### 3.1 · hipótese, linhas de base e o número que derruba

**a hipótese:** Ao ser forçado a vocalizar e justificar a arquitetura, o aluno retém o conhecimento, diminuindo a taxa de erros estruturais repetidos ao longo das tarefas.

**o jeito de hoje:** O aluno codifica (ou usa Copilot/ChatGPT) livremente, focando só em fazer o código rodar, sem interrupções reflexivas.

**o competidor mais forte:** *Codswallop* (extensão que dispara um quiz de texto ao detectar Ctrl+V). Ele tenta gerar o mesmo atrito reflexivo, mas permite que o aluno "bule" copiando e colando a resposta. Não roda no piloto pois exige chaves da API do Claude.

**o número que derruba a hipótese:** Se, ao longo de 5 tarefas, a quantidade de erros estruturais repetidos for igual ou a redução for menor que 30% em comparação ao "jeito de hoje".

**escrito antes de rodar:** [link do mesmo commit usado no E1]