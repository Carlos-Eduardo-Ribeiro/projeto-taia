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
| [x] A | outra: Sistemas Multiagente com Papéis (Auditor/Cético) |
| [x] B | outra: Redes Neurais / Modelos Autoencoders |
| [x] C | outra: Análise de Trajetória / Aprendizado por Reforço |

**infraestruturas tradicionais** (marque 3 e chame de 1, 2, 3):

| | infraestrutura |
|:-:|:--|
| [x] 1 | outra: Infraestrutura de Testes Automatizados (CI/CD) |
| [x] 2 | outra: Controle de Versão (Git / Histórico de Commits) |
| [x] 3 | outra: Plataformas de Code Review/Peer Review Assíncrono |

## 2 · clichês

| clichê | o que acerta | onde fica raso |
|:--|:--|:--|
| **1. Tutor chatbot que "não dá a resposta"** | Tenta forçar o usuário a pensar guiando-o com o método socrático. | É facilmente "vencido" pelo usuário com prompts como "ignore as regras", falhando na restrição. |
| **2. Plugin bloqueador de copiar e colar** | Impede que o usuário jogue a resposta direto no projeto. | Foca na ação motora (digitar) e não no raciocínio; o usuário apenas transcreve sem entender. |
| **3. Detector de IA (Anti-Cheat / Turnitin)** | Inibe entregas 100% geradas por IA pelo medo da punição. | Transforma a educação em jogo de polícia e ladrão; o foco vira "mascarar o texto" em vez de aprender. |
| **4. Quiz de múltipla escolha no final da tarefa** | Estabelece um ponto de checagem do conteúdo gerado. | São genéricos. Não avaliam se o usuário sabe consertar ou adaptar a lógica na arquitetura real. |
| **5. Dashboard de limite de IA diário** | Restringe a quantidade de chamadas, obrigando a racionar. | Quantidade não é qualidade. O usuário pode gastar a cota pedindo a solução inteira de uma vez. |

## 3 · matriz 3 × 3 e a minha ideia

cada célula: **nome** · frase de até 20 palavras (quem usa, o que faz).

| | 1 · Infra de CI/CD | 2 · Controle de Versão (Git) | 3 · Code/Peer Review |
|:--|:--|:--|:--|
| **A · Multiagente** | **CI Cético** · a esteira CI usa agente para injetar falha; o dev explica a quebra. | **Commit Entrevistado** · agente audita grande mudança e exige justificativa de linha específica. | **Reviewer Infiltrado** · agente esconde erro sutil no review para testar aprovação automática. |
| **B · Autoencoders** | **Filtro de Anomalia** · build falha se a estrutura de código for idêntica à média global (slop puro). | **Assinatura de Código** · Git treina modelo de estilo; commits destonantes exigem explicação. | **Mapa de Originalidade** · review exibe mapa de calor destacando blocos gerados por IA para discussão. |
| **C · RL / Trajetória** | **Esteira Progressiva** · CI mede intervenção humana e ajusta complexidade de testes futuros. | **Jornada Recompensada** · Git acompanha histórico premiando refatorações iterativas sobre copiar/colar. | **Match de Complexidade** · pareia aluno obrigatoriamente para revisar lógicas que exigem profundidade. |

**as 9 no mapa impacto × viabilidade:**

| | viabilidade alta | viabilidade baixa |
|:--|:--|:--|
| **impacto alto** | **Commit Entrevistado**<br>**Filtro de Anomalia** | **Assinatura de Código**<br>**Jornada Recompensada** |
| **impacto baixo** | **Mapa de Originalidade**<br>**Reviewer Infiltrado** | **CI Cético**<br>**Esteira Progressiva**<br>**Match de Complexidade** |

onde discordei da IA, e por quê: Concordei com a IA, pois o mapeamento de impacto e viabilidade se alinhou à minha visão de focar no entendimento do código sem complexidade desnecessária.

**minha ideia escolhida:** **Commit Entrevistado** · Antes de aceitar um push gigante, um agente audita a mudança e exige que o aluno justifique uma linha específica.

**por que ela, sem IA, em até 3 linhas:** 
Escolhi pois é compreensível e obriga o profissional/estudante a ter noção do código sem apenas colar às cegas. Isso liga a parte consciente do cérebro, forçando-o a pensar, o que reduz erros e melhora absurdamente a produção no mundo corporativo.

## 4 · motores

