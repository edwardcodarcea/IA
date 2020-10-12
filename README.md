# IA
Inteligenta Artificiala - UPB 2020-2021


## Laboratoare
### Laborator 1 - A*
Se foloseste _A*_ pentru a se gasi drumul de lungime minima intre 2 puncte
dintr-un sistem de coordonate carteziene. Nu exista costuri la trecerea dintr-o
celula in alta, iar euristicile folosite sunt distanta euclidiana si cea
Manhattan.

#### Nota
Daca se elimina `sqrt()` din distanta euclidiana, **pare** ca algoritmul se
comporta mai bine, dar asta e o pura intamplare, din moment ce fara `sqrt()`
euristica nu mai e admisibila. De fapt, explorand mai putine stari, algoritmul
ar putea ajunge la un rezultat gresit daca ar fi rulat pentru o problema mai
complexa
