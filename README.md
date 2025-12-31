# 📰 Aikalaisotsikot – Sukututkijan apuri

**Aikalaisotsikot** on yksinkertainen ja helppokäyttöinen web-sovellus, joka on suunniteltu sukututkijoiden ja historian harrastajien tarpeisiin. Sovellus hakee Kansalliskirjaston avoimesta datasta annetun päivämäärän sanomalehdet ja tarjoaa suorat linkit digitoituihin aineistoihin.

Tämä työkalu auttaa hahmottamaan **historiallista kontekstia**: mitä maailmassa ja Suomessa tapahtui juuri sinä päivänä, kun esivanhempasi syntyi, vihittiin tai kuoli?

## ✨ Ominaisuudet

* **Päivämäärähaku:** Valitse mikä tahansa päivämäärä (painopiste vuosissa 1771–1939).
* **Automaattinen haku:** Sovellus hakee kyseisen päivän suomenkieliset sanomalehdet Kansalliskirjaston `digi.kansalliskirjasto.fi` -palvelusta.
* **Suorat linkit:** Pääset yhdellä klikkauksella lukemaan alkuperäistä, digitoitua lehteä.
* **Responsiivinen:** Toimii selaimessa ja mobiililaitteilla (Streamlit-pohjainen).

## 🚀 Käyttöönotto omalla koneella

Tarvitset Pythonin asennettuna koneellesi.

1.  **Lataa tai kloonaa projekti** omalle koneellesi.
2.  **Asenna tarvittavat kirjastot** (Streamlit ja Requests):

    ```bash
    pip install -r requirements.txt
    ```

3.  **Käynnistä sovellus:**

    ```bash
    streamlit run app.py
    ```

4.  Sovellus aukeaa automaattisesti selaimeesi osoitteeseen `http://localhost:8501`.

## 📂 Tiedostorakenne

* `app.py`: Sovelluksen lähdekoodi (Python + Streamlit).
* `requirements.txt`: Lista tarvittavista ohjelmistokirjastoista.
* `README.md`: Tämä ohjetiedosto.

## 🛠 Teknologiat

* **[Streamlit](https://streamlit.io/):** Käyttöliittymä ja web-sovelluskehys.
* **Python:** Ohjelmointikieli.
* **API:** [Kansalliskirjaston avoin data (Digi)](https://digi.kansalliskirjasto.fi/opendata).

## ⚠️ Huomioitavaa aineistoista

* Sovellus hakee ensisijaisesti **suomenkielisiä sanomalehtiä**.
* **Tekijänoikeudet:** Kansalliskirjaston digitaaliset aineistot ovat vapaasti luettavissa vuoteen 1939 saakka. Sitä uudempien lehtien kohdalla saatat nähdä vain metatiedot, mutta et voi avata sivua kotikoneelta (vaatii käynnin vapaakappalekirjastossa).
* **Aukot:** Ennen vuotta 1771 sanomalehtiä ei juuri julkaistu. Sunnuntaisin ja pyhäpäivinä lehtiä ei välttämättä ilmestynyt.

## 📜 Lisenssi

Tämä koodi on tarkoitettu opetuskäyttöön ja harrastustoimintaan. Datalähde on Kansalliskirjasto.

---
*Tekijä: Sukututkija ja opettaja Juha Vuorela*
