import streamlit as st
import requests
from datetime import datetime

# --- Sivun asetukset ---
st.set_page_config(page_title="Aikalaisotsikot", page_icon="📰")

st.title("📰 Aikalaisotsikot - Sukututkijan apuri")
st.write("Syötä päivämäärä, niin haemme Kansalliskirjaston digiarkistosta tuon päivän sanomalehdet.")

# --- Käyttöliittymä (Input) ---
# Käytetään Streamlitin kalenterivalitsinta, on helpompi kuin tekstisyöte
valittu_pvm = st.date_input(
    "Valitse päivämäärä",
    value=datetime(1908, 11, 21), # Oletuspäivä
    min_value=datetime(1771, 1, 1), # Ensimmäiset sanomalehdet
    max_value=datetime(1939, 12, 31) # Tekijänoikeusraja (suuntaa-antava)
)

# Muutetaan pvm API:n vaatimaan muotoon (YYYY-MM-DD)
api_date = valittu_pvm.strftime("%Y-%m-%d")
nayta_pvm = valittu_pvm.strftime("%d.%m.%Y")

# --- Haku-nappi ja logiikka ---
if st.button("Hae lehdet"):
    
    st.info(f"Haetaan lehtiä päivälle {nayta_pvm}...")
    
    # Kansalliskirjaston API
    url = "https://digi.kansalliskirjasto.fi/api/search"
    
    params = {
        "startDate": api_date,
        "endDate": api_date,
        "formats": "NEWSPAPER",
        "language": "fi", 
        "limit": 10, # Näytetään max 10 tulosta
        "orderBy": "RELEVANCE"
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        tulokset = data.get("rows", [])

        if not tulokset:
            st.warning("Ei löytynyt lehtiä tälle päivälle. Kokeile toista päivää tai tarkista onko päivä sunnuntai/pyhä.")
        else:
            st.success(f"Löytyi {len(tulokset)} lehteä!")
            
            # Käydään tulokset läpi ja tehdään niistä kivat kortit
            for lehti in tulokset:
                nimi = lehti.get("bindingTitle", "Tuntematon lehti")
                binding_id = lehti.get("bindingId")
                # Linkki suoraan sivuun 1
                linkki = f"https://digi.kansalliskirjasto.fi/sanomalehti/binding/{binding_id}?page=1"
                
                # Näytetään tulos "expander"-elementtinä tai korttina
                with st.expander(f"📄 {nimi}"):
                    st.write(f"**Julkaistu:** {nayta_pvm}")
                    st.markdown(f"[Lue lehti digi.kansalliskirjasto.fi -palvelussa]({linkki})")
                    # Jos haluaisit hifistellä, tähän voisi hakea jopa pienen esikatselukuvan, 
                    # mutta se vaatisi yhden API-kutsun lisää.

    except requests.exceptions.RequestException as e:
        st.error(f"Yhteysvirhe rajapintaan: {e}")

# --- Alatunniste ---
st.markdown("---")
st.caption("Datalähde: Kansalliskirjaston avoin data (digi.kansalliskirjasto.fi)")
