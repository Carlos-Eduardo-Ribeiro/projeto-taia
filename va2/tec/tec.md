# tec · Carlos Eduardo Ribeiro

> folha do artefato [tecnologia base demonstrável](../3-tecnologia-base.md). siga o guia passo a
> passo e preencha cada seção aqui. as decisões são suas, e decidir é saber explicar.

## 0 · a minha ideia completa

**Rastro Cognitivo (Edge AI Edition)**
Uma extensão do VS Code 100% local. Ela instala, faz profiling de hardware (CPU/RAM/GPU) e baixa o Qwen2.5-Coder (GGUF/llama.cpp) e o Whisper. Se o PC for fraco, prioriza o local com um modelo menor. A extensão lê diffs do Git e a AST, detectando mudanças estruturais e emitindo um alerta não-intrusivo para o aluno justificar a arquitetura em áudio. O Qwen usa uma rubrica semântica para avaliar a compreensão (sem "caçar" IA). O aluno ganha um relatório de evolução de sua base técnica, e o professor recebe um dashboard consolidado das lacunas e dos alertas ignorados da turma.

técnica do § 6b do brw: Modelos Locais (SLMs quantizados, ex: Qwen2.5-Coder via llama.cpp) e Transformers de Voz (Whisper local)

## 1 · as peças

