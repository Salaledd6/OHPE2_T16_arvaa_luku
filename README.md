# OHPE2_T16_arvaa_luku
Ohjelma, jossa käyttäjän pitää arvata ohjelman arpoma luku. Lukuarvo syötetään tekstikenttään ja tarkistus suoritetaan painiketta klikkaamalla. Tulos (väärin/oikein) kerrotaan ikkunassa alimpana olevaan label-kenttään.

Oikean arvauksen jälkeen arvotaan uusi luku ja ohjelman toiminta jatkuu.

Lisätty tekstikenttää varten importeihin ```QLineEdit``` ja tehty koodiin olio: ```self.vastaus = QLineEdit(self)```

Tekstikentän tiedon saa luettua seuraavasti:
```arvattu_luku = self.vastaus.text()```