| motor | nome | frase | o que mudou em relação à ideia |
|:--|:--|:--|:--|
| inverter | **Agente Sabotador** | o agente faz o commit; o aluno atua como auditor e precisa encontrar a falha proposital antes de aprovar. | inverte o papel: o aluno investiga e acha o erro no código da IA, em vez de explicar o próprio. |
| canalizar | **Documentação Involuntária** | a explicação que o dev dá para passar o commit vira a documentação oficial daquele código. | a obrigação chata de passar no teste é canalizada para gerar documentação útil para toda a equipe. |
| transplantar | **Captcha Cognitivo** | como um Captcha, antes do push a IDE apaga partes vitais da lógica e o aluno as preenche de memória. | transplanta a mecânica de segurança contra bots para provar que o humano entende a lógica. |
| reescalar | **Ctrl+V Entrevistado** | em vez do grande push final, o agente pausa e entrevista o aluno a cada bloco colado na IDE. | auditoria reescalada 100x para baixo: sai do Git e vai para a edição (colar texto). |
| trocar a persona | **Commit Entrevistado no RH** | recrutadores usam a ferramenta para que candidatos justifiquem linhas do desafio antes da contratação. | usuário deixa de ser estudante e passa a ser candidato a vaga de TI. |
| trocar o contexto | **Parágrafo Entrevistado** | a ferramenta audita TCCs no Google Docs, questionando parágrafos gerados por IA. | contexto sai do código para o mundo da redação acadêmica. |
| trocar a tecnologia | **Push por Voz** | Git bloqueia teclado; o aluno aprova o commit se gravar um áudio de 15s explicando a lógica. | troca texto por voz, obrigando a verbalizar a cognição sem copiar a explicação. |
| juntar | **Commit Anômalo Entrevistado** | o agente só exige justificativa das linhas exatas que o Autoencoder flagrou como slop genérico. | junta agente e filtro de anomalia, auditando só o que tem "cheiro" de alienação. |
| restringir | **Batalha contra o Relógio** | o aluno tem apenas 20 segundos para justificar a linha, senão o commit é rejeitado. | restrição de tempo severa: impede que o aluno vá pesquisar a resposta na hora. |

## 5 · o que fica e o que sai

**o que eu gostei:** Gostei de "Documentação Involuntária", "Ctrl+V Entrevistado", "Commit Entrevistado no RH" e "Commit Anômalo Entrevistado".

**o que achei interessante:** Achei "Push por Voz" fantástica, pois junta a fala com a cognição e aumenta a retenção do aprendizado. Obriga a verbalizar a lógica sem "copiar e colar" a explicação.

**o que eu descarto, e por quê:** Descarto o restante, pois seguem uma vertente de mais atrapalhar do que ajudar. A ferramenta no ambiente corporativo precisa combinar trabalho e aprendizagem, sendo rápida e dinâmica.

**minha ideia completa:** **Rastro Cognitivo (Ctrl+V Falado)**
Desenvolvedores e estudantes usam a ferramenta direto na IDE. Quando colam códigos sinalizados por Autoencoder como "100% IA genérica", a IDE exige que o dev grave um áudio explicando a arquitetura e segurança daquele bloco na hora (ou faz um apanhado para antes do commit/PR). Esse áudio é transcrito via Transformers (Voz ↔ Texto) e acoplado automaticamente ao código como documentação. A pessoa ganha velocidade para produzir e documentar, enquanto verbalizar consolida o raciocínio, reduzindo a alienação.

## 6 · refinamento

**a · e se todo mundo usasse?** Em 5 anos, haveria uma redução drástica na geração de "código lixo", garantindo entregas mais seguras e aderentes à arquitetura corporativa. A adoção ocorreria porque o dev usaria a IA para trabalhar rápido, mas teria interesse egoísta em verbalizar a documentação: demonstrar domínio, conseguir aumentos salariais e promoções, evitando virar um "apertador de botão" facilmente substituível.

**b · a IA que não pode faltar.** técnica: Autocodificadores (detecção de anomalia) e Transformers (Voz ↔ Texto) · aula da disciplina: 07 - arquiteturas de deep learning (autocodificadores) e 11 - arquiteturas de deep learning (transformers).

por que sem ela não roda: Sem autocodificadores, o sistema não isolaria o "slop", pausando todo trecho e irritando o dev. Sem transformers de voz, a exigência de digitar justificativas de arquitetura à mão destruiria a agilidade corporativa que a IA deveria trazer. A IA avançada viabiliza a auditoria ágil.

**c · o cético e as saídas**

| crítica | saída 1 | saída 2 | minha decisão |
|:--|:--|:--|:--|
| Devs sêniores podem achar o áudio um "microgerenciamento" irritante. | Focar a ferramenta no onboarding, estagiários e desenvolvedores juniores. | Exigir áudio apenas em PRs que alterem o core da arquitetura de segurança. | Escolho a saída 1. Focar a ferramenta no onboarding e juniores transforma-a em motor de evolução e comprovação sem atritar com sêniores. |
| O Autocodificador pode sinalizar configurações simples ou boilerplates. | Treinar o modelo para ignorar arquivos de configuração (JSON, YAML). | Apoiar-se no Tech Lead para aprovar padrões prévios da empresa. | Escolho a saída 1. Ignorar arquivos de configuração poupa tempo e foca a auditoria exclusivamente nas regras de negócio e lógica complexa. |
| Gravar áudio em escritório open-space pode captar segredos e gerar péssima transcrição. | Testar inicialmente apenas para times em regime de trabalho remoto. | Oferecer "modo silencioso" com bullet points estritos de arquitetura caso haja muito barulho. | Escolho a saída 2. O modo silencioso focado restringe danos e impede que limitações físicas da infraestrutura quebrem o fluxo. |

## 7 · resumo, sem IA

Ataco a crise da robotização do pensamento, onde indivíduos delegam suas decisões à IA e param de pensar por si. A ideia é um avaliador que questiona o desenvolvedor (desde funções básicas até arquitetura e segurança) para garantir que ele compreenda e justifique suas decisões. A IA avalia o código gerado, entrevista o usuário sobre as regras de negócio e transcreve a defesa falada para documentar a validação. Em escala, o mundo ganharia profissionais conscientes do impacto de suas produções. O uso ocorreria por interesse egoísta: blindar a carreira, desenvolvendo-se intelectualmente para não ser um copiador facilmente substituível.