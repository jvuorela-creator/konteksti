class AgraariAnalysaattori:
    def __init__(self):
        # Tietokanta: Vuosi -> {Sää, Sato, Sosiaalinen vaikutus}
        # Lähteet: Historiallinen maataloustilasto, Ilmatieteen laitos, historiankirjoitus
        self.historia_data = {
            1862: {"sää": "Viileä kesä.", "sato": "Huono sato Pohjois- ja Itä-Suomessa.", "vaikutus": "Paikallista nälänhätää, velkaantumista."},
            1866: {"sää": "Erittäin sateinen kesä, peruna mätäni peltoon.", "sato": "Katovuosi.", "vaikutus": "Talven varastot jäivät tyhjiksi. Nälänhädän alkusoitto."},
            1867: {"sää": "Kylmin tunnettu vuosi. Jäät lähtivät kesäkuussa. Syyskuun 3. päivän halla tuhosi viljan.", "sato": "Täydellinen kato koko maassa.", "vaikutus": "Suuret nälkävuodet. Kerjuulaumat liikkeellä, pilkkukuume levisi. 8% väestöstä kuoli."},
            1868: {"sää": "Lämmin kesä.", "sato": "Sato onnistui vihdoin.", "vaikutus": "Väestö alkoi toipua, mutta taudit tappoivat yhä heikkokuntoisia keväällä."},
            1892: {"sää": "Kylmä ja sateinen syksy.", "sato": "Ruis- ja perunasato epäonnistui.", "vaikutus": "Viimeinen rauhanajan nälkäkriisi. Kruunu jakoi hätäapua."},
            1899: {"sää": "Kuiva kesä.", "sato": "Heinäsato heikko.", "vaikutus": "Karjaa jouduttiin teurastamaan rehun puutteessa."},
            1902: {"sää": "Kylmä kevät, sateinen kesä.", "sato": "Paha katovuosi ( ns. 'pasuunavuosi').", "vaikutus": "Laukaisi valtavan siirtolaisallon Amerikkaan. Maaseudun köyhälistö ahdingossa."},
            1917: {"sää": "Kohtalainen sää.", "sato": "Sato keskinkertainen, mutta tuonti katkesi.", "vaikutus": "Maailmansota ja Venäjän sekasorto estivät viljan tuonnin. Elintarvikepula johti levottomuuksiin ja lakkoihin."},
            1918: {"sää": "Kevät myöhässä.", "sato": "Kylvöt viivästyivät sodan takia.", "vaikutus": "Sisällissota esti maataloustyöt monin paikoin. Espanjantauti iski syksyllä aliravittuun kansaan."},
            1928: {"sää": "Sateinen syksy, vaikea korjuusää.", "sato": "Kato, vilja heikkolaatuista.", "vaikutus": "Johti maatalousvaltaisen talouden taantumaan jo ennen 1930-luvun suurta lamaa. Pakkohuutokaupat yleistyivät."}
        }

    def analysoi_tapahtuma(self, vuosi, tapahtuma_tyyppi="kuolema"):
        print(f"--- ANALYYSI VUODELTA {vuosi} ({tapahtuma_tyyppi.upper()}) ---")
        
        # 1. Tarkistetaan kyseinen vuosi
        if vuosi in self.historia_data:
            data = self.historia_data[vuosi]
            print(f"🌡️ SÄÄOLOSUHTEET: {data['sää']}")
            print(f"🌾 SADON LAATU: {data['sato']}")
            print(f"📉 YHTEISKUNNALLINEN VAIKUTUS: {data['vaikutus']}")
        else:
            print(f"Ei merkittävää valtakunnallista katastrofia vuonna {vuosi}. Elämä oli todennäköisesti normaalia agraariarkea.")

        # 2. Tarkistetaan EDELLINEN vuosi (erityisen tärkeä kuolemantapauksissa kevättalvella)
        prev_year = vuosi - 1
        if prev_year in self.historia_data:
            print(f"\n⚠️ HUOMIOITAVAA EDELLISELTÄ VUODELTA ({prev_year}):")
            print(f"Edellisen vuoden sato ({self.historia_data[prev_year]['sato']}) vaikutti suoraan tämän vuoden ruokavarantoihin.")
            if "nälkä" in self.historia_data[prev_year]['vaikutus'] or "Kato" in self.historia_data[prev_year]['sato']:
                print("-> MAHDOLLINEN KUOLINSYY-KONTEKSTI: Aliravitsemus tai sen heikentämä vastustuskyky taudeille.")

        print("-" * 60)

# --- SIMULAATIO ---
# Kuvitellaan tilanne: Sukututkija tutkii henkilöä, joka kuoli keväällä 1868.
app = AgraariAnalysaattori()
app.analysoi_tapahtuma(1868, "kuolema")

# Kuvitellaan tilanne: Perhe muutti Amerikkaan 1903.
print("\n")
app.analysoi_tapahtuma(1902, "muutto")
