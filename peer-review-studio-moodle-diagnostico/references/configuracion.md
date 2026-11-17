# Configuración de Peer Review Studio 1.0.2

Nombres tal como aparecen en pantalla (idioma español). Valores de fábrica verificados en la versión 1.0.2. Manual público con simuladores: https://claude.ai/artifact/RzMxCe9u5hXWWZy9kPUcXq

## Sitio (administrador)
Ruta: Administración del sitio › Extensiones › Módulos de actividad › Peer Review Studio.
- «Manual de configuración»: enlace al manual.
- «Revisión con IA»: texto informativo y línea «Estado». No hay campos. Con proveedor disponible ofrece «probar la revisión con IA».
- «Probar la revisión con IA» › «Ejecutar la prueba»: envía una petición mínima y dice si el modelo responde en el formato necesario. Cuenta como uso de IA.
Fuera del plugin, el administrador prepara:
- Proveedor de IA de Moodle con la acción «Generar texto» (Administración del sitio › General › IA › Proveedores de IA). Solo para la IA.
- Límites de peticiones del proveedor: suficientes para una tanda (entregas + revisiones).
- Cron en marcha y tarea «Emparejar revisores y hacer seguimiento de las revisiones pendientes» activa (cada 10 minutos).
- Avisos: seis tipos, activos por notificación y correo.
- Permisos por defecto. Para un auditor: ver la actividad y ver el panel del tutor.

## Actividad: General
- «Nombre de Peer Review Studio»: obligatorio.
- «Descripción»: el enunciado. Con IA, se envía como contexto; conviene que explique la tarea y pida no incluir datos personales.

## Actividad: Ajustes del flujo de trabajo
- «Tipo de entrega» (Subida de fichero): fichero, texto en línea o ambos. Con IA, preferir texto en línea o .docx.
- «Modo de flujo de trabajo» (Programado por fechas): Programado, Manual o Abierto / autoformativo. Programado para cursos con calendario común; Abierto para cursos sin fechas; Manual para controlar cada paso.
- «Fase manual» (Entrega; solo en Manual): Entrega, Asignación, Revisión, Feedback, Cerrada. Los plazos de recordatorio y reasignación empiezan al abrir Revisión. Recomendación: no ir a Feedback con entregas sin revisar.
- «Apertura de entregas» (sin fecha; solo Programado): opcional.
- «Cierre de entregas» (obligatoria en Programado): posterior a la apertura.
- «Fecha límite de revisión» (obligatoria en Programado): posterior al cierre. Dejar más días que el umbral de reasignación.
- «Revisiones que cada alumno debe completar» (2): contador, nota de revisión y finalización. No decide cuántas se asignan.
- «Objetivo de revisiones recibidas por entrega» (2): cuántos revisores se buscan por entrega. Recomendación: igual que el anterior.
- «Activar asignación automática de revisores» (sí): si se desmarca, el tutor asigna a mano y no hay reasignación automática.
- «Modo del grupo de revisores» (Cualquier alumno elegible): mismo grupo o grupos distintos. Exige grupos bien formados y suficientemente grandes.
- «Evitar revisiones recíprocas» (no): solo en grupos grandes.
- «Recordar a revisores inactivos tras (días)» (2; 0 desactiva).
- «Reasignar revisiones no completadas tras (días)» (4; 0 desactiva; mayor que el recordatorio).

## Actividad: Ajustes de calificación
- «Calificación máxima de la entrega» (100).
- «Calificación máxima de revisión» (0): recomendable darle entre un 10 y un 20 % del total.
- «Categoría de calificación» y «Calificación para aprobar»: estándar de Moodle.

## Actividad: Revisión por IA (opcional)
- Línea de estado: disponible, sin proveedor, o IA desactivada en el curso. En los dos últimos casos no se puede guardar con la casilla marcada.
- «Activar segunda revisión por IA» (no).
- «Usar la revisión por IA como respaldo cuando no llega ninguna revisión de compañeros» (no): recomendable en cursos sin tutor.
- «Peso de la nota de la IA (%)» (30): 0 para que la IA solo comente.
- «Prompt de IA: calificar la entrega» y «Prompt de IA: evaluar al revisor»: traen un texto de fábrica; vaciarlos lo restaura. No pedir en ellos formatos de salida: el plugin impone el suyo. Sí se puede matizar tono, idioma y qué valorar.

## Actividad: Ajustes de la rúbrica
Cinco huecos «Criterio 1» a «Criterio 5» con «Etiqueta del criterio», «Descripción del criterio», «Peso del criterio» y, por nivel, etiqueta y puntuación. Etiqueta vacía = no se usa.
Recomendaciones: criterios observables y distintos entre sí; descripciones que digan en qué fijarse; niveles con diferencias claras; puntuar desde 0 si el peor nivel debe valer cero; cerrar la estructura antes de que empiece la revisión.

## Actividad: apartados de Moodle
- «Modo de grupo» y «Agrupamiento»: deciden qué ven los tutores y qué grupos cuentan para el modo del grupo de revisores.
- Finalización: «Los estudiantes deben entregar su trabajo» y «Los estudiantes deben completar las revisiones entre pares requeridas». La segunda solo es justa si el reparto da a todos suficientes revisiones.

## Panel del tutor y página de una entrega
- «Emparejar revisores ahora»: reparto inmediato (con asignación automática y en fase que lo permita).
- «Requiere atención»: «Sin ninguna revisión; requiere a un tutor», «No hay ningún revisor elegible», «Revisada parcialmente; sin revisores pendientes», «Pendiente de emparejamiento», «Pendiente de asignación manual».
- «Asignar manualmente»: entre los «Revisores disponibles».
- «Retirar revisiones abiertas y volver a emparejar»: conserva las revisiones recibidas.
- «Nota final fijada por el docente» › «Guardar calificación»: sustituye la nota calculada; vacío la restaura.

## Configuraciones de partida
| Situación | Propuesta |
|---|---|
| Clase con fechas | Programado; 2 y 2; recordatorio 2, reasignación 4; una semana de revisión; revisión con valor |
| Autoformativo sin tutor | Abierto; objetivo 1 o 2; recordatorio 3, reasignación 7; IA con respaldo |
| Grupo de 3 a 5 | Objetivo y requeridas 1 o 2; sin evitar recíprocas; cualquier alumno |
| Control total | Manual o asignación automática desmarcada |
