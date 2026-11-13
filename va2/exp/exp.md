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

**escrito antes de rodar:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/3403538c009813d65dbdd5d48d7b2cafd8888998

## 3 · E2 · A feirante erra menos... digo, o aluno retém o conhecimento

### 3.1 · hipótese, linhas de base e o número que derruba

**a hipótese:** Ao ser forçado a vocalizar e justificar a arquitetura, o aluno retém o conhecimento, diminuindo a taxa de erros estruturais repetidos ao longo das tarefas.

**o jeito de hoje:** O aluno codifica (ou usa Copilot/ChatGPT) livremente, focando só em fazer o código rodar, sem interrupções reflexivas.

**o competidor mais forte:** *Codswallop* (extensão que dispara um quiz de texto ao detectar Ctrl+V). Ele tenta gerar o mesmo atrito reflexivo, mas permite que o aluno "bule" copiando e colando a resposta. Não roda no piloto pois exige chaves da API do Claude.

**o número que derruba a hipótese:** Se, ao longo de 5 tarefas, a quantidade de erros estruturais repetidos for igual ou a redução for menor que 30% em comparação ao "jeito de hoje".

**escrito antes de rodar:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/3403538c009813d65dbdd5d48d7b2cafd8888998

### 2.2 · métricas e ablação (E1)

