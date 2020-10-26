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


### Laborator 2 - Arbore SI/SAU
Se foloseste un *arbore SI/SAU* pentru a se modela comportamentul unui aspirator
**nedeterminist** intr-un spatiu 1D, unde celulele pot fi fie curate, fie
murdare. Nedeterminismul consta in faptul ca atunci cand aspiratorul curata o
celula, exista 2 posibilitati:
- Celula era curata $\Rightarrow$ aceasta se poate ramane curata sau se poate
murdari
- Celula era murdara $\Rightarrow$ aceasta va fi curatat, dar se poate ca si
celula din dreapta sa fie curatata

#### Nod SAU
Reprezinta o decizie. In fiecare stare, sunt maxumum 3 actiuni posibile: `Left`,
`Right`, `Clean`. Fiii unui nod **SAU** reprezinta efectele acestor decizii,
daca ar deveni actiuni. Deci daca oricare dintre ele duce la o stare de succes
(in care toate celulele sunt cu siguranta curate), atunci si nodul poate duce
la o stare de succes.

#### Nod SI
Reprezinta o actiune in sine. Pentru actiunile de miscare (`Left`, `Right`), are
un singur fiu, noua pozitie in care ajunge aspiratorul. Pentru actiunea `Clean`,
nedeterminismul aspiratorului inseamna ca pentru a fi siguri ca acest nod duce
la o stare de succes, e nevoie ca ambele situatii care se pot obtine in urma
acestei actiuni (descrise mai sus) sa duca la succes, pentru ca nu stim care
scenariu se va intampla in cazul unei functionari a aspiratorului.

#### Plan
La final se creeaza un *plan* de actiune, un fel de algoritm care descrie
deciziile aspiratorului in functie de mediu (curatenia celulelor).
