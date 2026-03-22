# Design System — Paleta de Colores y Componentes

Aplica este sistema de diseño en todos los artefactos HTML del skill
(Artefactos 4, 5 y 8). Garantiza coherencia visual entre entregas.

**Tema: Claro y profesional.** Fondos blancos y grises neutros, acentos de color
controlados. No usar fondos oscuros ni navy. El objetivo es un documento que se
vea bien impreso y en pantalla sin depender de modo oscuro.

---

## ⚠️ REGLAS CRÍTICAS DE RENDERIZADO — LEER PRIMERO

Estas reglas garantizan que el HTML se vea igual en el chat de Claude
y al abrirlo en un navegador. Son OBLIGATORIAS en cada archivo.

### Regla 1 — Fondo blanco/neutro siempre como valor fijo en `html` y `body`

```css
html, body {
  background: #F8FAFC;      /* valor literal — nunca solo var() */
  background-color: #F8FAFC;
  color: #1E293B;
  min-height: 100vh;
  margin: 0;
  padding: 0;
}
#root {
  background: #F8FAFC;
  min-height: 100vh;
  color: #1E293B;
}
```

### Regla 2 — Meta `color-scheme` para que el navegador no fuerce tema del sistema

```html
<!-- OBLIGATORIO: va justo después de <meta charset> -->
<meta name="color-scheme" content="light" />
```

### Regla 3 — Forzar fondo desde JavaScript como fallback definitivo

```javascript
// Primera línea del <script type="text/babel">, ANTES de cualquier componente:
document.documentElement.style.background = '#F8FAFC';
document.body.style.background = '#F8FAFC';
document.body.style.color = '#1E293B';
document.body.style.margin = '0';
```

