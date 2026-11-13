# Termo de Consentimento Livre e Esclarecido (TCLE)

Você está sendo convidado(a) a participar da avaliação da extensão **Rastro Cognitivo**, um projeto da disciplina de IA for Good da Universidade Federal Rural de Pernambuco (UFRPE).

## O que é o projeto?
O Rastro Cognitivo é uma extensão para o VS Code que busca ajudar estudantes de programação a reterem o conhecimento de arquitetura de software. Quando você fizer uma mudança estrutural importante no código, a extensão pedirá que você explique rapidamente, por voz, o motivo técnico dessa decisão.

## O que será coletado?
Durante a sua participação, a extensão irá coletar:
1. **O áudio da sua justificativa** (sua voz).
2. **O trecho da Árvore de Sintaxe Abstrata (AST)** do código que você alterou.

## Como protegemos sua privacidade (LGPD)?
Este projeto foi desenhado com foco em **Edge AI** (Processamento Local), garantindo a sua privacidade:
* **Seu áudio não vai para a nuvem.** A transcrição e a avaliação são feitas por inteligência artificial (Whisper e Qwen) rodando **diretamente no seu próprio computador**.
* A gravação da sua voz fica apenas na memória RAM e é **apagada imediatamente** após a transcrição para texto. 
* O seu código-fonte não é enviado para servidores de empresas externas (como OpenAI ou Google).
* Apenas as **métricas do seu desempenho** (se a IA considerou que você compreendeu ou não a arquitetura, e o tempo de resposta) serão consolidadas em um painel para o professor. 

## Riscos e Benefícios
* **Riscos:** O principal risco é o de frustração temporária caso a IA não compreenda corretamente o seu áudio devido a sotaques, ruídos ou limitações técnicas (falsos negativos), exigindo que você repita a explicação.
* **Benefícios:** Você receberá um relatório individual detalhando a evolução da sua base técnica e mapeando suas lacunas de conhecimento.

## Participação Voluntária
A sua participação neste teste é **totalmente voluntária**. Você pode se recusar a participar ou desistir a qualquer momento, desinstalando a extensão, sem qualquer penalidade ou prejuízo nas suas notas da disciplina.

---

**Declaração de Consentimento:**
Ao prosseguir com a gravação do áudio na IDE após ler este aviso, você declara que compreende os termos acima e concorda voluntariamente em participar deste experimento.