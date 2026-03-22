# Cortex Skill: Architectural Analysis

[Versión en Inglés disponible aquí](README.md)

Este skill genera un análisis funcional y arquitectónico completo para propuestas a clientes a partir de un documento de requerimientos o conversación. Está diseñado para transformar necesidades de negocio en artefactos técnicos y ejecutivos de alta calidad, siguiendo un flujo secuencial estricto. A sido probado con claude.ia / claudde code . Dependerá de las capcidades de cada agente la generación de artefactos como las infografías en HTML

## Estructura del Proyecto

```text
.
├── .gitignore                          # Configuración de archivos ignorados
├── README.md                           # Documentación principal del proyecto (Inglés)
├── README_es.md                        # Documentación del proyecto (Español)
└── cortex-skill-architectural-analysis/ # Directorio raíz del skill
    ├── SKILL.md                        # Definición y lógica del skill
    └── references/                     # Plantillas y guías de referencia
```

## Arquitectura del Skill

### Arquitectura Conceptual

El skill opera bajo un modelo de **bloques secuenciales** con compuertas de aprobación (*gates*). Cada bloque genera un conjunto de artefactos que sirven de insumo para el siguiente.

```mermaid
graph TD
    P0[Paso 0: Cuestionario de Contexto] --> |Aprobación| BA[Bloque A: Diagnóstico y Contexto]
    BA --> |Aprobación| BB[Bloque B: Narrativa Ejecutiva]
    BB --> |Aprobación| BC[Bloque C: Detalle Técnico]
    
    subgraph "Bloque A (Interno/Cliente)"
        A1[A1: Resumen Ejecutivo]
        A2[A2: RNFs]
        A3[A3: Mapa de Procesos]
    end
    
    subgraph "Bloque B (Ejecutivo)"
        A4[A4: Infografía]
        A5[A5: Arquitectura Conceptual]
    end
    
    subgraph "Bloque C (Técnico)"
        A6[A6: Arq. Contextual]
        A7[A7: Secuencias Atómicas]
        A8[A8: Prototipos HTML]
        A9[A9: Riesgos]
        A10[A10: ADRs]
        A11[A11: OpEx]
        A12[A12: Equipo]
        A13[A13: Sprints]
        A14[A14: RACI]
    end
```

### Diagrama de Secuencia de Operación

El flujo de interacción entre el usuario y el skill garantiza que no haya sobreingeniería y que los artefactos sean consistentes.

```mermaid
sequenceDiagram
    participant U as Usuario
    participant S as Cortex Skill (Arquitecto)
    
    U->>S: Proporciona Requerimiento / RFP
    S->>S: Activa Paso 0 (Gate Obligatorio)
    S->>U: Presenta Cuestionario de Contexto
    U->>S: Confirma Respuesta / Ajusta Stack
    
    Rect rgb(240, 240, 240)
        Note over S, U: BLOQUE A: Diagnóstico
        S->>U: Genera A1-A3 con micro-checkpoints
        U->>S: Aprueba Bloque A (Checkpoint A)
    End
    
    Rect rgb(220, 240, 220)
        Note over S, U: BLOQUE B: Narrativa
        S->>U: Genera A4-A5 (Visuales/Estratégicos)
        U->>S: Aprueba Bloque B (Checkpoint B)
    End
    
    Rect rgb(200, 220, 255)
        Note over S, U: BLOQUE C: Detalle Técnico
        S->>U: Activa PDA (Protocolo de Decisiones)
        U->>S: Confirma Decisiones Técnicas
        S->>U: Genera A6-A14 (Especificación Técnica)
    End
    
    S->>U: Entrega Empaquetado Final (.md, .html, .mmd)
```

## Características Principales

- **Propagación de Contexto**: El stack tecnológico y los nombres de componentes definidos inicialmente se mantienen idénticos en todos los artefactos.
- **Protocolo de Decisiones Arquitectónicas (PDA)**: Antes de definir arquitectura técnica, se consultan trade-offs de cómputo, datos e integración.
- **Atomicidad en Secuencias**: Los diagramas de secuencia se dividen en flujos mínimos verificables.
- **Prototipado Derivado**: Las pantallas de UI se generan directamente de los pasos de los diagramas de secuencia.

## Uso del Skill

Para activar el skill, simplemente carga un documento de requerimientos o describe tu sistema. El skill responderá iniciando el **Paso 0** para capturar el contexto tecnológico base (Nube, Backend, Frontend, etc.).

> **Importante**: No se avanzará a la generación de artefactos hasta que el Paso 0 sea confirmado explícitamente.

## Guía de Diseño (Design System)

Todos los artefactos HTML generados siguen un sistema de diseño premium, con paletas claras y tipografía moderna, asegurando una presentación profesional para el cliente final. Reportarse a `references/design-system.md` para más detalles.

