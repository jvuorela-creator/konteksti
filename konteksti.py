import streamlit as st
import requests
from datetime import datetime

# --- 1. Sivun asetukset (TÄMÄN TÄYTYY OLLA ENSIMMÄINEN KOMENTO) ---
st.set_page_config(page_title="Aikalaisotsikot", page_icon="📰")

# --- 2. Otsikko ja johdanto ---
st.title("📰 Aikalaisotsikot")
st.write("Hae esi-isiesi elinpäivien sanomalehdet Kansalliskirjaston arkistosta.")

# --- 3. Käyttöliittymä (Päivämäärän valinta) ---
valittu_pvm = st.date_input(
    "Valitse päivämäärä",
    value=datetime(1908, 11, 21),    # Oletuspäivä
    min_value=datetime(1771, 1, 1),  # Vanhin aineisto
    max_value=datetime(1939, 12, 31) # Tekijänoikeusraja (suuntaa-antava)
)

# Muutetaan pvm API:n vaatimaan muotoon (YYYY-MM-DD) ja näytettäväksi (DD.MM.YYYY)
api_date = valittu_pvm.strftime("%Y-%m-%d")
nayta_pvm = valittu_pvm.strftime("%d.%m.%Y")

# --- 4. Haku-nappi ja logiikka ---
if st.button("Hae lehdet"):
    
    st.info(f"Haetaan lehtiä päivälle {nayta_pvm}...")
    
    # KORJATTU OSOITE: Käytetään binding-search -rajapintaa (hakee niteitä/lehtiä)
    url = "https://digi.kansalliskirjasto.fi/api/binding-search"
    
    # KORJATUT PARAMETRIT: dateStart, dateEnd, count
    params = {
        "dateStart": api_date,
        "dateEnd": api_date,
        "formats": "NEWSPAPER",
        "language": "fi", 
        "count": 20   # Haetaan max 20 tulosta
    }

    # "Valeasu" - Kerrotaan palvelimelle olevamme selain, ei robotti
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    try:
        # Tehdään pyyntö (timeout estää ikuisen jumittamisen)
        response = requests.get(url, params=params, headers=headers, timeout=15)
        response.raise_for_status() # Heittää virheen jos status ei ole 200 OK
        
        data = response.json()
        
        # Binding-search palauttaa tulokset yleensä 'rows'-listassa
        tulokset = data.get("rows", [])

        if not tulokset:
            st.warning(f"Ei löytynyt lehtiä päivämäärällä {nayta_pvm}.")
            st.write("Vinkki: Kokeile vaihtaa päivää. Sunnuntaisin ja pyhinä ei aina ilmestynyt lehtiä.")
        else:
            st.success(f"Löytyi {len(tulokset)} lehteä!")
            
            # Järjestetään tulokset nimen mukaan aakkosiin selkeyden vuoksi
            tulokset.sort(key=lambda x: x.get("bindingTitle", ""))

            for lehti in tulokset:
                # Haetaan tiedot (käsitellään mahdolliset puuttuvat kentät)
                nimi = lehti.get("bindingTitle", "Nimetön lehti")
                
                # ID voi olla joko "id" tai "bindingId" riippuen API-versiosta
                binding_id = lehti.get("id") or lehti.get("bindingId")
                
                if binding_id:
                    # Rakennetaan linkki digitoituun sivuun
                    linkki = f"https://digi.kansalliskirjasto.fi/sanomalehti/binding/{binding_id}?page=1"
                    
                    # Näytetään tulos
                    with st.expander(f"📄 {nimi}"):
                        st.write(f"**Päiväys:** {nayta_pvm}")
                        st.markdown(f"👉 **[Lue lehti tästä]({linkki})**")
                else:
                    st.error(f"Virheellinen data lehdelle: {nimi}")

    except requests.exceptions.RequestException as e:
        st.error("Yhteysvirhe rajapintaan.")
        st.write(f"Tekninen virhe: {e}")
        # Jos palvelin palautti virhekoodin (esim 404 tai 500), näytetään se
        if hasattr(e, 'response') and e.response is not None:
             st.code(e.response.text)

# --- 5. Alatunniste ---
st.markdown("---")
st.caption("Datalähde: Kansalliskirjaston avoin data (digi.kansalliskirjasto.fi)")
