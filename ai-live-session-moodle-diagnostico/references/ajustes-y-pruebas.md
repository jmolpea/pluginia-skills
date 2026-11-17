# Ajustes y pruebas antes de escalar

## Regla de intervención
Buscar primero una solución con ajustes del sitio, de la actividad o del bloque. Cambiar solo el elemento que explique el problema y una sola variable por prueba.
Conservar objetivos, criterios, niveles y pesos. No desactivar la validación del tutor para «desatascar» notas ni subir límites sin explicar el efecto en el coste.
Probar en «Probar como alumno» (IA real, coste real, sin nota en el libro) o en una copia de la actividad con un alumno de prueba. «Borrar mi prueba» permite repetir desde cero.
Recordar que los cambios en un bloque afectan desde ese momento a quienes ya lo empezaron; lo ya hecho no cambia.

## Lista de revisión
| Elemento | Revisar | Ajuste que se puede probar |
|---|---|---|
| Claves y proveedor | Clave del proveedor que usa el modelo de la actividad; saldo | «Probar la conexión»; cambiar de modelo dentro del mismo proveedor |
| Límites del sitio | Alumnos simultáneos × 8 llamadas por minuto | Subir el límite del sitio; mantener 30 por usuario |
| Proveedor de reserva | Caídas o cuotas del principal | Elegir otro proveedor con su clave |
| Voz | Proveedor de TTS y su clave; voz del avatar | Cambiar a voces del navegador para aislar un fallo de voz |
| Cron | Evaluaciones y borradores que no llegan | Confirmar que se ejecuta cada minuto |
| Fechas e intentos | Apertura, cierre, intentos, excepciones | Excepción de usuario en lugar de cambiar la actividad |
| Cortes y preguntas | Final real del vídeo; preguntas dentro del fragmento; tramos de más de 5 minutos | Corregir el final; mover o borrar la pregunta sobrante |
| Misión | Tarea concreta y resultado comprobable | Reescribir la tarea; añadir «Qué debe mostrar la imagen» |
| Avatar | Tono y personalidad coherentes con lo que se evalúa | Cambiar solo el tono; después la personalidad |
| Rúbrica | Criterios audibles, niveles con conductas, pesos que sumen 100 | Separar criterios solapados; describir el nivel suficiente |
| Instrucciones para la evaluadora | Solución del caso; qué no penalizar | Añadir la solución y una regla por problema observado |
| Pesos de la nota | Reparto entre vídeo, entregable y conversación | Ajustar sin tocar la rúbrica |
| Reloj | Pausas por cortes; duración | «Tiempo que el reloj puede detenerse»; duración de la conversación |

## Pruebas controladas
1. Conexión: «Probar la conexión» antes y después de cambiar una clave. Resultado esperado: «Correcto en N ms» en chat y voz.
2. Recorrido mínimo: actividad de un bloque con vídeo corto, una pregunta, práctica de 2 minutos y conversación de 3. Comprobar cada fase en modo prueba.
3. Voz: misma actividad con «Proveedor de TTS» en OpenAI o Gemini y después en voces del navegador. Si solo falla la primera, el problema es la clave o la cuota de voz.
4. Micrófono: «Comprobar mi micrófono» en la portada, en Chrome y por https. Si falla, repetir escribiendo: la conversación debe funcionar igual.
5. Límites: bajar temporalmente el límite por usuario en un sitio de pruebas y verificar que aparece un código con la letra L; restaurarlo.
6. Evaluación: una conversación de prueba con respuestas claras para cada criterio. Verificar puntuación por criterio, citas y nota combinada con los pesos.
7. Avisos: una conversación con una sola frase corta debe quedar «Por revisar» con el aviso de poca participación, aunque la validación esté desactivada.
8. Entregable: subir una imagen legible y otra irrelevante en dos pruebas; comparar lo que la IA describe y su puntuación.
9. Datos corregidos: escribir la respuesta con mayúsculas, acento o espacios distintos; debe darse por buena.
10. Publicación: con la validación activada, confirmar que el alumno ve la espera; publicar; comprobar libro de calificaciones y aviso.
11. Segundo intento: tras publicar, comprobar que aparece «Repetir este bloque» y que se conserva el resultado del vídeo.
12. Reserva: no hay forma segura de provocar una caída del proveedor; verificar solo que la clave de reserva es válida con una actividad que use un modelo de ese proveedor.
Registrar para cada prueba: fecha, qué se cambió, resultado real y si queda pendiente. No dar por probado lo que solo está preparado.

## Cuándo escalar al mantenedor
- El síntoma coincide con una limitación conocida de la 1.0.3 y el rodeo no basta.
- Un intento sigue «En evaluación» tras restablecer cron, clave y cuota y usar «Evaluar de nuevo».
- Código con la letra X repetido, o comportamiento distinto del descrito en las referencias.
Incluir: versiones, configuración relevante, pasos para reproducir, pruebas hechas con su resultado, códigos ALS- y lo que se espera que ocurra. Sin datos personales ni claves.