### Regla 4 — Estructura HTML base obligatoria

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8" />
  <meta name="color-scheme" content="light" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>[Nombre del artefacto]</title>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react/18.2.0/umd/react.production.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/react-dom/18.2.0/umd/react-dom.production.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/babel-standalone/7.23.5/babel.min.js"></script>
  <link href="https://fonts.googleapis.com/css2?family=Syne:wght@700;800&family=DM+Sans:wght@300;400;500&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <style>
    /* BLOQUE 1 — Reset y fondo base LITERAL */
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    html { background: #F8FAFC; min-height: 100%; }
    body { background: #F8FAFC; color: #1E293B; min-height: 100vh;
           font-family: 'DM Sans', sans-serif; }
    #root { background: #F8FAFC; min-height: 100vh; }

    /* BLOQUE 2 — Variables CSS */
    :root { /* ver paleta abajo */ }

    /* BLOQUE 3 — Estilos del componente */
  </style>
</head>
<body>
  <div id="root"></div>
  <script type="text/babel">
    // PRIMERA LÍNEA SIEMPRE — antes de definir componentes:
    document.documentElement.style.background = '#F8FAFC';
    document.body.style.background = '#F8FAFC';
    document.body.style.color = '#1E293B';
    document.body.style.margin = '0';

    // ... componentes React ...
  </script>
</body>
</html>
```

---

## Paleta Base (CSS Variables)

```css
:root {
  /* Fondos */
  --bg:        #F8FAFC;   /* blanco-gris principal */
  --bg2:       #F1F5F9;   /* gris muy suave — secciones alternas */
  --card:      #FFFFFF;   /* tarjetas y paneles */
  --card-alt:  #F8FAFC;   /* tarjeta alternativa */
  --sidebar:   #1E293B;   /* sidebar oscuro (único elemento dark permitido) */

  /* Texto */
  --text:      #1E293B;   /* casi negro — texto principal */
  --text-2:    #475569;   /* gris medio — texto secundario */
  --muted:     #94A3B8;   /* gris claro — labels, metadatos */
  --inverse:   #F8FAFC;   /* texto sobre fondos oscuros (sidebar, badges dark) */

  /* Acento principal — naranja marca */
  --orange:    #F97316;
  --orange-l:  #FED7AA;   /* fondo suave de badge naranja */
  --orange-d:  #EA580C;   /* hover/active */

  /* Bordes */
  --border:    #E2E8F0;   /* borde neutro principal */
  --border-2:  #CBD5E1;   /* borde un poco más visible */
  --border-accent: rgba(249,115,22,0.3);  /* borde con acento naranja */

  /* Estados */
  --success:   #16A34A;   --success-bg: #F0FDF4;
  --warning:   #D97706;   --warning-bg: #FFFBEB;
  --error:     #DC2626;   --error-bg:   #FEF2F2;
  --info:      #2563EB;   --info-bg:    #EFF6FF;

  /* Colores de capa — Artefacto 5 */
  --layer-users:    #2563EB;   /* azul */
  --layer-edge:     #F97316;   /* naranja */
  --layer-core:     #16A34A;   /* verde */
  --layer-data:     #7C3AED;   /* violeta */
  --layer-ext:      #DC2626;   /* rojo */

  /* Badges de servicio cloud — texto sobre fondo blanco */
  --svc-cloudfront: #2563EB;
  --svc-waf:        #DC2626;
  --svc-apigateway: #F97316;
  --svc-cognito:    #7C3AED;
  --svc-lambda:     #D97706;
  --svc-fargate:    #0369A1;
  --svc-bedrock:    #92400E;
  --svc-dynamodb:   #0F766E;
  --svc-s3:         #15803D;
  --svc-kms:        #6D28D9;
  --svc-sqs:        #065F46;
  --svc-telco:      #BE185D;
}
```

---

## Tipografía

```
Display / títulos:  Syne — weights 700, 800
Body / texto:       DM Sans — weights 300, 400, 500
Código / badges:    JetBrains Mono — weights 400, 500
```

---

## Componentes Recurrentes

### Tarjeta estándar
```css
.card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  transition: box-shadow 0.2s, border-color 0.2s;
}
.card:hover {
  box-shadow: 0 4px 12px rgba(0,0,0,0.08);
  border-color: var(--border-accent);
}
```

### Tarjeta con acento de color (borde superior)
```css
.card-accent {
  border-top: 3px solid var(--orange);  /* o el color de capa correspondiente */
}
```

### Badge de servicio cloud
```css
.svc-badge {
  display: inline-flex;
  align-items: center;
  padding: 3px 10px;
  border-radius: 6px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  font-weight: 500;
  border: 1px solid currentColor;
}
/* Aplicar con opacity en background: color + '18' o '22' */
.badge-cloudfront  { color: #2563EB; background: #EFF6FF; border-color: #BFDBFE; }
.badge-waf         { color: #DC2626; background: #FEF2F2; border-color: #FECACA; }
.badge-apigateway  { color: #EA580C; background: #FFF7ED; border-color: #FED7AA; }
.badge-cognito     { color: #7C3AED; background: #F5F3FF; border-color: #DDD6FE; }
.badge-lambda      { color: #B45309; background: #FFFBEB; border-color: #FDE68A; }
.badge-fargate     { color: #0369A1; background: #F0F9FF; border-color: #BAE6FD; }
.badge-bedrock     { color: #92400E; background: #FFFBEB; border-color: #FDE68A; }
.badge-dynamodb    { color: #0F766E; background: #F0FDFA; border-color: #99F6E4; }
.badge-s3          { color: #15803D; background: #F0FDF4; border-color: #BBF7D0; }
.badge-kms         { color: #6D28D9; background: #F5F3FF; border-color: #C4B5FD; }
.badge-sqs         { color: #065F46; background: #ECFDF5; border-color: #A7F3D0; }
.badge-telco       { color: #BE185D; background: #FDF2F8; border-color: #FBCFE8; }
```

### Encabezado de sección numerada
```css
.section-header {
  display: flex;
  align-items: center;
  gap: 16px;
  margin-bottom: 24px;
}
.section-number {
  font-family: 'Syne', sans-serif;
  font-size: 13px;
  font-weight: 800;
  color: var(--inverse);
  background: var(--orange);
  border-radius: 6px;
  padding: 4px 10px;
  letter-spacing: 1px;
}
.section-title {
  font-family: 'Syne', sans-serif;
  font-size: 22px;
  font-weight: 800;
  color: var(--text);
}
```

### Sidebar de navegación (SPA Staff — único elemento oscuro)
```css
.sidebar {
  width: 200px;
  background: var(--sidebar);   /* #1E293B — oscuro intencional */
  color: var(--inverse);
}
.nav-item        { color: #94A3B8; padding: 10px 20px; font-size: 13px; }
.nav-item.active { color: #FFFFFF; border-left: 3px solid var(--orange);
                   background: rgba(249,115,22,0.12); }
```

### Botón primario
```css
.btn-primary {
  background: var(--orange);
  color: white;
  border: none;
  border-radius: 8px;
  padding: 10px 24px;
  font-weight: 600;
  font-size: 14px;
  cursor: pointer;
  box-shadow: 0 1px 2px rgba(0,0,0,0.1);
  transition: background 0.2s, box-shadow 0.2s;
}
.btn-primary:hover { background: var(--orange-d); box-shadow: 0 4px 8px rgba(249,115,22,0.25); }
```

### Panel de detalle lateral (Artefacto 8)
```css
.detail-panel {
  width: 320px;
  background: var(--bg2);
  border-left: 1px solid var(--border);
  padding: 24px;
}
.dp-label {
  font-size: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--muted);
  font-weight: 600;
  margin-bottom: 8px;
}
.flow-path {
  background: #FFF7ED;
  border: 1px solid #FED7AA;
  border-radius: 6px;
  padding: 8px 12px;
  font-family: 'JetBrains Mono', monospace;
  font-size: 11px;
  color: var(--orange-d);
}
```

### KPI card (Dashboard)
```css
.kpi-card {
  background: var(--card);
  border: 1px solid var(--border);
  border-radius: 12px;
  padding: 20px 24px;
  box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.kpi-number {
  font-family: 'Syne', sans-serif;
  font-size: 32px;
  font-weight: 800;
  line-height: 1;
  color: var(--text);
}
.kpi-label {
  font-size: 11px;
  color: var(--muted);
  margin-top: 6px;
  text-transform: uppercase;
  letter-spacing: 1px;
}
```

### Status badge (tickets)
```css
.badge-open     { background: #FEF2F2; color: #DC2626; border: 1px solid #FECACA; }
.badge-progress { background: #FFFBEB; color: #D97706; border: 1px solid #FDE68A; }
.badge-closed   { background: #F0FDF4; color: #16A34A; border: 1px solid #BBF7D0; }
```

---

## Colores de capa — Artefacto 5 (fondos de subgrafo)

| Capa | Fondo suave | Borde / acento | Texto del header |
|------|-------------|----------------|-----------------|
| Usuarios | `#EFF6FF` | `#2563EB` | `#1D4ED8` |
| Edge y Seguridad | `#FFF7ED` | `#F97316` | `#C2410C` |
| Núcleo | `#F0FDF4` | `#16A34A` | `#15803D` |
| Datos | `#F5F3FF` | `#7C3AED` | `#6D28D9` |
| Integraciones | `#FEF2F2` | `#DC2626` | `#B91C1C` |

---

## Reglas de aplicación

1. **Fondos:** Siempre `#F8FAFC` o `#FFFFFF`. Nunca negro ni navy como fondo de página.
2. **El único elemento oscuro permitido:** la sidebar de navegación del staff (`#1E293B`).
3. **Acentos:** Naranja `#F97316` para CTAs, estados activos y elementos de marca.
4. **Servicios cloud:** Cada servicio usa su badge de color consistentemente en A5, A6 y A8.
5. **Sombras:** Suaves (`0 1px 3px rgba(0,0,0,0.06)`). Sin sombras dramáticas.
6. **Separadores de sección:** `background: var(--bg2)` para alternar secciones, no líneas fuertes.
7. **No usar:** gradientes dramáticos, fondos oscuros en tarjetas, texto blanco sobre fondo blanco.
