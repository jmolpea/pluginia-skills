# Ajustes y pruebas antes de escalar

## Regla de intervención
Resolver primero con lo que el cliente controla. Cambiar un solo elemento cada vez y conservar la intención pedagógica: no bajar la exigencia de la rúbrica ni el número de revisiones solo para que desaparezca un aviso, salvo que el responsable lo decida.
No usar la nota fijada por el docente para tapar un problema de configuración que se repetirá.

## Qué puede ajustar cada uno
| Quién | Ajuste | Efecto esperado |
|---|---|---|
| Docente | Modo y fechas, o fase manual | Cuándo se entrega, se empareja, se revisa y se publica |
| Docente | Requeridas por alumno y objetivo por entrega | Carga de trabajo y cuándo una entrega está completa |
| Docente | Modo del grupo de revisores y recíprocas | Quién es elegible |
| Docente | Recordatorio y reasignación | Ritmo del seguimiento |
| Docente | Máximos de entrega y de revisión | Peso de revisar en la nota |
| Docente | IA, respaldo, peso y prompts | Segunda opinión y plan B |
| Docente | Rúbrica: textos, pesos y puntos | Nota que propone cada revisión |
| Docente | Tipo de entrega y enunciado | Qué puede leer la IA y los compañeros |
| Tutor | Emparejar ahora, asignar a mano, volver a emparejar, fijar nota | Resolver casos concretos |
| Administrador | Cron, proveedor y límites de IA, avisos, permisos | Que lo automático ocurra |

## Ajustes frecuentes por síntoma
- Entregas sin revisor en grupos pequeños: quitar «Evitar revisiones recíprocas», volver a «Cualquier alumno elegible», bajar el objetivo.
- Alumnos que no llegan a las requeridas: igualar requeridas y objetivo; compensar con «Asignar manualmente»; no exigir la finalización por revisiones si el grupo es muy pequeño.
- Revisiones retiradas demasiado pronto: subir la reasignación; en Manual, si ocurre nada más abrir Revisión, comprobar la versión (corregido en 1.0.1).
- Feedback que no llega en Abierto: bajar el objetivo, asignar a mano o activar el respaldo por IA.
- Notas demasiado altas con trabajos flojos: puntuar los niveles desde 0; revisar descripciones de criterios.
- La IA no califica: cambiar el tipo de entrega a texto en línea o pedir .docx; recordar a los alumnos que acepten la política de IA.
- Nadie revisa a tiempo: dar valor a la nota de revisión, acortar el recordatorio.

## Secuencia de prueba
1. Anotar la línea base: configuración, síntoma y mensaje exacto.
2. Elegir un único cambio y decir qué se espera ver.
3. Probar en una copia de la actividad, en un curso de pruebas, con al menos tres cuentas con rol de estudiante. Una cuenta de profesor o administrador no sirve para la parte del alumno.
4. Para pruebas rápidas usar el modo Abierto o el Manual; en Programado hay que esperar a las fechas y al cron.
5. Ejecutar el cron o usar «Emparejar revisores ahora» cuando la prueba dependa del reparto.
6. Comprobar en el panel: estado, revisiones recibidas y hechas, «Requiere atención», desglose de nota y libro de calificaciones.
7. Con IA: las pruebas consumen peticiones del proveedor; pedir autorización. Los resultados pueden variar entre ejecuciones.
8. Registrar el resultado y decidir el siguiente cambio. No mezclar cambios.

## Registro de prueba
| Ensayo | Cambio único | Configuración y datos | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; simulado en papel; ejecutado en Moodle; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
Un cálculo hecho en el chat o en el simulador del manual es una simulación, no una ejecución.

## Aceptación
Cada entrega llega al objetivo o queda visible en «Requiere atención»; cada alumno puede alcanzar las requeridas; la nota reproduce el cálculo documentado; el feedback se publica cuando corresponde al modo; los avisos llegan a quien debe.

## Solicitud final al mantenedor
Solo cuando los ajustes probados no bastan. Incluir versión, síntoma, esperado, ajustes probados con resultado real, fallo residual, comportamiento funcional que se pide y criterio de aceptación. Sin código fuente ni datos de alumnos. Si falta acceso para probar, entregar el plan y declarar el bloqueo, sin concluir que los ajustes han fallado.
