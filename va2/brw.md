# brw · Carlos Eduardo Ribeiro

> folha do artefato [brainwriting híbrido](../3-brainwriting-hibrido.md). siga o guia passo a passo
> e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 1 · onde atacar

**crise** (marque 1 com `x`):

| | crise |
|:-:|:--|
| [x] | perda do raciocínio crítico e alienação (*slop*) |

por que esta crise: Porque as pessoas estão delegando o processo inteiro à IA focando apenas no resultado final. Quero criar algo que alie a agilidade da IA à construção ativa de aprendizado, garantindo que o usuário entenda, valide e construa de forma segura.

**tecnologias de IA** (marque 3 e chame de A, B, C):

| | tecnologia de IA |
|:-:|:--|
| [x] A | modelos locais / no aparelho (*SLMs*, 1B–7B) (Qwen2.5-Coder via llama.cpp) |
| [x] B | voz (fala ↔ texto) e interfaces sem tela (Whisper Local) |
| [x] C | sistemas multiagente e agência (Orquestração de Git/AST) |

**infraestruturas tradicionais** (marque 3 e chame de 1, 2, 3):

| | infraestrutura |
|:-:|:--|
| [x] 1 | outra: Infraestrutura de Testes e Compilação (IDE/VS Code) |
| [x] 2 | outra: Controle de Versão (Git / Histórico de Diffs) |
| [x] 3 | outra: Code/Peer Review (Avaliação Semântica) |

## 2 · clichês

| clichê | o que acerta | onde fica raso |
|:--|:--|:--|
| **1. Tutor chatbot que "não dá a resposta"** | Tenta forçar o usuário a pensar guiando-o com o método socrático. | É facilmente "vencido" pelo usuário com prompts como "ignore as regras", falhando na restrição. |
| **2. Plugin bloqueador de copiar e colar** | Impede que o usuário jogue a resposta direto no projeto. | Foca na ação motora (digitar) e não no raciocínio; o usuário apenas transcreve sem entender. |
| **3. Detector de IA (Anti-Cheat / Turnitin)** | Inibe entregas 100% geradas por IA pelo medo da punição. | Transforma a educação em jogo de polícia e ladrão; o foco vira "mascarar o texto" em vez de provar autoria cognitiva. |
| **4. Quiz de múltipla escolha no final da tarefa** | Estabelece um ponto de checagem do conteúdo gerado. | São genéricos. Não avaliam se o usuário sabe consertar ou adaptar a lógica na arquitetura real. |
| **5. Dashboard de limite de IA diário** | Restringe a quantidade de chamadas, obrigando a racionar. | Quantidade não é qualidade. O aluno pode gastar a cota pedindo a solução inteira de uma vez. |

## 3 · matriz 3 × 3 e a minha ideia

cada célula: **nome** · frase de até 20 palavras (quem usa, o que faz).

| | 1 · IDE / VS Code | 2 · Histórico Git (Diffs) | 3 · Avaliação (Review) |
|:--|:--|:--|:--|
| **A · Modelos Locais (SLM)** | **IDE Investigativa** · modelo local avalia AST do código e questiona decisões complexas. | **Commit Explicado** · modelo avalia o diff do commit local e exige justificativa em texto. | **Rubrica Automática** · SLM avalia qualidade do código baseado nos padrões do laboratório. |
| **B · Voz (Whisper)** | **Ctrl+V Falado** · ao colar código genérico, IDE obriga aluno a explicar a lógica por voz. | **Push por Voz** · para autorizar envio ao Git, aluno explica alteração em áudio transcrito. | **Review em Áudio** · professor escuta resumo transcrito das decisões arquiteturais do aluno. |
| **C · Orquestração** | **Agente AST** · lê a árvore estrutural do código para isolar apenas o que mudou. | **Filtro de Diffs** · cruza histórico Git com AST para não questionar arquivos de configuração. | **Relatório Consolidado** · gera métricas de evolução e dependência de IA com base nas respostas. |

**as 9 no mapa impacto × viabilidade:**

| | viabilidade alta | viabilidade baixa |
|:--|:--|:--|
| **impacto alto** | **Ctrl+V Falado**<br>**Agente AST** | **Push por Voz**<br>**Relatório Consolidado** |
| **impacto baixo** | **IDE Investigativa**<br>**Filtro de Diffs** | **Commit Explicado**<br>**Rubrica Automática**<br>**Review em Áudio** |

onde discordei da IA, e por quê: Concordei com o mapeamento, mas notei que a viabilidade de ferramentas puramente de voz ou puramente locais só se torna alta se a arquitetura for adaptável ao PC do usuário.

**minha ideia escolhida:** **Ctrl+V Falado (Extensão VS Code)** · Extensão lê diffs e AST, pausando para o aluno explicar decisões arquiteturais complexas por áudio.

**por que ela, sem IA, em até 3 linhas:** 
Escolhi pois abandona o foco policial de "caçar IA" e foca na comprovação cognitiva. Ao integrar isso direto no VS Code, o aluno consolida os fundamentos da programação de forma dinâmica, em casa ou na faculdade, reduzindo a dependência e melhorando a qualidade do código.

## 4 · motores

