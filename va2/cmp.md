# cmp · Carlos Eduardo Ribeiro

> folha do artefato [competidores e contribuição](../3-competidores-e-contribuicao.md). siga o guia
> passo a passo. **abra cada link**: a IA inventa referências.

## 0 · a minha ideia completa

**Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e exigindo que o aluno justifique a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas da turma.

## 1 · a ficha da ideia

- **cenário:** Ambientes de prática de programação (laboratórios de faculdade e estudo autônomo).
- **usuário:** Estudantes de computação/programação e seus professores.
- **problema do usuário:** Alunos entregam códigos gerados por IA sem entender a lógica; o professor não tem garantia da autoria cognitiva do aluno.
- **tecnologia:** Extensão de VS Code local (SLM + Whisper) baseada em leitura de AST/Git Diff.

## 2 · catálogo de ferramentas

ficha: **C**enário · **U**suário · **P**roblema · **T**ecnologia, cada um **=** igual, **≈** parecido ou **≠** diferente.

| ferramenta | o que faz | no que é bom | onde falha | C U P T |
|:--|:--|:--|:--|:-:|
| **[Viva](https://vivaproof.com/)** | Aceita código final (ex: notebook.ipynb) e faz uma conversa de voz avaliativa com IA. | Avalia o projeto final com voz, confirmando a identidade e gerando relatório. | Ocorre só no fim do projeto; não atua na IDE durante a construção para prevenir a falha cognitiva. | ≈ = = ≈ |
| **[Codswallop](https://marketplace.visualstudio.com/items?itemName=GideonBear.codswallop)** | Extensão de VS Code que dispara quiz (Claude) ao detectar colagem de código ou alta complexidade. | Atua na hora do atrito (Ctrl+V) direto na IDE. | O quiz é em texto, permitindo que o aluno fraude facilmente copiando a pergunta e jogando na IA. | = = = ≈ |
| **[comprehension-gate](https://github.com/hasura/comprehension-gate)** | GitHub Action que faz perguntas de texto sobre o diff do PR antes do merge. | Força a justificativa estrutural de um código antes de aceitá-lo. | O aluno escreve a resposta, o que não prova cognição real, pois a justificativa pode ser gerada. | ≈ = = ≠ |
| [Socratic IDE](https://github.com/Socratic-IDE) | Extensão que usa Ollama para fazer perguntas socráticas sobre o código. | Roda localmente sem custo de API de nuvem. | Age passivamente como tutor; não trava o fluxo exigindo prova estrutural antes do commit/salvamento. | = = ≈ ≈ |
| [Codefinds](https://marketplace.visualstudio.com/items?itemName=kabirmirza.codefinds) | Mede intervalos de digitação para classificar código como colado. | Mede perfeitamente o atrito mecânico localmente. | Foca na mecânica do teclado; o aluno pode burlar reescrevendo à mão sem entender a lógica. | = = ≈ ≈ |
| [DevForge Architect](https://marketplace.visualstudio.com/items?itemName=devforge.devforge-architect) | Extensão que dispara questionários ao detectar geração massiva de código. | Lê a arquitetura (AST) para barrar mudanças não justificadas. | Voltada para nuvem corporativa e devs, ignorando a dinâmica de avaliação de alunos; uso por texto. | ≈ ≈ ≈ ≈ |
| [VisualDebugger](https://github.com/Jason-Tan1/VisualDebugger) | Gera quizzes interativos e reproduz em voz as explicações sobre erros. | Estimula o canal auditivo no aprendizado. | Foca em resolver erros pontuais entregando a resposta mastigada, não em auditar código funcional. | = = ≈ ≈ |
| [CodeGrade AI](https://www.codegrade.com/solutions/ai-assistant) | Ambiente web educativo que responde dúvidas com base em regras do professor. | Centraliza logs contextuais para o educador. | É passivo, focado em dúvidas, e não exige ativamente a prova de autoria do aluno. | ≈ = ≠ ≠ |
| [Codequiry](https://codequiry.com/detect-ai-written-code) | Plataforma web anti-plágio baseada em estatística de tokens. | Precisão técnica em flagrar código de IA. | Abordagem policial e punitiva que ocorre pós-entrega, sem ensinar ou gerar evolução no aluno. | ≠ = ≠ ≠ |
| [Code Review AI](https://marketplace.visualstudio.com/items?itemName=NitishJT.code-review-ai) | Extensão de VS Code que revisa e dá dicas automáticas. | Acelera a correção de erros consultando o Git. | Dá a resposta pronta, aprofundando a alienação técnica e o problema do aluno não pensar. | ≈ ≠ ≠ ≈ |

## 3 · catálogo de artigos

| artigo (autores, ano, com link) | veículo | o que propõe | no que é bom | onde falha | C U P T |
|:--|:--|:--|:--|:--|:-:|
| **[Using GitHub Copilot to Solve Simple Programming Problems](https://dl.acm.org/doi/10.1145/3545945.3569830)** (Wermelinger, 2023) | SIGCSE · A1 | Avalia a capacidade de novatos resolverem problemas guiados pelo Copilot na IDE. | Mostra as implicações reais de ter código sugerido na tela do estudante. | Estudo empírico; não propõe uma ferramenta para remediar a confiança cega e alienação. | = = ≈ ≈ |
| **[“It's Weird That it Knows What I Want”](https://dl.acm.org/doi/10.1145/3617367)** (Prather et al., 2023) | TOCHI · A1 | Estudo observacional de novatos interagindo com IA generativa. | Documenta a alienação: o aluno aceita o código sem refletir sobre ele. | É um artigo de comportamento humano, não uma proposta de software avaliativo corretivo. | = = ≈ ≈ |
| **[Natural Language-Focused Software Engineering via Code-Documentation Equivalence](https://dl.acm.org/doi/10.1145/3660787)** (Eghbali et al., 2024) | FSE · A1 | Abordagem de LLMs para cruzar a intenção documentada com a estrutura do código. | Prova em veículo de excelência que LLMs podem validar lógicas de software complexo usando a AST. | Foco na validação de documentação corporativa e não em avaliações de estudantes por voz. | ≈ ≈ ≠ ≈ |
| [ChatGPT in Introductory Programming: Counterbalanced Evaluation](https://dl.acm.org/doi/10.1145/3769694.3771128) (Ouh et al., 2025) | SIGCSE · A1 | Avalia o aprendizado de turmas usando IA contra turmas sem IA. | Mede objetivamente o estrago da geração irrestrita na compreensão dos fundamentos. | Teste pedagógico passivo web; não propõe intervenção ativa dentro do editor (VS Code). | ≈ = = ≠ |
| [The Robots Are Here: Navigating the Generative AI Revolution in Computing Education](https://dl.acm.org/doi/10.1145/3564721.3569527) (Becker et al., 2023) | SIGCSE · A1 | Diretrizes e discussões sobre o impacto dos LLMs no ensino de computação. | Estabelece que ferramentas policiais vão falhar, exigindo novas formas ativas de avaliar. | É um artigo de posicionamento/discussão, e não uma ferramenta técnica ou infraestrutura de prova. | ≈ = = ≠ |
| [Exploring Motor-impaired Programmers' Use of Speech Recognition](https://dl.acm.org/doi/10.1145/3517428.3550392) (Sadia et al., 2022) | ASSETS · A1 | Análise de devs ditando código diretamente através da voz. | Prova o atrito e viabilidade técnica robusta do uso de voz (ASR) no ecossistema de programação. | Usa voz para ditar a sintaxe (acessibilidade), e não para exigir e processar prova lógica. | = ≠ ≠ ≈ |
| [Github Copilot in the Classroom](https://dl.acm.org/doi/10.1145/3575618.3575622) (Balse et al., 2023) | ICSE-SEET · A1 | Efeitos da adoção de assistentes em sala de aula de programação. | Mostra que o ambiente universitário carece de infraestrutura que acompanhe o uso da IA. | Foca em diretrizes de sala, sem propor validação por áudio/AST ou Edge AI local. | = = ≈ ≈ |
| [The StudyChat Dataset](https://dl.acm.org/doi/10.1145/3785022.3785029) (Sallam et al., 2024) | L@S · A1 | Analisa logs de alunos verbalizando dúvidas técnicas para o ChatGPT. | Mede a real dificuldade de novatos em explicar lógicas de código estruturadas para máquinas. | Usa texto em ambiente web, sendo puramente para tutoria, não para auditoria técnica. | ≈ = ≈ ≠ |
| [Programming education with ChatGPT](https://dl.acm.org/doi/10.1007/s10639-025-13542-4) (Yilmaz et al., 2026) | EAIT · A2 | Compara o desempenho educacional na adoção base de IA. | Mede em escala acadêmica as métricas de evasão cognitiva decorrentes do atalho gerado. | Estudo metodológico; não desenvolve solução de software baseada em Edge AI/Voz. | ≈ = = ≠ |
| [VocalIDE: An IDE for Programming via Speech Recognition](https://dl.acm.org/doi/10.1145/3132525.3134824) (Deselaers et al., 2017) | ASSETS · A1 | IDE desenvolvida estritamente para codar por fala. | Mostra que acoplar captura profunda de voz em arquiteturas de IDE é perfeitamente viável. | Abordagem legada focada em substituição do teclado, e não na auditoria avaliativa de LLMs. | = ≈ ≠ ≈ |

## 4 · os 3 + 3 mais próximos

- **Viva:** Faz a auditoria verbal sobre código entregue; escolhido porque prova que o exame oral orquestrado por IA é viável e já existe como produto.
- **Codswallop:** É o concorrente mais direto: atua no atrito (Ctrl+V) dentro da IDE para auditar se o aluno entende o que colou. Falha usando quizzes de texto.
- **comprehension-gate:** Intercepta diffs estruturais forçando justificativa do autor. Escolhido porque age como uma catraca (gatekeeper), alinhado ao objetivo da minha ideia, mas falha no uso de texto copiável.
- **Using GitHub Copilot (Wermelinger):** O estudo basal sobre as implicações de novatos resolvendo problemas dentro da própria IDE. Escolhido por enquadrar perfeitamente a dor principal da minha ficha de "Cenário".
- **“It's Weird That it Knows What I Want” (Prather):** Documenta a confiança cega do aluno (viés de automação) em sugestões generativas, o "Problema" central que a obrigatoriedade da voz visa interromper.
- **Natural Language-Focused SE (Eghbali):** Prova técnica em veículo de excelência (FSE) de que cruzar estruturas complexas de código (AST) com análise semântica em IA tem embasamento científico e funciona.

## 5 · a matriz

**✔** faz · **◐** faz em parte · **✘** não faz · **?** não achei evidência

| trabalho | avalia a autoria por entrevista oral (voz) | atua preventivamente na IDE durante a construção | mastiga a resposta e entrega código pronto | o aluno pode fraudar copiando texto para a IA | roda 100% local (sem custo de API) |
|:--|:-:|:-:|:-:|:-:|:-:|
| Viva | ✔ | ✘ | ✘ | ✘ | ✘ |
| Codswallop | ✘ | ✔ | ✘ | ✔ | ✘ |
| comprehension-gate | ✘ | ✘ | ✘ | ✔ | ✘ |
| Copilot (Wermelinger) | ✘ | ✔ | ✔ | ✘ | ✘ |
| Confiança Copilot (Prather) | ✘ | ✔ | ✔ | ✘ | ✘ |
| Code Doc (Eghbali) | ✘ | ✘ | ✔ | ✘ | ? |
| **a minha ideia** | ✔ | ✔ | ✘ | ✘ | ✔ |

**evidência** (1 linha por ✔ e ◐ dos 6):
- Viva: Entrevista oral (✔) confirmada no site oficial, porém ocorre após a entrega e depende de APIs na nuvem (Claude/Gemini) para operar (✘).
- Codswallop: Trava a ação dentro da IDE para avaliação (✔), porém usa texto gerado pela API do Claude, permitindo que a justificativa seja fraudada via IA (✔).
- comprehension-gate: Ocorre na plataforma de repositório, lendo o diff para forçar a justificativa em texto (✔), usando APIs externas para validar o comentário.
- Copilot (Wermelinger): Opera dentro da IDE durante a codificação (✔), entregando ao aluno blocos de código mastigados baseados em nuvem (✔).
- Confiança Copilot (Prather): Demonstra na IDE em tempo de edição (✔) as entregas prontas de lógicas complexas para os novatos aprovarem (✔).
- Code Doc (Eghbali): Lê o contexto para construir de forma mastigada (✔) a equivalência da documentação natural ao longo do processo.

## 6 · a contribuição

**a frase:** O Rastro Cognitivo intercepta mudanças na estrutura do código diretamente na IDE e cobra explicação por voz rodando integralmente de forma local; por isso atua exclusivamente na auditoria e metrificação impedindo que o estudante fraude a justificativa com texto de IA e dispensa dependência de nuvem paga, o que ferramentas existentes de auditoria de código não conseguem fazer simultaneamente.

**o trabalho mais próximo, e por que ele não chega lá:** O Codswallop atua como auditor exatamente na IDE durante ações críticas (Ctrl+V), mas não chega lá porque suas avaliações geram quizzes de múltipla escolha baseados na nuvem, permitindo que o aluno burle a verificação copiando as respostas de IAs externas.

## 7 · tentei derrubar

o que a conversa nova achou: Os apps Codswallop e Socratic IDE (que testam alunos localmente ou na IDE via texto), e plataformas como Viva e Oralify (que fazem exames de voz baseados em código, mas na nuvem e no fim da entrega).

o que eu mudei: As promessas não comprováveis ("garantindo aprendizado") caíram. Os achados (Codswallop, Viva) entraram no catálogo, substituindo opções mais fracas. A matriz foi reestruturada: incluí o eixo em que a minha ideia "perde" (não entrego a solução/código mastigado). A frase passou a focar na exata intersecção de uso estrutural na IDE + bloqueio de fraude por voz + ambiente local.

## 8 · resumo, sem IA

Soluções como Codswallop disparam questionários na IDE ao detectar muito código gerado, mas usam texto, facilitando a fraude do aluno. Ferramentas como o Viva aplicam exames orais anti-fraude, mas rodam via nuvem apenas no final da entrega (punitivas). O Rastro Cognitivo usa LLMs locais e a AST para juntar a obrigatoriedade da voz preventiva dentro do editor de código, auditando o raciocínio sem custos de nuvem ou quebra de privacidade em laboratórios ou casa.

## 9 · auditoria cega

**o veredito da conversa nova:**

| item | passa ou não passa | trecho que prova | o que encontrei |
|:--|:--|:--|:--|
| 1. ferramentas | não passa | O catálogo tem 10 linhas (§2) e os 3 estão em §4 (Oralify.ai, Viva, comprehension-gate). Mas a única evidência de link aberto é "abri os três" (§7), e a folha não traz nenhuma URL. | Viva: achei o Viva do NYU Stern: prova oral por voz com examinador de IA, notas dadas por um conselho de modelos de linguagem. O pipeline usa Claude, Gemini e GPT-5 na correção, então ele é nuvem. A folha marca "?" na coluna "local" mesmo havendo evidência. Não confirmei o "notebook.ipynb" que a folha cita. Oralify.ai: não achei a página; as buscas devolveram homônimos. comprehension-gate: existem pelo menos dois projetos com esse nome. Um faz 2–4 perguntas sobre o diff e o autor responde em comentário. O outro gera 3 perguntas de múltipla escolha via Claude. A folha não diz qual é. Os dois são texto e nuvem, então a crítica da folha bate. |
| 2. artigos | não passa | A tabela tem 10 artigos e §4 escolhe Wermelinger, Prather e Alahmadi. Os rótulos são "SIGCSE · A1", "TOCHI · A1" e "FSE · A1", sem fonte, e nenhum tem link. | Wermelinger: existe, é SIGCSE 2023, pp. 172–178, em trilha de papers, então é artigo completo. Mas a folha diz que ele "analisa a fricção do aluno" e "prova o estrago de colar código". O resumo descreve o autor avaliando as sugestões do Copilot, e o foco é capacidade e implicações para o ensino. Prather: existe, é TOCHI 31(1), artigo 4, 31 páginas, completo. Bate em linhas gerais. Alahmadi: não bate. O artigo com esse título quase idêntico é "Natural Language-Focused Software Engineering via Code-Documentation Equivalence", de Eghbali, Liu e Pradel. Foi publicado no ESEC/FSE em 2026 (arXiv de junho de 2026). Não achei Alahmadi, nem 2024, nem "Code Documentary" no título (Documentary é o nome da abordagem). O resumo não menciona AST. Autores, ano, título e conteúdo estão errados na folha. |
| 3. contribuição | não passa | A frase está em §6, a matriz em §5 e o veredito pendente é este. Mas §6 diz "ausência comprovada de execução 100% local" e §5 marca "?" para Oralify e Viva. O §8 diz que "nenhum deles" roda local. | Não achei app ou artigo que faça tudo da frase (AST → pergunta → resposta em voz → modelos locais → código de IA). Busquei combinações de IDE, voz, local, quiz e AST. Os mais próximos, nenhum no catálogo: Codswallop, extensão de VS Code que dispara quiz por colagem de mais de 10 linhas ou complexidade ciclomática alta, com 4 perguntas geradas pelo Claude e painel para o professor. Socratic IDE, local via Ollama, quiz sobre o próprio código, extração de funções, mas em texto. CodeTogether, VS Code, pede ao dev que explique mudanças do Git em palavras próprias, mas ainda é protótipo sem isso implementado. Local Copilot, VS Code com Ollama e qwen2.5-coder, que explica código em voz; a voz é só de saída e não audita nada. Pontos mais fracos da frase: (1) "alcançam plenamente" é uma ressalva que blinda a frase. (2) "garantindo a prova cognitiva" promete demais. (3) A contradição entre "?" e "comprovada". |

**a minha resposta, sem IA:**
1. Corrigi as ausências de links, adicionando URLs aos itens das tabelas 2 e 3, e substituí o Oralify.ai (que existe: https://www.oralify.ai/) pelo Codswallop, identificado pelo auditor como um concorrente real no contexto de IDE.
2. Incorporei as URLs e corrigi totalmente a citação do artigo do FSE, passando a utilizar o trabalho exato de Eghbali et al. indicado pelo auditor. Além disso, ajustei as “falhas” do passo 2 para que representem dores e limitações reais do processo, e não simplesmente a ausência de funcionalidades.
3. Refiz totalmente a matriz com base nos achados do auditor: removi os eixos enviesados que favoreciam a solução e incluí critérios mais equilibrados, nos quais a solução também pode apresentar limitações. Também removi as promessas não comprováveis da frase no Passo 6, deixando claro que a ferramenta atua na auditoria e metrificação do código, sem prometer a entrega de código pronto.