| peça | central ou apoio | o que faz na ideia | link oficial | licença | por que esta, e não as alternativas |
|:--|:--|:--|:--|:--|:--|
| faster-whisper | central | transforma o áudio da justificativa do aluno em texto localmente na CPU | [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) | MIT | Roda rápido em CPU via Python, ideal para validar a transcrição da prova de conceito neste artefato. O [whisper.cpp](https://github.com/ggerganov/whisper.cpp) (MIT) será o alvo na versão de produção da extensão por rodar binários nativos que dispensam Python na máquina do aluno, mas exige compilação C++ local que atrasaria a entrega de hoje. O [openai/whisper](https://github.com/openai/whisper) (MIT) é mais lento em CPU e consome mais recursos. |
| Ollama (rodando Qwen2.5-Coder) | apoio | avalia a semântica da transcrição do aluno cruzando com a AST/Diff | [ollama/ollama](https://github.com/ollama/ollama) e [Qwen2.5-Coder](https://huggingface.co/Qwen/Qwen2.5-Coder-1.5B) | MIT (Ollama) e Apache 2.0 (Qwen) | O Ollama entrega o modelo empacotado num executável via API local pronta para uso. O [llama.cpp](https://github.com/ggerganov/llama.cpp) puro (MIT) é a meta para o produto final por ser leve e facilmente embutível na IDE do VS Code, mas requer lidar com binários/build manual no Windows agora. O pacote [transformers](https://github.com/huggingface/transformers) (Apache 2.0) exige bibliotecas Python pesadas e mais RAM. |

## 2 · o exemplo oficial, rodando

**de onde veio o código:** Trecho "Usage" do [README do faster-whisper](https://github.com/SYSTRAN/faster-whisper#faster-whisper), usando o áudio de teste `jfk.flac`.

**o que eu mudei nele:** Forcei as opções `device="cpu"` e `compute_type="int8"` oferecidas pelo projeto para rodar no notebook. Adicionei um *monkey patch* (remendo) no próprio código para contornar um erro de compatibilidade da biblioteca `av` com versões novas do Python, suprimindo o parâmetro `metadata_errors`.

**o commit:** [ac9cbe2 · exemplo oficial do faster-whisper](https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/ac9cbe22a93249e28be580234272fc478e0a28be)

**o comando e a saída, colados como vieram:**

```text
(venv) PS C:\codigos\tec> python transcrever.py
Detected language 'en' with probability 0.945187
[0.00s -> 8.00s]  And so, my fellow Americans, ask not what your country can do for you.
[8.00s -> 11.00s]  Ask what you can do for your country.
```

## 3 · a alteração mínima

**o commit:** [ac9cbe2 · exemplo oficial do faster-whisper](https://github.com/Carlos-Eduardo-Ribeiro/projeto-taia/commit/1464fbc7369220139157749eb5499370bb6f129c)

**a entrada:** antes, o áudio de exemplo do projeto (discurso do JFK em inglês); agora, um áudio do meu problema (`explicacao.mp3` gravado por mim) simulando um aluno justificando o uso do padrão Singleton no banco de dados.

**a saída:** antes, apenas a transcrição do áudio com marcações de tempo; agora, mostra a transcrição seguida de uma avaliação semântica gerada por um SLM local (Qwen2.5-Coder de 1.5B rodando via Ollama), que julga se a arquitetura explicada faz sentido.

**o comando e a saída, colados como vieram:**

```text
(.venv) PS C:\codigos\projeto_taia\va2\tec> python transcrever_02.py
Ouvindo a justificativa do aluno...
Transcrição: Eu isolei essa função de conexão com o banco de dados usando o padrão Singleton para evitar que a aplicação abra múltiplas conexões e estore a memória do servidor.

Avaliando a compreensão da arquitetura...
Veredito do Rastro Cognitivo: O aluno parece entender a ideia de utilizar o padrão Singleton para garantir que a aplicação abra apenas uma única conexão com o banco de dados, evitando abrições excessivas e consumo excessivo de memória do servidor.

Tempo de execução: 13.92s (Whisper: 7.08s | Qwen: 6.84s)
```

**onde a saída erra:** Na transcrição, o Whisper (tamanho small) errou a fonética e escreveu "estore" em vez de "estoure". Na avaliação, o Qwen de 1.5B acertou o mérito técnico da resposta, mas inventou a palavra "abrições" em vez de "aberturas", mostrando a limitação de um modelo tão pequeno ao gerar texto natural em português.

## 4 · o vídeo

**link:** https://youtu.be/NsGLbL-tTrk · **duração:** 2:47 · **o que aparece:** os dois commits, o comando e a saída.

## 5 · o que deu certo e o que errou, sem IA

Gostei de rodar o modelo local. Ele é bem limitado, acredito que possa ser usado caso tenha o contexto correto e detalhado. Ele errou no português quebrado com a palavra "abrições", e o Whisper trocou "estoure" por "estore", o que denota limitações, mas entendeu o contexto geral. Exigiu um esforço razoável para uma máquina de 8GB de RAM, levando cerca de 5 a 20 segundos por uma resposta (o tempo pode escalar dado o contexto real de aplicação). Seria interessante mudar e fazer testes com um modelo maior, de pelo menos 7B, para tentar eliminar questões como erros gramaticais.

## 6 · auditoria cega

### o veredito da conversa nova

| item | passa ou não passa | trecho que prova o que encontrei (links abertos, diff) |
|:--|:--|:--|
| 1. técnica, link, licença, justificativa | Não passa (por pouco) | **O que se sustenta:** faster-whisper … SYSTRAN/faster-whisper … MIT e Ollama … ollama/ollama … MIT. **O que falha:** Ollama (Qwen2.5-Coder) … MIT e exige compilação C++ que atrasaria a entrega. **O que passa:** os dois links abrem nos repositórios certos e os dois mostram MIT. **Falhas:** (1) A linha 2 leva o nome do Qwen, mas link e licença valem só para o Ollama. A licença do modelo não está na folha. (2) A justificativa do C++ é fraca pois o whisper.cpp usa menos RAM, é mais rápido e tem Docker pronto. (3) Ollama lista o llama.cpp como backend, não é alternativo de fato. |
| 2. vídeo a partir do código-fonte | Passa (provisório) | `(.venv) PS C:\codigos\tec> python transcrever.py`; para rodar no notebook; §4: os dois commits, o comando e a saída aparecendo no terminal. Roda em PowerShell local. O link do YouTube está no ar. **Pendências:** (a) os dois commits são placeholders sem URL. (b) diretórios diferentes (`C:\codigos\tec` e `C:\codigos\projeto_taia\va2\tec`). (c) monkey patch precisa estar no commit. |
| 3. alteração mínima + auditoria cega | Não passa | **O que se sustenta:** um áudio do meu problema (`explicacao.mp3` gravado por mim) e o Whisper … errou … "estore". **Falhas:** (i) Não há § 6. (ii) Diff não aberto e muda muito a saída acrescentando Ollama. (iii) A tabela diz que avalia cruzando com AST/Diff, mas a demonstração só passa transcrição sem AST. (iv) O veredito do Qwen só foi testado num caso positivo; faltou controle (aluno falando bobagem) para provar se a avaliação discrimina a compreensão. |

### a minha resposta, sem IA

1. Separei a licença do Qwen (Apache 2.0) da licença do Ollama (MIT) na tabela e adicionei os links diretos para as metas nativas (whisper.cpp e llama.cpp) reforçando que a escolha atual prioriza pular o build no Windows nativo sem depender de contêineres Docker.
2. Inseri os hashes de commit (ac9cbe2 e 1464fbc) na documentação final atestando o registro. A diferença de diretório apontada no item 'b' reflete apenas o deslocamento para dentro da pasta formal da disciplina (va2/tec).
3. Concordo que o teste atual não injeta a AST, servindo apenas para testar a transcrição combinada à inferência do LLM na CPU local. A crítica da ausência de um "caso de falha/bobagem" é pertinente e usarei no desenho formal dos próximos experimentos.
