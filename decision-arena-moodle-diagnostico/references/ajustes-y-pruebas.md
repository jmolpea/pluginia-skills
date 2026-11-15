# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero una solución con lo que el cliente puede cambiar: ajustes del sitio, ajustes de la actividad, diseño del escenario y textos que guían a la IA. Cambiar solo el elemento que explique el problema.
Conservar objetivos de aprendizaje, calificación máxima, criterios y exigencia. No bajar el umbral de confianza ni quitar la aprobación docente para ocultar valoraciones dudosas.
No proponer cambios sobre intentos reales con nota publicada sin advertir de su efecto.

## Qué puede ajustar el cliente
| Elemento | Revisar | Ajuste que se puede probar |
|---|---|---|
| Ajustes del sitio | Interruptor de IA, proveedor, clave, modelos, tiempo de espera, máximo de caracteres, anonimización | Corregir clave o modelo, subir tiempo de espera o caracteres, cambiar el modo de anonimización |
| Ajustes de la actividad | Justificación, intentos, método, calificación máxima, revisión, tiempo | Hacer obligatoria la justificación, ajustar intentos o tiempo, activar o quitar la revisión |
| Sección de IA | Uso de la IA, peso, feedback visible, aprobación, umbral | Empezar por «Solo feedback» y «Nada», después abrir gradualmente |
| Criterios de la IA | Criterios observables, sin solaparse, pesos coherentes | Reformular criterios, reducir su número, ajustar pesos |
| Orientaciones para la IA | Nivel del alumnado, qué es una buena justificación, tono | Añadir dos o tres frases concretas |
| Escenario | Variables, sentido, rangos, efectos, puntos, criterios que suman el máximo | Ampliar efectos, cambiar valores iniciales, ligar criterios a variables, añadir finales |
| Proveedor | Saldo, límites, disponibilidad del modelo | Cambiar de modelo o ampliar límites en el proveedor |

## Entorno de prueba recomendado
- Duplicar la actividad y ocultar la copia al alumnado.
- Para la puntuación por reglas: «Probar escenario». No guarda nada y muestra la puntuación del recorrido.
- Para intentos, tiempo, revisión e IA: un usuario de prueba con rol de estudiante. La vista previa no llama a la IA ni pide justificación.
- Para la conexión: «Probar la conexión con la IA», sin datos de alumnos.
- Avisar de que las pruebas con IA consumen saldo del proveedor.

## Secuencia
1. Registrar la línea base: qué se observa, sin atribuir causas.
2. Elegir un cambio único pertinente y explicar por qué.
3. Ejecutar la prueba en la copia con la misma entrada: mismo recorrido y mismas justificaciones.
4. Comparar: estado del intento, desglose por criterios, nota, estado de la IA, confianza, alertas, lo que ve el alumno y lo que llega al libro de calificaciones.
5. Para variabilidad de la IA, proponer tres ejecuciones por condición con el mismo texto. No ejecutarlas sin autorización del responsable.
6. Repetir con otro ajuste si el resultado lo justifica. No mezclar cambios.
7. Si los ajustes probados no resuelven el síntoma, preparar la solicitud al mantenedor.

## Pruebas controladas habituales
- Conexión: guardar ajustes, lanzar la prueba, anotar tiempo de respuesta o error literal.
- Activación de la IA: intento de prueba con una justificación; comprobar que aparece «Pendiente» y que pasa a «Completada» tras el cron.
- Sin justificación: intento de prueba sin texto; debe terminar sin evaluación de IA.
- Liberación: con aprobación desmarcada, comparar un texto razonado y uno de dos palabras; el segundo debería quedar retenido por baja confianza o alerta (resultado probable, no garantizado).
- Nota combinada: comprobar con la fórmula del peso que la nota publicada coincide tras la liberación.
- Recorte: justificación más larga que su parte del máximo; activar temporalmente la conservación del texto enviado para ver el corte, y desactivarla después.
- Anonimización: texto con un correo y un nombre inventados; comprobar las marcas en el texto conservado.
- Límite de tiempo: límite de dos minutos; dejar pasar el tiempo y volver a entrar; el intento debe cerrarse y puntuarse. Variante sin volver a entrar: pasados unos 15 minutos con el cron en marcha, el intento debe aparecer cerrado en el informe.
- Método de calificación: tres intentos de prueba con recorridos distintos; comparar con el libro de calificaciones.
- Reescalado: criterios que no suman la calificación máxima; comprobar el aviso y el desglose.

## Registro de prueba
| Ensayo | Cambio único | Entrada y configuración | Estado | Resultado observado | Conclusión |
|---|---|---|---|---|---|
Estados permitidos: diseñado; simulación; ejecutado en Moodle; pendiente de acceso; no resuelto; resuelto en las condiciones probadas.
Tres repeticiones no demuestran ausencia de errores en todos los casos.

## Aceptación
La nota por reglas coincide con el desglose y con la comprobación del constructor para ese recorrido. La evaluación de IA termina en «Completada», se libera o se retiene según la configuración, el alumno ve exactamente lo configurado y el libro de calificaciones refleja el método elegido.

## Solicitud final al mantenedor
Preparar únicamente tras ajustes probados e insuficientes:
- Versiones, síntoma y resultado esperado.
- Configuración y escenario relevantes, anonimizados.
- Ajustes probados y resultados reales, diferenciados de simulaciones.
- Fallo residual y evidencia disponible o pendiente.
- Cambio funcional solicitado y criterios de aceptación; no código fuente.
Si la ejecución está bloqueada, entregar el plan preparado y declarar el bloqueo; no afirmar que los ajustes han fallado.
