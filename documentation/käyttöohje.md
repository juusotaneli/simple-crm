# Käyttöohje

## 1. Sisäänkirjautuminen

Sisäänkirjautuminen tapahtuu käyttäjätunnus-salasana yhdistelmällä. Kirjautumisen jälkeen käyttäjä päätyy sovelluksen etusivulle, jossa näkyvät päivän tehtävät. Käyttäjä voi tarkastella myös kuluvalle viikolle sekä kuukaudelle ajastettuja tehtäviä.
Lisäksi käyttäjällä on pääsy tehtävä historiaan.

## 2. Uuden asiakkaan lisääminen järjestelmään

Uusi asiakas lisätään sovellukseen navikointipalkin kohdasta "Lisää uusi asiakas". Asiakkaan lisäämiseksi vaaditaan asiakkaan nimi ja asiakastunnus. Muut tiedot reitti, yhteyshenkilö, puhelinnumero sekä sähköpostiosoite ovat vapaaehtoisia kenttiä.

Asiakas tallennetaan järjestelmään painamalla nappua "Lisää uusi asiakas".

Jos asiakkaan nimellä tai asiakastunnuksella ei ole aiemmin tallennettu asiakasta, asiakas lisätään järjestelmään. Muussa tapauksessa järjestelmä ilmoittaa virheestä.

## 3. Asiakkaan hakeminen

Asiakkaan voi etsiä kirjoittamalla asiakkaan nimi tai sen osa hakukenttään. Jos haettu merkkijono ei vastaa täydellisesti jonkun asiakkaan nimeä tai asiakasnumeroa, palauttaa hakutoiminto enintään 10 ensimmäistä hakuosumaa.

**Esimerkki:**
```
Oletetaan asiakas, jonka nimi on Testi. Kun käyttäjä hakee kirjainyhdistelmällä 'tes', 
hänelle palautetaan näkymänä lista, joka sisältää 10 ensimmäistä asiakasta, 
joiden nimessä on kirjainyhdistelmä 'tes'. Jos käyttäjä hakee kirjainyhdistelmällä 'testi', 
ohjataan hänet suoraan asiakassivulle.

```

## 4. Asiakkaan sivu

Asiakkaan sivulla näkyvät asiakkaan tiedot, asiakkaaseen liittyvät kommentit ja ajastetut tehtävät.

Asiakassivulla käyttäjä voi painaa nappia "Muokkaa asiakkaan tietoja", jonka takaa käyttäjä pääsee muokkaamaan asiakkaan tietoja. Avautuvan sivun kenttiin on kopioitu valmiiksi asiakkaan sen hetkiset tiedot.

## 5. Kommenttien tarkastelu, muokkaminen ja poistaminen

Asiakkaan sivulle voi lisätä kommentin kirjoittamalla sivun vasemmassa laidassa olevaan tekstikenttään haluamansa kommentin ja painamalla 'Lisää kommentti'. Lisätty kommentti ilmestyy kommenttitekstikentän alapuolelle. Jos asiakkaalle ei ole lisättyjä kommentteja, kommenttien sijaan teksikentän alla lukee 'EI KOMMENTTEJA'. 

Käyttäjä voi muokata omia kommenttejaan painalla kommentin yhteydessä olevaa "Muokkaa kommenttia" -painiketta. Tämän jälkeen avautuu uusi näkymä, jossa käyttäjä voi muokata kommenttia tai vaihtoehtoisesti poistaa kommentin kokonaan.

## 6. Ajastettujen tehtävien lisääminen

Käyttäjä voi lisätä asiakassivun oikeassa laidassa olevasta "Lisää yhteydenottopyyntö" -otsakkeen alta löytyvästä kentästä asiakkaaeseen liittyvän ajastetun tehtävän. Alasvetovalikosta (ei toimi safarilla eikä expolorerilla) käyttäjä voi valita halutun päivämäärän. Kommenttikenttään käyttäjä voi halutessaan lisätä yhteydenottopyyntöön liittyvän kommentin - esimerkiksi "pyysi soittamaan - haluaa keskustella tuotteesta x". Jos käyttäjä yrittää ajastaa tehtävän menneiyyteen, näytetään varoitus. Vastaavasti varoitus näytetään, jos päivämäärää ei valitse tai kommenttikentän jättää tyhjäksi.

### 6.1. Ajastettujen tehtävien tarkastelu