| métrica | o que mede | por que esta, e não outra | de onde vem (artigo ou checklist, com link) |
|:--|:--|:--|:--|
| Acurácia (Resposta Exata) | Se o modelo acertou o veredito (Passar ou Barrar) batendo com o gabarito do professor. | Avalia o desempenho bruto do LLM. | [Cong et al., BEA 2026](https://aclanthology.org/2026.bea-1.19/) |
| Falso Negativo (Barrado Injustamente) | O aluno respondeu certo, mas o modelo barrou (por sotaque, transcrição errada, etc). | É a métrica da hipótese. Frustra o usuário e inutiliza a extensão. | O erro silencioso que gera atrito (Baseado em Cong et al.) |
| Falso Positivo (Besteira Aprovada) | O aluno enrolou ou falou errado, e o modelo deixou passar. | O erro que o professor não vê na hora, fraudando a intenção da ferramenta. | O mesmo. |
| Tempo de Processamento | Segundos desde o fim do áudio até o veredito na tela. | Acima de 30s a ferramenta quebra o fluxo de trabalho do desenvolvedor. | Engenharia de Software |

| ablação: o que eu tiro ou troco | o que espero ver | o que ela prova sobre a ideia |
|:--|:--|:--|
| Sem o trecho da AST no prompt | Mais Falsos Positivos e Falsos Negativos (modelo perde contexto). | Que o passo 2 e 3 do flx (ler a AST) não é capricho, é essencial para a IA julgar certo. |
| Trocar o Qwen por Regras de Palavra-Chave (Regex) | Acurácia despenca; aluno engana o sistema falando a palavra sem entender o conceito. | Que o Qwen local se justifica e não pode ser trocado por uma regra de programação (flx passo 7). |
| Trocar Qwen/Whisper por API da OpenAI | Acurácia ligeiramente maior, tempo variando com a rede. | Mostra o custo real (em performance) da escolha pela privacidade 100% local. |

**como vou reportar a incerteza:** Como o Qwen responde com `temperature=0` (sem sorteio de tokens), uma rodada sobre os 30 áudios basta. Reportarei as taxas brutas e o tempo médio.

### 3.2 · métricas e ablação (E2)

| métrica | o que mede | por que esta, e não outra | de onde vem (artigo ou checklist, com link) |
|:--|:--|:--|:--|
| Taxa de Sucesso/Falha da Submissão | Se a arquitetura entregue final possui erros de fundamento. | É a métrica da hipótese (queda nos erros repetidos). | [Edwards, SIGCSE 2004](https://dl.acm.org/doi/10.1145/971300.971312) |
| Tempo extra por tarefa | O custo temporal da interrupção (gravar áudio + esperar). | Se custar caro demais, os alunos vão boicotar o uso. | HCI na Educação |

| ablação: o que eu tiro ou troco | o que espero ver | o que ela prova sobre a ideia |
|:--|:--|:--|
| Condição A: "Jeito de hoje" (Sem a extensão) | Entregas mais rápidas, porém com mais erros estruturais graves/repetidos. | Prova o valor pedagógico da ideia em si (o atrito cognitivo funciona). |
| Omitir o relatório do aluno | Alunos sentem que a ferramenta é só punitiva e não os ajuda a estudar. | O relatório do passo 8 justifica o uso egoísta e voluntário do aluno. |

**como vou reportar a incerteza:** Diferença nas taxas de sucesso (B - A), sem caça a valor-p.

### 2.3 · dados, participantes e ética (E1)

| | resposta |
|:--|:--|
| origem dos dados ou das pessoas | 30 áudios curtos de estudantes de Ciência da Computação explicando trechos de código (arquitetura/mudança vital). No piloto, áudios simulados/gravados por colegas. |
| quantos, e por que esse número | 30 áudios no teste. É o mínimo para calcular uma taxa de 10% de falso negativo no piloto sem que 1 único erro distorça a métrica toda. |
| como é coletado, e quem faz o gabarito | Coletado via microfone do headset no VS Code. O gabarito (se o aluno entendeu ou não) é feito por um avaliador humano (professor/monitor) que escuta os 30 áudios e anota "Passa" ou "Barra". |
| o que separa treino, ajuste e teste | 5 áudios usados para ajustar a rubrica (prompt) do Qwen. 30 áudios novos para o teste, sem o Qwen ou o Whisper terem visto antes. |
| consentimento e comitê de ética | Termo de consentimento (TCLE) apresentado na tela e aceito no próprio áudio pelo participante (Res. CNS 510/2016). Preparado para submissão ao CEP da universidade. |
| dados pessoais: onde ficam e quando somem | Como garantido no fluxograma: o áudio fica na RAM do PC do aluno e é apagado imediatamente após a transcrição. |

### 3.3 · dados, participantes e ética (E2)

| | resposta |
|:--|:--|
| origem dos dados ou das pessoas | Turma de estudantes de programação (ex: alunos de laboratório de programação). |
| quantos, e por que esse número | 6 a 8 participantes no piloto. Design intra-sujeito (quadrado latino): cada um programa metade das tarefas com o Rastro Cognitivo e metade "do jeito de hoje". |
| como é coletado, e quem faz o gabarito | A própria extensão coleta as métricas de tempo e erros de compilação/arquitetura corrigidos. O gabarito final é a nota do projeto dada pelo professor. |
| o que separa treino, ajuste e teste | Não há treino de máquina aqui. Separa-se apenas a lista de tarefas (tarefas A e B têm a mesma dificuldade). |
| consentimento e comitê de ética | O mesmo TCLE do E1, detalhando os riscos de frustração com a ferramenta e a garantia de que a participação não afeta a nota final na disciplina. |
| dados pessoais: onde ficam e quando somem | Apenas as métricas pseudonimizadas vão para o professor. Códigos e áudios não saem da máquina. |

### 2.4 · o piloto: o que rodei, o que deu, o que mudou no desenho

**o script e o commit:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/e951529c9383391eb77f9630751bbead5bb4417b

**a tabela, colada como saiu:**
| ID | Condição | Tempo (s) | Gabarito | Qwen | Resultado |
|:---|:---|---:|:---|:---|:---|
| T1 | Normal | 6.81 | Passar | Passar | ✅ Acerto |
| T2 | Whisper Ruim | 2.87 | Passar | Passar | ✅ Acerto |
| T3 | Normal | 2.45 | Barrar | Barrar | ✅ Acerto |
| T4 | Sem AST | 2.74 | Passar | Passar | ✅ Acerto |

**o que o piloto prova, e o que ele não prova:** O piloto atesta o funcionamento base da ideia, se utilizado de poucos exemplos. Para todos os testes foram respeitados o limite máximo de 30 sec, em realidade, o tempo de execução não passou de 7 sec, possibilitando a geração de novos limites de desempenho melhorado. O testes foram um sucesso, ele barrou e passou as variações de teste com sucesso, para o teste normal, ele funcionou adequandamente, para o teste com falha de detcção correta do wisper, ele ainda sim entendeu o contexto e passo, para o teste normal mais tendo o usuário falado bobagem, ele o barrou, já o teste 4, cabe-se um adendo, mesmo sem ast ele passou, mas porque ? porque não tem contexto o suficente ? porque não a regars claras que exigem a presença de todos os dados ? Cabe-se mais testes para uma respota mais eficais. 

**o que mudou no desenho por causa dele:** Vou ter de melhorar o prompt, principamente nas regras, estipulando que não seja aceita execuções sem ter todo o contexto(ast + transcricao Whisper + regras claras)

### 3.4 · o piloto: o que rodei, o que deu, o que mudou no desenho (E2)

**o script e o commit:** https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/30b51835b30b82683be50d73c2b6823cff38750a

**a tabela, colada como saiu:**
| Condição | T1 | T2 | T3 | T4 | T5 | Total de Erros | Redução T1->T5 |
|:---|---:|---:|---:|---:|---:|---:|---:|
| A: Sem a Extensão | 4 | 4 | 3 | 4 | 4 | 19 | 0 erros |
| B: Com a Extensão | 4 | 3 | 2 | 1 | 0 | 10 | 4 erros |

**o que o piloto prova, e o que ele não prova:** Prova que o protocolo de métricas faz sentido e a matemática do experimento real fecha: capturar os erros tarefa a tarefa permite medir a "Redução T1->T5", que é exatamente o que a hipótese pede. Ele não prova ABSOLUTAMENTE NADA sobre o comportamento de estudantes reais ou se a ideia funciona; os números foram gerados por regras estáticas simulando alunos, apenas para validar a montagem da tabela antes do comitê de ética liberar a pesquisa com humanos.

**o que mudou no desenho por causa dele:** Percebi que olhar o "Total de Erros" não é a melhor métrica para avaliar aprendizado. A ferramenta deve ser julgada pela coluna "Redução T1->T5". O desenho do experimento final focará em comparar se a inclinação de queda dos erros da condição B é pelo menos 30% maior que a da condição A.

## 3 · o que mudou na ideia, sem IA

Até o presado momento, não foi alterado nada na ideia, pois com base no desempenho obtitdo, abre-se a possibilidade (já prevista pois a extensão é modular a depender do hardware) de se usar modelos mais robustos e com isso obter mais desempenho em tempo habio. 

## 4 · auditoria cega

> uma conversa nova, que não ajudou a fazer esta folha, julga cada item de verificação começando
> de "não passa", tenta derrubar cada hipótese e confere cada referência (prompt no passo 6 do
> guia). você cola o veredito dela aqui, sem editar, e responde, sem IA, item por item.

**o veredito da conversa nova** (a tabela item | passa ou não passa | trecho que prova | o que encontrei, colada como veio):

| item | passa ou não passa | trecho que prova | o que encontrei |
|:--|:--|:--|:--|
| 1. hipótese, linha de base e número que derruba, decididos antes | **passa** | § 2.1 e § 3.1 (os limiares e commits). | O artigo de Cong (BEA 2026) e Edwards (SIGCSE 2004) sustentam as métricas. As hipóteses têm risco de falhar (10% de falso negativo; 30 segundos). O competidor do E1 (OpenAI) e E2 (Codswallop) estão corretos. O limiar foi commitado antes do piloto. |
| 2. métricas e ablação, rodadas num piloto | **passa (com alerta)** | § 2.2 (métricas) e § 2.4 (tabela do piloto). | A tabela do piloto saiu do script com o gabarito correto. Porém, a ablação "Sem AST" (T4) resultou em "Passar", o que contraria o esperado em § 2.2 ("espero ver mais falsos positivos"). Isso prova que o LLM atual está avaliando só o texto e ignorando a arquitetura. O item passa porque o autor detectou a falha no texto de análise (§ 2.4) e assumiu que precisa mudar o prompt. |
| 3. dados, participantes e ética | **passa** | § 2.3 e § 3.3. | A quantidade de participantes (30 áudios no E1; 6 a 8 no E2) está justificada e é viável. A separação entre áudios de ajuste e teste está clara. O TCLE foi estruturado conforme LGPD e CNS 510/2016 e os dados ficam apenas na RAM, sendo apagados logo em seguida. Nenhuma persona de IA substituiu o humano na avaliação pedagógica (E2). |

**a minha resposta, sem IA** (uma linha por item: o que mudei por causa da auditoria, e onde; ou por que discordo dela):
1. Concordo com a auditoria, bem exuta, tive algumas duvidas ao decorrer da execução, acerca de é humano que tem de fazer ou não, mas já foram sanadas. As hipóteses, foram testadas e aprovadas e ate com bom desempenho.
2. Concordo com o alerta. Já registrei no passo 3 que vou alterar o Passo 6 do fluxograma para amarrar o prompt com rigor as regras adequadas na leitura da AST.
3. Concordo, a ética e privacidade são os pilares dessa extensão local. Assim que obter aporvaçaõ, partirei para os testes reais.