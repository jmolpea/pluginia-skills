# Configuración y diseño pedagógico

Revisado para la versión 1.7.2 el 15-11-2026. Para la lista completa de ajustes, sus nombres de pantalla y valores de fábrica, ver configuracion.md y el manual público: https://claude.ai/artifact/FsE6HtPSgw77e3w7uVcKsk

## Configuración verificable
Valores predeterminados observados: confianza 7/10, máximo 3 evaluaciones por estudiante y tarea, máximo 50 solicitudes diarias por tarea.
Límites horarios opcionales: 100 para el sitio y 10 por usuario, desactivados por defecto. No confundir topes horarios con el diario de tarea.
Confirmar los valores realmente guardados. No confundir intentos de evaluación del tutor con intentos permitidos de entrega en Moodle.
Activar uso de rúbrica en el tutor y comprobar que el método activo de Moodle es rúbrica o guía, según corresponda.
Verificar que existe una definición utilizable. No inventar un ajuste máximo de criterios no documentado.
Usar un usuario de prueba con rol de alumno para comprobar ejecución y visibilidad: las entregas de cuentas que pueden calificar no se corrigen.
Comprobar que la tarea usa el flujo de trabajo de calificación antes de confiar en que una corrección quedará retenida para revisión.
Si se publica sin revisión docente, adaptar el texto de aviso: el de fábrica promete que un profesor revisará la nota.

## Prompt
Definir qué evidencia cuenta y cómo aplicar cada nivel. Evitar instrucciones que obliguen a devolver un formato incompatible con el que espera el plugin.
El plugin ya incorpora descripción, rúbrica y puntos de Moodle. No duplicar toda la rúbrica dentro del prompt por defecto.
Mantener las reglas esenciales de la actividad al principio de la descripción, dentro de los 8.000 caracteres efectivos, y eliminar redundancias. No presentar esa reorganización como solución si la pérdida real está en un archivo.
Solicitar evaluación de todos los criterios con nombres y niveles reconocibles y no ambiguos. Preferir correspondencia exacta. En 1.7.2 se pueden ensayar referencias cortas si son subcadenas literales únicas de los nombres de Moodle, por ejemplo «Criterio 1» cuando solo hay «Criterio 1» a «Criterio 4». Verificar unicidad: «Criterio 1» también puede coincidir con «Criterio 10». No extrapolar este recurso a versiones no verificadas. No convertir el prompt en un sustituto de la configuración de Moodle.
Evitar exigir feedback muy extenso cuando debe compartir presupuesto con la respuesta estructurada.
No pedir en el prompt un idioma, un formato de salida o un tratamiento de la confianza distintos de los que el plugin añade por su cuenta: la retroalimentación sale en el idioma de la entrega.
Recordar que la IA solo ve los primeros 8.000 caracteres de la descripción y ningún adjunto del enunciado: lo que deba saber para corregir tiene que estar en ese texto o en el prompt.
No incluir código del plugin ni revelar instrucciones privadas del mantenedor.

## Rúbrica
Usar criterios distinguibles, descriptores observables y niveles que no se solapen.
Conservar puntuaciones en los campos de Moodle. Si se mencionan además en texto, comprobar que coincidan; la duplicación por sí misma no prueba un fallo.
Evitar nombres idénticos para criterios diferentes, niveles vacíos y textos de niveles que sean simples fragmentos de otros.
No eliminar detalle académico necesario solo para acortar. Separar instrucciones extensas del desempeño observable que define cada nivel.
Evaluar globalmente o por apartados/preguntas según los objetivos. Justificar cualquier cambio de estructura.
Para criterios visuales, asegurar que la evidencia llega por un formato que el plugin y el proveedor puedan procesar. Pedir revisión humana si no puede verificarse.
No otorgar cero automáticamente por un fallo de lectura: distinguir fallo técnico de ausencia de evidencia académica.

## Propuesta de mejora
Cuando el usuario solicite reescritura, entregar el prompt y/o la rúbrica completos, señalar cambios y conservar ponderaciones salvo que se solicite modificarlas.
Explicar qué problema resuelve cada cambio. Probar primero en una actividad de prueba con evidencia conocida y revisión del docente.

## Coherencia de puntuaciones
Comparar cada número del prompt con los niveles realmente configurados. Si Moodle admite solo 1, 3 y 5, no solicitar intervalos 0–1, 2–3 o 4–5.
Con cuatro criterios de 1, 3 y 5, la suma directa solo puede ser 4, 6, 8, 10, 12, 14, 16, 18 o 20. Esto no prueba que la nota final transformada por Moodle deba tener esos valores.
Mantener coherentes niveles individuales, total narrativo y nivel global. Detectar contradicciones ya en tandas anteriores; no asumir que un síntoma sea nuevo sin compararlas.
Distinguir bajo desempeño de baja confianza: una respuesta claramente insuficiente puede evaluarse con alta confianza.
Distinguir ausencia de respuesta académica de imposibilidad técnica de leerla. No prescribir una nota por un fallo del extractor.
No prometer que las comprobaciones escritas en el prompt sustituyen una validación ejecutada por el software.

## Prioridad de soluciones
Aplicar references/ajustes-y-pruebas.md antes de proponer cambios de código. Entregar versiones completas cuando se soliciten y explicar diferencias. Conservar objetivos, escala, pesos y política de aprobación. Registrar las pruebas antes de recomendar al administrador un cambio del plugin.
