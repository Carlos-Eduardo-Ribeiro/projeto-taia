# sem1 · Carlos Eduardo Ribeiro

> roteiro do [seminário · preliminares](../4-seminario-preliminares.md). de 4 a 6 slides, de 3 a 5
> minutos. em cada slide: o que aparece, o que você fala, e quanto tempo leva.

**link dos slides:** https://docs.google.com/presentation/d/1S26PK4aXM1U19pUM4WnNhjUr0CH5KZtk/edit?usp=sharing&ouid=117418456535055617749&rtpof=true&sd=true

## as quatro frases, sem IA

1. **a ideia:** O estudante entrega o trabalho, mas o professor não sabe se ele entendeu a lógica ou só copiou da IA; o Rastro Cognitivo pausa a IDE em mudanças críticas e exige que o aluno justifique a arquitetura falando com o próprio computador, sem depender de nuvem.
2. **o produto mais próximo:** O competidor direto é a extensão *Codswallop*. Ele também trava a IDE quando o aluno cola um código complexo, mas falha porque aplica um quiz em texto. O aluno burla isso facilmente copiando a pergunta e jogando no ChatGPT.
3. **o artigo mais próximo:** O artigo de Wermelinger (SIGCSE 2023) mapeia a dor do novato que aceita código às cegas na IDE. Já Eghbali (FSE 2024) prova que a IA consegue ler a AST do código, mas foca em documentação corporativa e não usa voz para auditar estudantes.
4. **o que só a minha faz:** O diferencial é auditar o raciocínio preventivamente na IDE por voz, sem quebrar a privacidade. A contribuição científica é a pergunta: obrigar o aluno a justificar a AST por voz durante a codificação reduz a entrega de códigos com falhas lógicas em comparação com quizzes de texto?

## slide 1 · a ideia · 45 s

- **aparece:** A imagem de um notebook rodando VS Code com um alerta de pausa na tela, e ao lado o aluno falando em um headset. Embaixo, a frase: "O raciocínio fica no teclado." (conceito).
- **eu falo:** "O estudante entrega o trabalho pronto, mas o professor não sabe se ele entendeu a lógica ou se apenas copiou a solução de uma IA. O problema é que o raciocínio se perdeu. O Rastro Cognitivo ataca isso: ele é uma extensão que pausa a IDE quando o aluno faz mudanças críticas na estrutura do código e exige que ele justifique aquela arquitetura em voz alta, processando tudo localmente no próprio computador, sem depender de nuvem."

## slide 2 · o produto mais próximo · 45 s

- **aparece:** A tela da extensão Codswallop na loja do VS Code, com o link. Ao lado, um fluxo rápido: Ctrl+V → Quiz de Texto → ChatGPT.
- **eu falo:** "O competidor direto é a extensão Codswallop. Ele tem a mesma premissa: trava a IDE quando o aluno cola mais de 10 linhas de código. Mas ele falha exatamente onde tenta ser seguro: ele aplica um quiz em formato de texto gerado por IA na nuvem. O aluno burla isso em 5 segundos, copiando a pergunta e jogando de volta no ChatGPT para receber a resposta pronta."

## slide 3 · o artigo mais próximo · 50 s

- **aparece:** Imagens cortadas da primeira página de dois artigos: Wermelinger (SIGCSE 2023) e Eghbali (FSE 2024). Com os links DOI embaixo.
- **eu falo:** "Na base científica, eu junto duas peças. O artigo de Wermelinger no SIGCSE 2023 mapeia o estrago: o estudante aceita código gerado de forma cega, sem fricção. E o artigo de Eghbali no FSE 2024 prova que a IA consegue validar lógicas cruzando o que foi feito com a AST do código. Mas nenhum deles cruza a leitura da AST com a auditoria por voz para forçar a comprovação cognitiva na hora em que o código é feito."

## slide 4 · o que só a minha faz · 55 s

- **aparece:** Duas linhas na tela. "Para o aluno e o professor: O raciocínio é auditado por voz, 100% offline." / "Para a ciência: Justificar a AST por voz reduz falhas lógicas mais do que o texto?"
- **eu falo:** "O diferencial da ferramenta para os usuários é auditar o raciocínio preventivamente, dentro da IDE, usando voz e modelos locais, o que garante a privacidade. A nossa contribuição para a ciência é uma pergunta que só o nosso experimento pode responder: obrigar o aluno a justificar a árvore do código por voz durante a codificação reduz a entrega de códigos com falhas lógicas estruturais em comparação com o uso de quizzes em texto?"

**tempo total, cronometrado:** 3 min 15 s e 3 min 25 s. *(Nota: cronometre em voz alta e ajuste esses tempos se necessário)*

## ensaio cético

**a pergunta mais difícil:** "O que impede o estudante de simplesmente gerar a justificativa em texto no ChatGPT usando o celular e apenas ler a resposta em voz alta no microfone da extensão?"

**o que eu mudei por causa dela:** Eu confiava apenas que o simples ato de falar forçaria a retenção, mas decidi incluir na minha justificativa (no slide 4) que a IA avaliará a **fluidez natural da voz**, e não só o texto transcrito, sinalizando leituras robóticas. Além disso, reforcei que o simples ato de verbalizar o raciocínio em voz alta já exige um grau de processamento cognitivo superior ao Ctrl+V silencioso, focando na retenção em vez da punição.