Käyttäjä voi tarkastella järjestelmään lisättyjä ajastettuja tehtäviä painamalla navigointipalkista kohtaa "Tehtävät". Tämän jälkeen käyttäjälle aukeaa näkymä, jossa käyttäjä voi hakea tehtäviä valitsemalla 'Tänään' (kuluvalle päivälle ajastetut tehtävät ja sellaiset menneisyydessä olevat tehtävät joita ei ole vielä suoritettu), 'Huomenna' (huomiselle ajastetut tehtävät), 'Viikko' (tulevalle 7 päivälle ajastetut tehtävät), 'Kuukausi' (tehtävät seuraavan 30 päivän ajalta) tai 'Valmiit tehtävät' (käsitellyt tehtävät järjestettynä nykyhetkestä menneisyyteen). 

Tehtävien yhteydessä näkyy asiakas jolle tehtävä on lisätty, toivottu yhteydenottoajankohta sekä tehtävään mahdollisesti lisätty kommentti.

Tehtävä käsitellään painamalla 'Valitse' ja tämän jälkeen 'Merkitse tehtävä suoritetuksi'. 

## 7. Tilastojen tarkastelu

Tilastot sivulta löytyy koottuna sovelluksen käyttöön liittyvää tietoa. Käyttäjä voi tarkastella lisättyjen kommenttien sekä lisättyjen tehtävien määrää / käyttäjä.

## 8. Käyttäjätiliin liittyvät toiminnot

Käyttäjätiliin liittyvät toiminnot löytyvät navigointipalkista, jossa on 'Toiminnot' alasvetovalikko. Valikkonäkymän sisältö riippuu käyttäjän käyttäjäroolista. 

Kaikille käyttäjille alasvetovalikossa näkyy painikkeet 'Vaihda salasana' sekä 'Kirjaudu ulos'. Adminkäyttäjän on mahdollista lisätä ohjelmistoon uusia käyttäjiä sekä tarkastella käyttäjiä kontrollinäkymässä. 

### 8.1 Salasanan vaihtaminen

Salasana vaihdetaan syöttämällä vähintään 10 merkkiä pitkä salasana kahteen kertaan niille tarkoitettuihin kenttiin. Jos salasanat täsmäävät, ja ne salasana on vaatimusten mukainen, käyttäjälle asetetaan uusi salasana.

### 8.2 Uuden käyttäjän lisääminen

Adminkäyttäjä voi lisätä uuden käyttäjän painamalla 'Toiminnot' alasvetovalikon painiketta 'Lisää uusi käyttäjä'. Avautuvaan näkymään täytetään uuden käyttäjän tiedot: nimi, sukunimi, käyttäjätunnus, salasana ja käyttäjärooli. *Jokainen kenttä on pakollinen!*
Jos syötetty käyttäjätunnus on jo käytössä, käyttäjää ei tallenneta, ja tästä näytetään varoitus.

### 8.3 Uuden käyttäjän lisääminen

Adminkäyttäjä voi lisätä uuden käyttäjän painamalla 'Toiminnot' alasvetovalikon painiketta 'Lisää uusi käyttäjä'. Avautuvaan näkymään täytetään uuden käyttäjän tiedot: nimi, sukunimi, käyttäjätunnus, salasana ja käyttäjärooli. *Jokainen kenttä on pakollinen!*
Jos syötetty käyttäjätunnus on jo käytössä, käyttäjää ei tallenneta, ja tästä näytetään varoitus.

### 8.4 Käyttäjien kontrollointi

Adminkäyttäjä pääsee käyttäjätilien kontrollinäkymään painamalla 'Toiminnot' alasvetovalikon painiketta 'Käyttäjien hallinta'. Adminkäyttäjällä on mahdollisuus deaktivoida (paitsi adminkäyttäjän omaa tiliä) ja aktivoida käyttäjätili (esimerkiksi tapauksessa, jossa työntekijä vaihtaa työpaikkaa). Deaktivoidulla käyttäjätilillä ei ole mahdollista kirjautua järjestelmään. Vastaavasti käyttäjätilin voi aktivoida - tämä ominaisuus on luotu mahdollisten virheellisten deaktivointien varalle. 

Kontrollinäkymässä adminkäyttäjän on mahdollista muokata minkä tahansa käyttäjän (paitsi käyttäjän omaa) salasanaa. Jos käyttäjän x käyttäjätili on lukkiutunut, adminkäyttäjä voi poistaa lukituksen vaihtamalla käyttäjän x käyttäjätilin salasana.

### 8.5 Uloskirjautuminen

Sovelluksesta kirjaudutaan ulos painamalla 'Toiminnot' alasvetovalikon painiketta 'Kirjaudu ulos'







