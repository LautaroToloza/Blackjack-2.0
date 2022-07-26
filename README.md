<h1>El Juego del Blackjack [versión 2.0]</h1>
<h2>Enunciado y Consignas:</h2>
<p>En el presente trabajo práctico se pretende replantear la solución aplicada para el juego del Blackjack implementado en el TP1, pero adecuándose a nuevas reglas:
Al inicio del juego se debe solicitar al jugador su nombre y que indique el monto que desea tener de pozo para poder jugar al Blackjack, no pudiendo ser este monto mayor a $100000. Y luego se pide implementar un programa controlado por menú de opciones en el que las opciones sean:</p>
<p>1.Apostar</p>
<p>2.Jugar una Mano</p>
<p>3.Salir</p>
<p>El jugador recibe dos cartas inicialmente y a partir de ese momento puede seguir pidiendo cartas hasta que decida frenar o bien logre 21 o se pase.
El valor del AS no es fijo. Cuando el jugador o el crupier lo recibe puede sumar 11 mientras no pase de 21. Si siguiera pidiendo cartas y se pasara, el valor del AS vuelve a 1.
El crupier inicialmente recibe una carta que se muestra junto con las dos primeras cartas del jugador. Su juego continúa cuando el jugador termina. Debe pedir cartas mientras tenga 16 o menos de puntaje y plantarse con 17 o más, siendo indefinida la cantidad de cartas hasta lograrlo.
El blackjack natural le gana a un blackjack conseguido con 3 cartas o más.
El ganador de la partida es quien logra 21 o el valor más próximo sin pasarse. Las posibles opciones son:
Gana el jugador: Recibe el doble de su apuesta. (si tenía 10 y apostó 5, queda con 15).
Pierde el jugador: En esta ocasión no pueden perder ambos. Si el jugador pierde y el crupier también, gana el crupier. (si tenía 10 y apostó 5, queda con 5).
Empatan: Si tanto el jugador como el crupier obtienen el mismo puntaje (21 o menos) entonces el jugador recibe su apuesta. (si tenía 10 y apostó 5, queda con 10).
En cada mano se debe mostrar:
Monto inicial del pozo (previo a la apuesta).
Monto de la apuesta.
Cartas de cada jugador y su puntaje final.
Mensaje indicando quién es el ganador.
Monto actualizado del pozo.</p>
<p>Salir: Cuando el usuario elige esta opción se debe mostrar su pozo actualizado y los siguientes resultados:</p>

<p>1.El porcentaje de victorias del jugador.</p>
<p>2.La racha más larga de victorias del croupier.</p>
<p>3.La cantidad de manos donde hubo un blackjack natural.</p>
<p>4.El monto máximo que llegó a tener el jugador en el pozo.</p>
<p>5.El monto promedio del que dispuso el jugador para realizar apuestas.</p>
<p>6.La pérdida más grande que sufrió el jugador (si hubo alguna).</p>
