# Script de orquestração para rodar a Arena no Antgravity CLI
# Requisito: Antgravity CLI e ferramentas de redirecionamento de logs configurados.

Write-Host "[*] Inicializando Arena: O Futuro do Trabalho..." -ForegroundColor Cyan

$TEMA = "Como a robótica avançada e a IA impactarão a classe trabalhadora global até 2040?"
$LOG_FILE = "../resultados/debate_log_$(Get-Date -Format 'yyyyMMdd_HHmm').md"

Write-Host "[*] Gerando Tópico de Abertura com o Moderador (Com Busca na Web)..."
antgravity prompt --system-file ../prompts/moderador.md --tools search --temp 0.3 "Inicie o debate apresentando um dado real sobre automação e faça a primeira pergunta para os agentes." > $LOG_FILE

Write-Host "[*] Turno 1: Agente Utópico (Aurora)"
$ARG_UTO = antgravity prompt --system-file ../prompts/utopico.md --temp 0.8 "Responda à abertura do moderador com sua visão."
$ARG_UTO >> $LOG_FILE

Write-Host "[*] Turno 2: Agente Distópico (Orion - Thinking Model)"
# Assumindo que o CLI possui flag para ativar modelos de raciocínio
$ARG_DIS = antgravity prompt --system-file ../prompts/distopico.md --temp 0.2 --enable-thinking "Refute os argumentos utópicos apresentados: $ARG_UTO"
$ARG_DIS >> $LOG_FILE

Write-Host "[*] Processo concluído. Log salvo em: $LOG_FILE"
Write-Host "[!] Verifique os logs para iniciar o relatório em LaTeX (Atividade 2)."
