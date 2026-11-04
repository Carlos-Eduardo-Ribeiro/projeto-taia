# Arquitetura: Rastro Cognitivo

```mermaid
flowchart TD
    classDef pessoa fill:#d4edda,stroke:#28a745,stroke-width:2px,color:#155724;
    classDef regra fill:#cce5ff,stroke:#007bff,stroke-width:2px,color:#004085;
    classDef ia fill:#fff3cd,stroke:#ffc107,stroke-width:2px,color:#856404;

    subgraph PC["PC do Aluno (Processamento 100% Local)"]
        N1(["1. Aluno salva/commita alteração"]):::pessoa --> N2
        N2["2. Extensão lê diff e extrai AST"]:::regra --> N3
        N3["3. Filtro compara AST por mudança vital"]:::regra
        N3 -- Sem mudança estrutural --> F(["Fim: fluxo normal liberado"]):::pessoa
        N3 -- Com mudança estrutural --> N4
        N4(["4. IDE pausa e abre microfone para justificar"]):::pessoa --> N5
        N5{"5. Transcrição do áudio - Whisper"}:::ia --> N6
        N6["6. Empacota transcrição, AST e rubrica"]:::regra --> N7
        N7{"7. Avalia compreensão da arquitetura - Qwen"}:::ia --> N8
        N8["8. Exibe veredito e atualiza relatório local"]:::regra
    end
    
    subgraph Servidor["Servidor da Faculdade / Moodle"]
        N9["9. Gera dashboard consolidado para professor"]:::regra
    end
    
    N8 ==>|Envia apenas métricas de acerto| N9