## Ejemplos de Artefactos

A continuación se presentan ejemplos de algunos de los artefactos que este skill es capaz de generar como parte de un análisis arquitectónico de un requerimiento.

### 1. Arquitectura Conceptual
Este diagrama muestra la interacción del sistema con actores externos y capas internas.

![Arquitectura Contextual](examples/arquitectura_conceptual.png)

### 1.2 Arquitectura Contextual
Este diagrama muestra la relación entre los componentes del sistema.

![Arquitectura Contextual](examples/arquitectura_contextual.png)

### 2. Infografía de Problema y Solución
Visualización ejecutiva de los desafíos del cliente y la propuesta de valor.

![Infografía de Problema y Solución](examples/problema_solucion_inforgrafia.png)

### 3. Diagramas de Secuencia Atómicos
Ejemplos de flujos detallados para diagnóstico y reporteo.

#### Detalle de Diagnóstico Reactivo
```mermaid
sequenceDiagram
    actor Operador as Personal de Soporte
    participant Orch as Cortex Orchestrator
    participant Diag as Diagnostic Agent
    participant Know as Knowledge Agent
    participant OraDB as Oracle Autonomous DB AI
    participant Gemini as Gemini API

    Note over Operador,Gemini: ── FLUJO FELIZ (P03 — Diagnóstico reactivo de incidente) ──
    Note right of Operador: P95 < 5s extremo a extremo (RNF Latencia)

    Operador->>Orch: "Falla en WebLogic-Prod-07. AdminServer no responde"
    Note right of Orch: Supervisor detecta intención: diagnóstico de incidente
    Orch->>Diag: task("diagnosticar AdminServer WebLogic-Prod-07")
    Diag->>OraDB: get_server_status("WebLogic-Prod-07")
    OraDB-->>Diag: {status: "degraded", cpu: 98%, heap: 95%, threads: "stuck"}
    Diag->>OraDB: get_server_logs("WebLogic-Prod-07", last=100)
    OraDB-->>Diag: [log_entries con OutOfMemoryError y stuck threads]
    Diag->>Know: task("buscar OutOfMemoryError WebLogic stuck threads")
    Know->>OraDB: vector_search("OutOfMemoryError WebLogic AdminServer")
    OraDB-->>Know: [{runbook: "wl_oom_remediation.md", score: 0.91}]
    Know-->>Diag: contexto_runbook
    Diag->>Gemini: analyze(logs + status + runbook, model=pro)
    Gemini-->>Diag: {causa_raiz: "Heap exhaustion por thread leak", remediacion: [...]}
    Diag-->>Orch: diagnostico_estructurado
    Orch-->>Operador: Diagnóstico + causa raíz + pasos de remediación sugeridos
    Note right of Orch: AuditLog registra todas las tool calls
```

#### Generación de Reportes
```mermaid
sequenceDiagram
    actor Operador as Personal de Soporte
    participant Orch as Cortex Orchestrator
    participant Rep as Reporting Agent
    participant Gemini as Gemini API
    participant Audit as AuditLog

    Note over Operador,Audit: ── FLUJO FELIZ (P06 — Generación de reporte de incidente) ──

    Operador->>Orch: "Genera el reporte del incidente de WebLogic-Prod-07"
    Note right of Orch: Supervisor recupera contexto de la sesión actual
    Orch->>Rep: task("generar reporte de incidente", contexto_sesion)
    Rep->>Audit: get_session_actions(thread_id)
    Audit-->>Rep: [{tool: "get_server_logs", result: ...}, {tool: "get_server_status", result: ...}]
    Rep->>Gemini: generate_report(acciones + diagnostico + plantilla_reporte, model=flash)
    Gemini-->>Rep: reporte_estructurado
    Note right of Rep: Estructura: resumen · timeline · diagnóstico · lecciones aprendidas
    Rep-->>Orch: {reporte: reporte_estructurado, formato: "markdown"}
    Orch->>Audit: log_action("generate_report", actor=Operador, resultado=ok)
    Orch-->>Operador: Reporte completo del incidente

    Note over Operador,Audit: ── RUTA ALTERNATIVA — Sin sesión activa de diagnóstico ──
    Operador->>Orch: "Genera reporte" (sin diagnóstico previo en sesión)
    Orch-->>Operador: "No encontré diagnóstico en la sesión actual. ¿Deseas iniciar uno primero?"
```

### 4. Prototipos de Pantallas
Ejemplo de interfaces generadas para el sistema.

![Prototipo de Pantallas](examples/prototipo_pantallas.png)

## Autor

- **Autor**: Alejandro Sánchez C.
- **Contacto**: [alejandro.sanchez.caceres@gmail.com](mailto:alejandro.sanchez.caceres@gmail.com) / [Linktr.ee](https://linktr.ee/alejandro.sanchez.caceres)
