```mermaid
 classDiagram
      Monopoli "1" --> "1" Pelilauta : Pelataan
      Monopoli "*" --> "1" Pelaaja 
      Monopoli "40" --> "1" Ruutu
      Pelaaja "1" --> "1" Pelinappula : Omistaa
      Ruutu "*" --> "1" Pelinappula : Sisältää
      
      class Monopoli{
      	aloitusruutu
      	vankila
      }
      class Pelilauta{
      }
      class Ruutu{
      	seuraava_ruutu
      	toiminto
      }
      class Pelaaja{
     	rahan_määrä
      }
      class Pelinappula{	
      }
      class Aloitusruutu{
      }
      class Vankila{
      }
      class Sattuma/yhteismaa{
        toiminto_kortti
      }
      class Asema/laitos{
      }
      class Katu{
        talojen_määrä
        hotellien_määrä
        omistaja
      }
```