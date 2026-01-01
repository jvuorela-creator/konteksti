import streamlit as st
import requests
from datetime import datetime

# --- 1. Sivun asetukset ---
st.set_page_config(page_title="Aikalaisotsikot", page_icon="📰")

# --- 2. Otsikko ---
st.title("📰 Aikalaisotsikot")
st.write("Hae esi-isiesi elinpäivien sanomalehdet Kansalliskirjaston arkistosta.")

# --- 3. Päivämäärän valinta ---
valittu_pvm = st.date_input(
    "Valitse päivämäärä",
    value=datetime(1908, 11, 21),    
    min_value=datetime(1771, 1, 1),  
    max_value=datetime(1939, 12, 31) 
)

# API vaatii päivämäärät muodossa YYYY-MM-DD
api_date = valittu_pvm.strftime("%Y-%m-%d")
nayta_pvm = valittu_pvm.strftime("%d.%m.%Y")

# --- 4. Haku (POST-metodilla) ---
if st.button("Hae lehdet"):
    
    st.info(f"Haetaan lehtiä päivälle {nayta_pvm}...")
    
    # Tämä on se virallinen hakurajapinta
    url = "https://digi.kansalliskirjasto.fi/api/search"
    
    # Määritellään "payload" eli data, joka lähetetään POST-paketissa
    payload = {
        "formats": ["NEWSPAPER"],
        "startDate": api_date,
        "endDate": api_date,
        "language": "fi",
        "limit": 20,
        "orderBy": "RELEVANCE"
    }

    # "Valeasu" (User-Agent) on edelleen tärkeä
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Content-Type": "application/json"
    }

    try:
        # TÄRKEÄ MUUTOS: Käytetään requests.post() eikä requests.get()
        # Lähetetään data 'json'-parametrissa
        response = requests.post(url, json=payload, headers=headers, timeout=15)
        response.raise_for_status() 
        
        data = response.json()
        tulokset = data.get("rows", [])

        if not tulokset:
            st.warning(f"Ei löytynyt lehtiä päivämäärällä {nayta_pvm}.")
            st.write("Vinkki: Kokeile vaihtaa päivää. Sunnuntaisin ja pyhinä ei aina ilmestynyt lehtiä.")
        else:
            st.success(f"Löytyi {len(tulokset)} lehteä!")
            
            # Lajitellaan aakkosiin
            tulokset.sort(key=lambda x: x.get("bindingTitle", ""))

            for lehti in tulokset:
                nimi = lehti.get("bindingTitle", "Nimetön lehti")
                # Varmistetaan ID:n löytyminen
                binding_id = lehti.get("id") or lehti.get("bindingId")
                
                if binding_id:
                    linkki = f"https://digi.kansalliskirjasto.fi/sanomalehti/binding/{binding_id}?page=1"
                    
                    with st.expander(f"📄 {nimi}"):
                        st.write(f"**Päiväys:** {nayta_pvm}")
                        st.markdown(f"👉 **[Lue lehti tästä]({linkki})**")

    except requests.exceptions.RequestException as e:
        st.error("Yhteysvirhe rajapintaan.")
        # Jos virhe on palvelimen päässä, näytetään tarkempi syy
        if hasattr(e, 'response') and e.response is not None:
             st.code(f"Virhekoodi: {e.response.status_code}\n{e.response.text}")
        else:
             st.write(f"Virhe: {e}")

# --- 5. Alatunniste ---
st.markdown("---")
st.caption("Datalähde: Kansalliskirjaston avoin data")