| motor | nome | frase | o que mudou em relação à ideia |
|:--|:--|:--|:--|
| inverter | **Agente Sabotador** | a extensão injeta erro no código; o aluno usa a AST para achar e explicar o problema. | aluno acha erro gerado pela IA em vez de explicar o próprio código. |
| canalizar | **Documentação Involuntária** | a explicação por voz vira documentação rica no Git e material de estudo. | obrigação de falar canalizada para gerar bem coletivo (docs). |
| transplantar | **Captcha Cognitivo** | como um Captcha, apaga lógicas vitais que o aluno deve reescrever e explicar. | transplanta segurança anti-bot para prova de aprendizado. |
| reescalar | **Rastro Microscópico** | pausa e avalia linha a linha digitada, em vez de avaliar o bloco todo. | auditoria excessivamente granular e intrusiva. |
| trocar a persona | **Extensão de RH** | recrutadores usam o plugin para avaliar candidatos em testes práticos. | foco sai do aluno/professor para o mercado de contratação. |
| trocar o contexto | **Redação Cognitiva** | avalia TCCs em editores de texto usando a mesma lógica estrutural. | contexto sai da programação e vai para a escrita acadêmica. |
| trocar a tecnologia | **Verificação em Nuvem** | força todo o processamento para APIs externas em vez de usar SLM local. | troca a infraestrutura local (privada) por nuvem (custosa). |
| juntar | **AST Falada** | cruza a leitura da árvore estrutural (AST) com o Whisper para questionamento cirúrgico. | mistura detecção inteligente com input humanizado por voz. |
| restringir | **Avaliação Sem Tela** | VS Code trava a tela visual; aluno deve justificar lógica guiado apenas por áudio. | restringe uso visual, forçando lembrança total da arquitetura. |

## 5 · o que fica e o que sai

**o que eu gostei:** Gostei da junção de ler a AST (para isolar alterações vitais) e usar a explicação por voz. É brilhante a ideia de canalizar essa validação para a geração de relatórios e documentação do aluno.

**o que achei interessante:** A noção de que a ferramenta deve avaliar não se a IA fez o código, mas se o aluno compreende o que está ali, usando uma rubrica avaliativa padronizada. 

**o que eu descarto, e por quê:** Descarto restrições punitivas (batalhas contra o relógio ou travar a tela). O foco precisa ser educacional e adaptável, rodando de forma soberana (localmente) e funcionando bem tanto nos laboratórios da faculdade quanto nos estudos da madrugada em casa.

**minha ideia completa:** **Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor; se não der, libera uso de API Key na nuvem. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e exigindo que o aluno justifique a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas da turma.

## 6 · refinamento

**a · e se todo mundo usasse?** Em 5 anos, formaríamos programadores com base sólida, capazes de ler, auditar e orquestrar código gerado por IA com maestria, porque foram forçados a interpretar a lógica ao longo de todo o curso. Estudantes (na faculdade e em casa) usariam a extensão ativamente pelo desejo egoísta de descobrir exatamente onde estão falhando nos fundamentos, mapear sua evolução técnica em métricas claras e conseguir trilhas de estudo personalizadas baseadas em seus relatórios.

**b · a IA que não pode faltar.** técnica: Modelos Locais (*SLMs* quantizados, ex: Qwen2.5-Coder) e Transformers de Voz (*Whisper*). · aula da disciplina: 07 - modelos locais / SLMs e 11 - transformers.

por que sem ela não roda: Sem SLMs locais executando llama.cpp, a extensão dependeria de servidores caros, ferindo a privacidade do aluno e inviabilizando uso sem internet ou em universidades sem verba. O Qwen-Coder é vital para ler o contexto do Git/AST e aplicar a rubrica inteligentemente. O Whisper garante o fluxo por fala; sem ele, a exigência de digitar justificativas longas transformaria a extensão numa burocracia insustentável.

**c · o cético e as saídas**

| crítica | saída 1 | saída 2 | minha decisão |
|:--|:--|:--|:--|
| PCs de alunos (em casa/laboratório) não aguentam rodar Docker, IDE, Qwen e Whisper simultaneamente sem travar. | Forçar todo o processamento para a nuvem da universidade via API. | Fazer profiling adaptativo: manter local com modelo menor se o PC for fraco, ou liberar API Key do usuário em último caso. | Escolho a saída 2. A degradação suave garante que a prioridade seja sempre o processamento local (Edge AI), sacrificando desempenho sutil do LLM em PCs fracos antes de apelar para a nuvem. |
| O Whisper pode transcrever jargões técnicos errado ("array" como "rei"), frustrando a rubrica de avaliação. | Injetar o dicionário de variáveis da AST no prompt do Whisper. | Instruir o Qwen via prompt a focar na intenção lógica da resposta, perdoando erros fonéticos óbvios. | Escolho a saída 2 apoiada pela saída 1. Ao injetar a AST no Whisper e instruir a tolerância na rubrica do Qwen, anulamos a frustração por falso-negativo semântico. |
| O aluno pode gerar a explicação num celular com ChatGPT e ler feito um robô. | Adicionar cronômetro punitivo (10s) para responder. | O LLM analisa a fluidez, sinalizando falas robóticas e sem hesitações naturais. | Escolho a saída 2. Avaliar fluidez foca a análise em cognição real e evita punições de tempo que prejudicariam alunos mais reflexivos. |

## 7 · resumo, sem IA

Ataco a crise da robotização do pensamento, onde o estudante delega o raciocínio e enfraquece seus fundamentos técnicos. A solução é a extensão "Rastro Cognitivo" (VS Code), que usa leitura de AST e Git para acionar perguntas estruturais sobre o código em áudio. Rodando via Edge AI (Qwen-Coder e Whisper locais com adaptação inteligente de hardware), avalia a autoria cognitiva e a compreensão. O incentivo egoísta de uso, em casa ou no lab, seria o mapeamento detalhado da própria evolução e a identificação de lacunas, formando devs conscientes e competitivos para o futuro.