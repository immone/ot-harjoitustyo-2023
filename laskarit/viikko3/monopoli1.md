```mermaid
 classDiagram
      Monopoli "1" --> "1" Pelilauta
      Monopoli "2..8" --> "1" Pelaaja
      Monopoli "40" --> "1" Ruutu
      Pelaaja "1" --> "1" Pelinappula
      Pelinappula "1" --> "*" Ruutu
      class Monopoli{
      }
      class Pelilauta{
      }
      class Ruutu{
      	seuraava_ruutu
      }
      class Pelaaja{
      }
      class Pelinappula{	
      }
```