# Cortex Skill: Architectural Analysis

Este skill genera un análisis funcional y arquitectónico completo para propuestas a clientes a partir de un documento de requerimientos o conversación. Está diseñado para transformar necesidades de negocio en artefactos técnicos y ejecutivos de alta calidad, siguiendo un flujo secuencial estricto.

## Estructura del Proyecto

```text
.
├── .gitignore                          # Configuración de archivos ignorados
├── README.md                           # Documentación principal del proyecto
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
