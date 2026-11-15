# Configuración de Decision Arena 0.8.1

Nombres tal como se ven en pantalla en español. Valores y límites: ver limites-0.8.1.md. Manual público con explicaciones y simuladores: https://claude.ai/artifact/LWRnWzs6sxsFBc3Nx2AD3K

## Ajustes del sitio
Ubicación: Administración del sitio › Extensiones › Módulos de actividad › Decision Arena. Todos tratan de la IA, que es opcional. Si no se usa IA, no hay nada que configurar.

### Bloque «Evaluación con IA»
- **Activar las funciones de IA**: interruptor general. Apagado, la sección de IA no aparece en las actividades y no sale ningún dato. Apagarlo no borra la configuración de las actividades ni las evaluaciones hechas. Recomendación: encender solo con proveedor preparado y decisión institucional tomada.
- **Proveedor IA**: «Subsistema de IA de Moodle» usa el proveedor configurado para todo el sitio en Administración del sitio › General › IA, con la acción de generar texto activada; no requiere clave en el plugin y el uso aparece en los informes de IA de Moodle. Las otras opciones (OpenAI, Anthropic, Google Gemini, DeepSeek) llaman directamente al proveedor con la clave y los modelos de esta página. Recomendación: subsistema de Moodle salvo que se necesite elegir modelo por actividad o no haya proveedores configurados en Moodle.
- **Clave de API**: solo con proveedor directo. Recomendar una clave exclusiva para Moodle con límite de gasto en el proveedor. Nunca pedir al usuario que la comparta.
- **Modelos**: uno por línea; el primero es el predeterminado. Vacío usa la lista propia del proveedor. Un nombre mal escrito o retirado provoca fallos. Si se retira un modelo que una actividad tenía elegido, la evaluación usa el primero de la lista.
- **Timeout de petición IA**: espera máxima de respuesta. Subir a 120 segundos solo ante fallos por tiempo con modelos lentos. No se aplica con el subsistema de IA de Moodle.
- **Máximo de caracteres enviados a la IA**: tope de texto del alumno por intento, repartido entre las decisiones con justificación; cada una conserva al menos 200 caracteres. Subir si se piden justificaciones largas.
- **Modo de anonimización**: estricta (recomendada) o básica. La estricta puede tapar nombres propios que no son personas.
- **Conservar el texto enviado a la IA**: guarda copia del texto enmascarado para auditoría. Recomendación: apagado, salvo exigencia de auditoría o investigación temporal.
- **Probar la conexión con la IA** (enlace en la descripción del bloque): envía una petición fija sin datos de alumnos y muestra el resultado o el error del proveedor. Usa los ajustes guardados. Primer paso de cualquier diagnóstico de IA.

### Bloque «Valores por defecto para actividades nuevas»
Solo rellenan el formulario de actividades nuevas; no cambian las existentes.
- **Un docente aprueba cada evaluación de la IA**: recomendado marcado.
- **Confianza necesaria para liberar automáticamente**: de 0 a 1; solo influye donde no se exige aprobación.
- **Peso de la IA en la nota (%)**: solo influye donde el docente hace que la IA cuente para nota.

## Ajustes de la actividad
Ubicación: actividad › Configuración.

### General y Escenario
- **Nombre de la actividad** y **Descripción**: estándar. Usar la descripción para explicar normas y avisar de no escribir datos personales.
- **Partir de** (solo al crear): plantilla o escenario vacío. Recomendar una plantilla la primera vez.
- **Justificación escrita**: Sin justificación, Opcional u Obligatoria. La IA exige que no esté desactivada. Con «Opcional», los intentos sin texto no reciben evaluación de IA.
- **Mostrar en el resultado las opciones no elegidas**: útil para aprender; desaconsejado si cuenta para nota y hay varios intentos.

### Intentos y calificación
- **Intentos permitidos**: 1 para evaluar; varios o ilimitado para practicar. Para una oportunidad extra individual, eliminar el intento.
- **Método de calificación**: visible con más de un intento.
- **Calificación máxima**: fijarla antes de que haya intentos, porque los intentos terminados no se recalculan; los criterios del escenario deberían sumarla.
- **Un docente revisa cada intento antes de publicar la nota**: retiene nota y desglose hasta la revisión. No activar si no se va a poder revisar. Es distinto de la aprobación de la IA.
- **Límite de tiempo**: sin pausas; cierre al volver a entrar o enviar y, si el alumno abandona, automático a los pocos minutos (requiere cron).
- **Número máximo de decisiones** (avanzado): 0 recomendado.

### Evaluación con IA (solo si el administrador la permite)
- **Evaluar con IA las justificaciones escritas**: activa la IA en la actividad.
- **Para qué se usa la IA**: «Solo feedback» (recomendado para empezar) o «Feedback y parte de la nota».
- **Peso de la puntuación de la IA en la nota (%)**: solo con parte de la nota. Recomendación: 20 a 30.
- **Feedback de la IA que ve el alumnado**: «Nada (solo docentes)» para pilotar; general; o general con detalle.
- **Un docente aprueba cada evaluación de la IA**: recomendado si la IA cuenta para nota.
- **Qué valora la IA en las justificaciones**: un criterio por línea con peso opcional tras barra vertical. Distinto de los criterios del escenario.
- **Orientaciones para la IA (opcional)**: nivel del alumnado, qué es una buena justificación, en qué ser exigente. Sin datos personales.
- **Modelo de IA** (avanzado): solo con proveedor directo.
- **Confianza necesaria para liberar automáticamente** (avanzado): solo si no se exige aprobación.

### Avanzado y finalización
- **Editar a mano el JSON del escenario** y **JSON del escenario**: solo usuarios avanzados; sustituye el escenario. Preferir importar y exportar en el constructor.
- **Intentos finalizados / Intentos a finalizar**: condición de finalización propia. El formulario no deja pedir más intentos de los permitidos.
- Grupos y restricciones de acceso: estándar de Moodle. Para abrir o cerrar por fecha, usar restricciones de acceso.

## Constructor de escenarios
- Variables: nombre, «Qué es bueno», valor inicial, mínimo y máximo. Dos a cuatro variables suelen bastar.
- Criterios: nombre, descripción, puntuación máxima, «Cómo se puntúa este criterio» y, en su caso, variables que deciden la puntuación.
- Nodos: tipo, título y situación. Opciones: texto, «Lleva a», feedback de consecuencia, efectos sobre variables y puntos para criterios.
- Herramientas: mapa del escenario, comprobación del escenario, comprobación de la puntuación, «Probar escenario».
- Partir de contenido existente: plantillas, banco de escenarios, redactar con cualquier asistente de IA, borrador con la IA del sitio, importar y exportar. Todas sustituyen el escenario completo previa confirmación.

## Configuraciones tipo
- Práctica formativa sin IA: intentos ilimitados, calificación más alta, opciones no elegidas visibles, justificación opcional.
- Examen: un intento, límite de tiempo, justificación obligatoria, revisión docente, opciones no elegidas ocultas.
- Piloto de IA: IA activada, solo feedback, aprobación docente marcada, feedback al alumnado «Nada».
- IA formativa en grupos grandes: solo feedback, sin aprobación obligatoria, umbral de confianza de fábrica, feedback general con detalle; revisar las retenidas.
- IA con peso en nota: aprobación docente marcada, peso bajo, criterios y orientaciones revisados tras un piloto.
