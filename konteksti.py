import streamlit as st
import requests
from datetime import datetime

# --- ASETUKSET ---
st.set_page_config(page_title="Aikalaisotsikot", page_icon="📰")

st.title("📰 Aikalaisotsikot")
st.write("Hae esi-isiesi elinpäivien sanomalehdet.")

# --- KÄYTTÖLIITTYMÄ ---
col1, col2 = st.columns(2)
with col1:
    valittu_pvm = st.date_input(
        "Valitse päivämäärä",
        value=datetime(1908, 11, 21),
        min_value=datetime(1771, 1, 1),
        max_value=datetime(1939, 12, 31)
    )

api_date = valittu_pvm.strftime("%Y-%m-%d")
nayta_pvm = valittu_pvm.strftime("%d.%m.%Y")

# --- HAKULOGIIKKA ---
if st.button("Hae lehdet"):
    
    st.divider()
    
    # 1. Luodaan "varma linkki" suoraan verkkosivulle (tämä toimii aina)
    web_link = f"https://digi.kansalliskirjasto.fi/search?formats=NEWSPAPER&startDate={api_date}&endDate={api_date}&orderBy=RELEVANCE"
    
    st.info(f"Päivämäärä: {nayta_pvm}")
    
    # Näytetään iso nappi, josta pääsee aina perille
    st.link_button(f"↗️ Avaa {nayta_pvm} lehdet Kansalliskirjaston sivulla", web_link)
    
    st.write("---")
    st.caption("Sovellus yrittää ladata esikatselua alle...")

    # 2. Yritetään ladata esikatselu API:n kautta
    try:
        # Käytetään yksinkertaisinta mahdollista GET-hakua
        url = "https://digi.kansalliskirjasto.fi/api/search"
        
        params = {
            "queryString": "*",  # Hakee kaikkea
            "startDate": api_date,
            "endDate": api_date,
            "formats": "NEWSPAPER",
            "limit": 10
        }
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        with st.spinner("Yhdistetään arkistoon..."):
            response = requests.get(url, params=params, headers=headers, timeout=5)
            response.raise_for_status()
            data = response.json()
            tulokset = data.get("rows", [])

        if not tulokset:
            st.warning("Rajapinta ei palauttanut tuloksia, mutta yllä oleva linkki voi silti toimia.")
        else:
            st.success(f"Esikatselu onnistui! ({len(tulokset)} lehteä)")
            for lehti in tulokset:
                nimi = lehti.get("bindingTitle", "Nimetön")
                binding_id = lehti.get("id") or lehti.get("bindingId")
                
                if binding_id:
                    linkki = f"https://digi.kansalliskirjasto.fi/sanomalehti/binding/{binding_id}?page=1"
                    st.markdown(f"**[{nimi}]({linkki})**")

    except Exception as e:
        # Tässä on "Plan B" - jos API ei toimi, ei kaadeta ohjelmaa
        st.warning("⚠️ Suora yhteys rajapintaan estettiin (Kansalliskirjaston palomuuri).")
        st.write("Tämä on yleistä pilvipalveluissa. **Ei hätää – käytä yllä olevaa painiketta.** Se toimii aina.")
        # Piilotetaan tekninen virhe "expanderin" sisään, ettei se säikäytä käyttäjää
        with st.expander("Näytä tekniset tiedot"):
            st.write(f"Virhe: {e}")

st.markdown("---")
st.caption("Datalähde: Kansalliskirjasto")
