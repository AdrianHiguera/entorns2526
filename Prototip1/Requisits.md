# Requisits TapatApp
## Descripcio del Projecte
Les cataractes són la causa més freqüent de ceguesa tractable en la infància i es podria fer una estimació de 200.000 nens cecs per cataracta al món.

L'ull amb cataracta congènita, un cop operat, ha de seguir un exhaustiu règim de rehabilitació per evitar l'ambliopia, el que coneixem comunament com "ull gandul", i aquí és on pretén ajudar TapatApp! 

A part del tractament amb lents de contacte d’alta graduació i, posteriorment, lents intraoculars, el tractament més eficaç possible en aquesta patologia consisteix en l’aplicació d’un pedaç (parche) a l’ull dominant, fent que l’ull operat es vegi forçat a desenvolupar-se el màxim possible. El repte en aquest sentit, és aconseguir que l’aplicació d’aquest tractament sigui el més equilibrada possible, per aconseguir el màxim desenvolupament d’aquest ull operat, sense penalitzar el de l’ull dominant, que també ha «d’aprendre a veure» en el que s’anomena l’etapa plàstica del cervell, que finalitza entre els 6-8 anys.

Durant aquesta etapa, el tractament amb pedaç varia en funció de l’edat de l’infant, començant per aplicar-lo la meitat del temps que estigui despert en els primers mesos de vida, i continuant amb un temps fix diari que estableix l’oftalmòleg. La dificultat real d’aquesta gestió rau en controlar el nombre de minuts que porta o li queda per portar al nen aquest pedaç, ja que el seu son acostuma a ser variable i molt freqüent durant al dia. Moltes famílies manifesten la dificultat de controlar això per les freqüents migdiades que fan els petits, i per la incertesa de quan s’adormiran en el que queda de dia.

L’objectiu de TapatApp consisteix en proporcionar a totes les famílies afectades per cataracta congènita, o qualsevol patologia que faci servir pedaç ocular, una eina senzilla i gratuïta que els ajudi a portar aquest tractament de la forma més equilibrada possible i, com a conseqüència, obtenir el màxim desenvolupament d’agudesa visual.

## Objectiu del Projecte
· Control del temps del pegat de l'infant

· Control del tractament de la 1/2 del temps que l'infant està despert.

· Control del tractament d'un temps fix que l'infant està despert.

· Compartir informació del tractament amb el servei mèdic

· Accés restringit per tipus d'usuari al control del pegat. App Multiusuari.

· Desenvolupar una App Móbil.

<h2>Actors de la Aplicació</h2>

<ul>
  <li>Administrador: gestiona usuaris i paràmetres generals de l’aplicació.</li>
  <li>Servei mèdic (oftalmòlegs): consulta les dades del tractament dels pacients.</li>
  <li>Tutors (mares/pares): controlen el tractament i poden afegir cuidadors.</li>
  <li>Cuidadors (mestres, avis, cangurs…): actualitzen l’estat del pegat mentre tenen l’infant.</li>
  <li>Infant: usuari indirecte que rep el tractament.</li>
  <li>Part pública: accés informatiu o de registre inicial.</li>
</ul>

<ol>
  <li>Administrador: gestiona usuaris i paràmetres generals de l’aplicació.</li>
  <li>Servei mèdic (oftalmòlegs): consulta les dades del tractament dels pacients.</li>
  <li>Tutors (mares/pares): controlen el tractament i poden afegir cuidadors.</li>
  <li>Cuidadors (mestres, avis, cangurs…): actualitzen l’estat del pegat mentre tenen l’infant.</li>
  <li>Infant: usuari indirecte que rep el tractament.</li>
  <li>Part pública: accés informatiu o de registre inicial.</li>
</ol>


## Requisits funcionals RF i Requisits de Funcionals

## RF

<div class="alert alert-info">
  <h4>RF1: Registre d’usuari</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder registrar-me amb correu electrònic, nom i contrasenya per poder accedir a l’aplicació i gestionar el tractament del meu fill.</p>
</div>

<div class="alert alert-info">
  <h4>RF2: Inici de sessió</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder iniciar sessió de forma segura amb les meves credencials per accedir a les dades del meu infant.</p>
</div>

<div class="alert alert-info">
  <h4>RF3: Alta de l’infant</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder donar d’alta el meu fill o filla dins de l’aplicació per fer el seguiment del seu tractament amb pegat.</p>
</div>

<div class="alert alert-info">
  <h4>RF4: Control del pegat</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder controlar les hores que el nen porta el pegat mentre està despert, per saber quant de temps li queda de tractament cada dia.</p>
</div>

<div class="alert alert-info">
  <h4>RF5: Configuració del tractament</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder indicar si el tractament és de temps fix o la meitat del temps despert, per tal que l’aplicació faci els càlculs automàticament.</p>
</div>

<div class="alert alert-info">
  <h4>RF6: Gestió de cuidadors</h4>
  <h5>Rol: Tutor</h5>
  <p>Com a tutor/a vull poder afegir o eliminar cuidadors perquè també puguin controlar el temps del pegat quan ells estiguin amb l’infant.</p>
</div>

<div class="alert alert-info">
  <h4>RF7: Control del pegat pels cuidadors</h4>
  <h5>Rol: Cuidador</h5>
  <p>Com a cuidador/a vull poder marcar quantes hores porta el nen amb el pegat i veure l’estat del tractament per seguir correctament la pauta mèdica.</p>
</div>

<div class="alert alert-info">
  <h4>RF8: Consulta mèdica</h4>
  <h5>Rol: Servei mèdic</h5>
  <p>Com a metge o metgessa vull poder consultar les hores totals de tractament registrades a l’aplicació per avaluar el progrés de cada pacient.</p>
</div>

## RNF