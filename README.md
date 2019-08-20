# simple-crm

simple-crm -ohjelman tarkoitus on tuoda tukkuliikkeen työntekijöiden käyttöön helppokäyttöinen työkalu, jonka avulla voidaan seurata ja pitää kirjaa asiakkaiden kanssa käytävää komminikaatiota. Ohjelman ydintoiminnalluus on Facebook-sivun kaltainen asiakaskohtainen seinä, jonne asiakaspalvelija voi kirjoittaa asiakkaaseen kohdistuvia kommentteja, liittyen esimerkiksi siihen, mitä asiakaspalvelija on asiakkaan kanssa sopinut viimeiseksi tapahtuneen kontaktoinnin yhteydessä. Toinen ydintoiminnallisuus on ajastetut tehtävät, joita asiakaspalvelija voi lisätä asiakkaalle. Tällainen ajastettu tehtävä voi esimerkiksi olla asiakkaan toivoma seuraava kontaktointiajankohta. Ajastetut tehtävät näkyvät listattuna kaikille ohjelman käyttäjille. Tehtäviä voi listata viidellä eri tasolla: tänään, huomenna, viikko, kuukausi ja käsitellyt tehtävät. Ydintoiminnallisuuksien lisäksi käyttäjien on mahdollista tarkastella omaa ja muiden aktiivisuutta statistiikka toiminnallisuuden avulla.

Sovellusta voi testata [Herokussa](https://simplecrmapp.herokuapp.com/).

Herokuun on valmiiksi luotu seuraavat tunnukset, joilla voi kirjautua sisään

| Käyttäjätunnus| Salasana      | Rooli |
| ------------- |:-------------:| -----:|
| admin         | testitesti    | admin |
| basic         | testitesti    | basic |   

Lisäksi järjestelmään on tallennettu seuraavat asiakkaat:

Testiasiakas Oy Ab
Parasfirma Oyj


## Tekninen toteutus

### Frontend

Tavoite oli tehdä asiat mahdollisimman yksinkertaisesti ilman Javascriptiä tai css -tiedostoja. Siksi lähes kaikki on toteutettu Bootstrap -frameworkilla.

### Backend

Python

### Tietokanta

Lokaalisti SQLite, Herokussa PostgreSQL

**HUOMIO!!!! SOVELLUKSEN KÄYTTÖÖN SUOSITELLAAN CHROMEA TAI FIREFOXIA. MOBIILISTI SOVELLUS ON TODETTU TOIMIVAKSI SAFARILLA**


## Tietoturva

- Tunnetut ja laajasti käytössä olevat teknologiat

- Salasanat tallennetaan tietokantaan hashatussa muodossa. 

- Kirjautumisyritykset on rajoitettu kolmeen (3), jonka jälkeen tili lukkiutuu pysyvästi

- Salasanan pituusvaatimus on 10 merkkiä



## Toiminnot

### Peruskäyttäjä ja adminkäyttäjä

Autorisointi toteutetaan kahden eri käyttäjäroolin avulla. Peruskäyttäjän oikeudet ovat suppeammat kuin adminkäyttäjän. Molemmat käyttäjät voivat:

- Kirjautua käyttäjätunnuksella ja salasanalla

- Kirjautunut käyttäjä voi lisätä asiakastilin, tarkastella asiakastiliä ja päivittää asiakkaan tietoja.

- Käyttäjä voi hakea asiakkaaseen liittyvän asiakassivun hakutoiminnolla

- Käyttäjä voi kirjoittaa kommentteja asiakassivulle, tarkastella kommentteja sekä päivittää ja poistaa omia kommentteja

- Käyttäjä voi lisätä, tarkastella sekä suorittaa asiakkaaseen liittyviä ajastettuja tehtäviä

- Käyttäjä voi tarkastella sovelluksen käyttöön liittyvää, yhteenvetokyselyillä luotavaa statistiikkaa

### Adminkäyttäjä

- Voi lisätä sovellukseen uusia käyttäjiä ja määritellä uusien käyttäjien käyttäjätasot

- Mahdollisuus inaktivoida ja aktivoida käyttäjätili (esimerkiksi tapauksessa, jossa työntekijä vaihtaa työpaikkaa)

- Uuden salasanan asettaminen käyttäjälle + lukittuneen tilin avaaminen



## Asennusohjeet // sovelluksen suorittaminen lokaalisti

Vaatimukset: Python (v. 3.5 tai uudempi) ja SQLite

- kloonaa projekti GitHubista ZIP-pakettina linkistä `Clone or download -> Download ZIP`
- pura .zip
- luo virtuaaliympäristö sovelluksen juurikansiion komennolla `python3 -m venv venv`
- aktivoi virtuaaliympäristö komennolla `source venv/bin/activate`
- lataa sovelluksen riippuvuudet suorittamalla komento `pip install -r requirements.txt`
- kaikki on valmista - voit suorittaa ohjelman komennolla `python run.py`
- ohjelmaa voi käyttää selaimella osoitteessa `localhost:5000`
- ohjelman suorituksen voi lopettaa näppäinyhdistelmällä `ctrl+c` (terminaalissa)

**HUOM!**

jos suoritat sovellusta lokaalisti customer.html -tiedostoon pitää tehdä seuraava muutos

korvaa koodi

    <p class="card-text">
    <small class="text-muted"> {{ c.commentator }} <br> 
    {{ c.date_created.strftime('%d.%m.%Y klo %H:%M:%S') }}</small>
    </p> 

koodilla

    <p class="card-text">
    <small class="text-muted"> {{ c.commentator }} <br>
    {{ datetime.strptime(c.date_created, '%Y-%m-%d %H:%M:%S').strftime('%d.%m.%Y klo %H:%M:%S') }}</small>
    </p> 



## Linkkejä

[Käyttöohje](https://github.com/juusotaneli/simple-crm/blob/master/documentation/k%C3%A4ytt%C3%B6ohje.md)

[Heroku](https://simplecrmapp.herokuapp.com/)




