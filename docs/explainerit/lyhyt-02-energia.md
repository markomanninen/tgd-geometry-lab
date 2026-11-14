# Energian säilyminen 16 sekunnissa

Tämä 16 sekunnin video näyttää, miksi energia ja muut symmetrioiden säilyvät suureet ovat TGD:ssä määriteltyjä, vaikka ne yleisessä suhteellisuusteoriassa menettävät määritelmänsä. Videon kuvat on laskettu tarkoista malleista, ja tarkistuslaskut ovat repon kansiossa [`scripts/lyhytvideot/energia`](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/lyhytvideot/energia). Sen jälkeen jokainen videon osa selitetään erikseen samalla tavalla kuin edellisessä videossa. Lukijaksi on ajateltu videon katsoja, joka osaa lukion pitkän matematiikan.

<div class="video">
<iframe src="https://www.youtube-nocookie.com/embed/MrGgK4D4Nf0" title="Energian säilyminen 16 sekunnissa" loading="lazy" allow="encrypted-media; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## 1. Killing-vektori ja säilyvä virta

Videon aika on 0–2,4 sekuntia.

Einsteinin teoriassa ja sen laakeassa erikoistapauksessa energia säilyy silloin, kun ajan siirto ei muuta aika-avaruuden metriikkaa. Tämän ehdon täsmällinen muoto on Killing-yhtälö, ja videon ensimmäiset sekunnit näyttävät sen yhdessä pisteessä.

### Mitä kuva näyttää

Kuvassa aika kulkee ylöspäin ja kaksi vaakasuuntaa ovat paikan suuntia. Vasemman alakulman akselit t, x ja y näyttävät nämä suunnat koko videon ajan. Kuvan tapahtumien joukko on piirretty hilaksi, eli säännölliseksi pisteiden ruudukoksi, ja lähikuva näyttää sen yhden pisteen. Hilassa on kaksi pisteriviä peräkkäin syvyyssuunnassa, ja kumpikin rivi on piirretty himmeäksi tasoksi. Tummansiniset pystytasot yhdistävät rivit laatikoksi, ja vaaleat vaakasuorat tasot ovat aikaviipaleita, eli koko avaruus yhtenä hetkenä. Kameraa lähempänä oleva kartio on kirkkaampi ja kauempana oleva himmeämpi, ja jokaisella kartiolla on läpikuultava pinta, joka peittää osittain sen takana olevat kartiot. Näin rivit erottuvat toisistaan.

Pisteessä on valokartio. Valokartio on kaksoiskartio, jonka pintaa pitkin valo kulkee pisteeseen ja pisteestä pois. Kartion leveys kertoo, kuinka pitkän matkan valo kulkee yhdessä aikayksikössä, ja videossa aika ja matka mitataan yksiköissä, joissa valon nopeus on c = 1.

Tapahtumassa välähtää valo. Valkoinen valorintama tulee kartion alaosan pintaa pitkin tapahtumaan ja lähtee siitä yläosan pintaa pitkin ulos. Rintaman säde kasvaa yhtä paljon kuin sen korkeus, ja tämä suhde on valon nopeus c = 1.

Sen jälkeen meripihkainen nuoli kasvaa tapahtumasta ylöspäin kartion sisään, ja kartion yläosa hehkuu hetken nuolen värissä. Nimiö Killing-vektori on lähikuvassa kartion alla, ja kun hila avautuu, nimiöstä lähtee neljä viivaa hilan nuoliin. Nuoli on vektori ξ, jonka komponentit ovat (1, 0, 0, 0). Ensimmäinen komponentti on ajan suunta ja kolme muuta ovat paikan suuntia, joten ξ osoittaa suoraan ajassa eteenpäin. Kuva näyttää ajan ja kaksi paikan suuntaa, joten neljäs komponentti kuuluu kuvasta puuttuvaan kolmanteen paikan suuntaan, ja siksi se on nimiössä harmaa.

Valoa hitaamman kappaleen reitti kulkee aina kartion sisällä, joten kartion sisällä olevat suunnat ovat aikasuuntia. Ajan siirron nuoli on kartion sisällä, ja tämän siirron säilyvä suure on energia. Osan 2 paikan siirtojen nuolet ovat vaakasuoria ja kartioiden ulkopuolella, ja niiden säilyvä suure on liikemäärä.

### Killing-yhtälö

Kun jokaiseen aika-avaruuden pisteeseen piirretään oma nuoli, syntyy vektorikenttä. Ajan siirron vektorikentässä jokainen nuoli on sama ξ. Vektorikenttää kutsutaan Killing-vektoriksi, kun siirto sen nuolten suuntaan säilyttää metriikan. Metriikka on se sääntö, jolla lasketaan kaikki aikavälit ja etäisyydet. Valokartiot ovat metriikan näkyvä osa. Ne kertovat, mitkä suunnat ovat valonkaltaisia, ja neliulotteisessa aika-avaruudessa nämä suunnat määräävät metriikan yhtä yhteistä kerrointa vaille. Kuvan laakeassa tapauksessa myös tämä kerroin on joka pisteessä sama, joten kartioiden osuminen päällekkäin tarkoittaa koko metriikan säilymistä.

Killing-yhtälö on

$$\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0.$$

Indeksit μ ja ν saavat arvot 0, 1, 2 ja 3, joten yhtälö on kuusitoista yhtälöä. Merkki ∇ on kovariantti derivaatta. Se mittaa, kuinka paljon vektorikenttä muuttuu siirryttäessä pisteestä toiseen. Laakeassa aika-avaruudessa, kun koordinaatit ovat suorakulmaiset, se on tavallinen derivaatta kunkin koordinaatin suhteen. Ajan siirron komponentit ovat samat joka pisteessä, joten derivaatat ovat nollia ja yhtälö toteutuu.

### Miksi juuri Killing-vektori

Kuvan toinen kaavarivi kertoo, miksi Killing-vektori on energian kannalta ratkaiseva. Energia-liikemäärätensori T on 4 × 4 -taulukko, joka kertoo jokaisessa pisteessä, paljonko siinä on energiaa ja liikemäärää ja miten ne virtaavat. Kun T kerrotaan vektorilla ξ, tulos on vektorikenttä J, jonka komponentit ovat

$$J^\mu=\sum_\nu T^{\mu\nu}\xi_\nu.$$

Kun ξ on ajan siirto, summasta jää vain T:n aikasarake. Sen ensimmäinen komponentti on energian tiheys ja kolme muuta energian virtauksen suuntia, joten J on energian virta. Tässä videossa kirjain J tarkoittaa tätä virtaa.

Virran divergenssi mittaa, paljonko virtaa lähtee pienestä alueesta enemmän kuin sinne tulee. Se lasketaan tulon derivoimissäännöllä,

$$\nabla_\mu(T^{\mu\nu}\xi_\nu)=(\nabla_\mu T^{\mu\nu})\,\xi_\nu+T^{\mu\nu}\,\nabla_\mu\xi_\nu,$$

jossa toistuvista indekseistä summataan. Ensimmäinen termi on nolla, koska aine noudattaa paikallista säilymislakia $\nabla_\mu T^{\mu\nu}=0$. Toinen termi on summa kuudestatoista tulosta. Taulukko T on symmetrinen, eli $T^{\mu\nu}=T^{\nu\mu}$. Kun summassa vaihdetaan indeksien μ ja ν paikat, summa pysyy samana, ja siksi derivaattojen $\nabla_\mu\xi_\nu$ paikalle voi kirjoittaa niiden keskiarvon $\tfrac12(\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu)$. Tämä keskiarvo on puolet Killing-yhtälön vasemmasta puolesta. Kun ξ on Killing-vektori, toinen termi on siis nolla aineesta riippumatta, ja energian virran divergenssi on nolla. Kun ξ ei ole Killing-vektori, jokin aineen jakauma tekee toisesta termistä nollasta poikkeavan. Killing-yhtälö on näin täsmälleen se ehto, jolla virta säilyy kaikenlaisen aineen kanssa.

Divergenssitön virta antaa säilyvän kokonaisenergian, kun virtaa ei tule avaruuden reunojen takaa. Virta vie energiaa paikasta toiseen, mutta ei luo eikä hävitä sitä, joten koko avaruuden yli laskettu energia on sama jokaisena hetkenä.

### Lähikuvan avautuminen

Aikavälillä 1,45–2,4 sekuntia kamera vetäytyy kauemmas. Lähikuvan kartio osoittautuu yhdeksi hilan kartioista ja nuoli yhdeksi vektorikentän nuolista. Samalla koko hilan kartioista tehdään meripihkainen kopio, ja ajan siirto vie kopion hilan välin ylöspäin. Kopion jokainen kartio osuu siellä olevan kartion päälle, koska laakeassa aika-avaruudessa jokainen kartio on sama. Kun kopio osuu, kuva välähtää vihreänä ja kello soi, samalla tavalla kuin myöhemmin TGD-osassa. Ajan siirto säilyttää siis metriikan kaikkialla, ja osa 3 toistaa saman siirron kaarevassa aika-avaruudessa.

### Mitä kuva jättää pois

- Kuva näyttää kolme aika-avaruuden neljästä suunnasta, ajan ja kaksi paikan suuntaa.
- Hila on otos pisteistä. Killing-yhtälö koskee jokaista pistettä, myös hilan pisteiden välisiä.
- Kartiot on piirretty lyhyiksi, ja valokartio jatkuu rajatta.

## 2. Kymmenen Killing-vektoria ja kymmenen säilyvää suuretta

Videon aika on 2,4–4 sekuntia.

Laakealla aika-avaruudella, jota kutsutaan Minkowskin avaruudeksi M⁴, on kymmenen toisistaan riippumatonta Killing-vektoria. Jokainen niistä antaa oman säilyvän suureensa samalla päättelyllä, jolla ajan siirto antoi energian osassa 1.

### Mitä kuva näyttää

Ruudun oikeassa reunassa on taulukko Killing-vektoreista ja niiden säilyvistä suureista, ja sen otsikko kertoo vektorien määrän sanoin 10 symmetriaa. Jokainen Killing-vektori on yksi metriikan symmetria, eli muunnos, joka säilyttää metriikan. Koko taulukko tulee näkyviin jo lähikuvassa niin, että energian rivi on kirkas ja muut himmeitä. Hilan nuolet vaihtuvat kolme kertaa, ja nuolia vastaava taulukon rivi kirkastuu, kun muut himmenevät:
- Paikan siirrossa jokainen nuoli osoittaa samaan vaakasuuntaan ja on samanpituinen. Siirtoja on kolme, yksi kutakin paikan suuntaa kohti, ja ne antavat liikemäärän p.
- Kierrossa nuolet kiertävät ympyröitä kuvan vaakatasossa, ja nuoli on sitä pidempi, mitä kauempana piste on kierron keskeltä. Kierron akseli on kuvasta puuttuva kolmas paikan suunta, ja jokainen hetki kierretään samalla tavalla. Kiertoja on kolme, yksi kunkin paikan akselin ympäri, ja ne antavat pyörimismäärän L.
- Puskussa nuolet kallistuvat ajan ja paikan välillä. Pusku eli Lorentz-pusku siirtää jokaisen tapahtuman siihen paikkaan ja hetkeen, jossa tapahtuma näkyisi tasaisesti liikkuvalle havaitsijalle. Puskuja on kolme, yksi kutakin liikkeen suuntaa kohti, ja ne antavat suureen K.

Kuvan alalaidan nimiössä sana Killing-vektori pysyy, ja sen kaava vaihtuu nuolten mukana. Kaava näyttää kunkin Killing-vektorin komponentit järjestyksessä (t, x, y, z):

| Symmetria | Killing-vektori | Säilyvä suure |
|---|---|---|
| ajan siirto | $(1,0,0,0)$ | energia E |
| paikan siirto x-suuntaan | $(0,1,0,0)$ | liikemäärä p |
| kierto z-akselin ympäri | $(0,-y,x,0)$ | pyörimismäärä L |
| pusku x-suuntaan | $(x,t,0,0)$ | suure K |

Siirtojen komponentit ovat vakioita, joten niiden nuoli on sama joka pisteessä. Kierron ja puskun komponentit riippuvat paikasta tai ajasta, joten niiden nuolet ovat eri pisteissä erisuuntaisia ja eripituisia.

Ajan siirron kanssa vektoreita on 1 + 3 + 3 + 3 = 10. Luku tulee Killing-yhtälöstä. Kenttä määräytyy yhden pisteen arvoistaan, eli nuolen neljästä komponentista ja derivaatan $\nabla_\mu\xi_\nu$ antisymmetrisestä osasta. Derivaatta on 4 × 4 -taulukko, ja Killing-yhtälö vaatii sen symmetrisen osan olevan nolla. Antisymmetrisessä osassa on kuusi vapaata lukua. Nuolen neljä komponenttia ovat siirrot E ja p, ja antisymmetrisen osan kuusi lukua ovat kolme kiertoa ja kolme puskua. Kuva näyttää kierroista ja puskuista vain yhden kummastakin, ja taulukon merkintä ×3 kertoo, että kumpaakin on kolme. Nämä kymmenen muunnosta muodostavat yhdessä Poincarén ryhmän.

Pusku ja kierto ovat todellisia muunnoksia, jotka siirtävät tapahtumia aika-avaruudessa ja säilyttävät metriikan. Tämä erottaa ne osan 4 koordinaattien uudelleennimeämisestä, joka jättää tapahtumat paikalleen.

### Mitä suure K tarkoittaa

Energia, liikemäärä ja pyörimismäärä ovat tuttuja säilyviä suureita. Puskun suure K on vähemmän tuttu. Yhden kappaleen tapauksessa sen komponentti on

$$K_x=t\,p_x-E\,x.$$

Kun K on vakio, kappaleen paikka on $x=(t\,p_x-K_x)/E$, ja tämä kasvaa tasaisesti ajan mukana, koska $p_x$ ja E ovat vakioita. Monen kappaleen järjestelmässä E, p ja K lasketaan yhteen, ja sama yhtälö antaa energialla painotetun keskipisteen paikan. Suureen K säilyminen tarkoittaa siis, että järjestelmän energian painopiste liikkuu tasaisella nopeudella suoraa viivaa pitkin. Taulukon nimi massakeskipiste viittaa tähän painopisteeseen.

### Energia integraalina

Kolmas kaavarivi kirjoittuu jo lähikuvassa kahden muun kanssa, ja se on kokonaisenergian kaava

$$E=\int T^{\mu\nu}\xi_\nu\,\mathrm d\Sigma_\mu.$$

Kun puhe sanoo, että energia säilyy, kaavan ympärille tulee kehys. Integraali lasketaan aikaviipaleen Σ yli. Aikaviipale on koko avaruus yhtenä hetkenä, ja dΣ on sen pieni tilavuuden osa, jonka suunta on viipaleen normaali. Integraali laskee yhteen osan 1 energian virran J, joka kulkee viipaleen läpi. Osan 1 tuloksen mukaan virta on divergenssitön, joten mikä tahansa myöhempi viipale antaa saman luvun. Kun ξ korvataan toisella Killing-vektorilla, sama kaava antaa liikemäärän, pyörimismäärän tai suureen K.

Tämä vastaavuus on Emmy Noetherin ensimmäinen lause vuodelta 1918. Lauseen mukaan jokaista jatkuvaa symmetriaa vastaa säilymislaki. Jatkuva symmetria tarkoittaa muunnosta, jonka suuruuden voi valita vapaasti ja pienentää nollaan, kuten siirron matkan tai kierron kulman.

### Mitä kuva jättää pois

- Nuolten pituudet on skaalattu näkyviksi. Kierron ja puskun nuolten pituus kasvaa rajatta etäisyyden mukana.

## 3. Aine ja kadonnut siirtosymmetria

Videon aika on 4–6 sekuntia.

Yleisessä suhteellisuusteoriassa, eli Einsteinin gravitaatioteoriassa, aine kaareuttaa aika-avaruuden. Kaarevuus tarkoittaa, että mikään koordinaattien valinta ei tee metriikasta laakean aika-avaruuden metriikkaa kokonaisella alueella. Kaareva aika-avaruus muuttuu yleensä paikasta ja ajasta toiseen, ja silloin ajan siirto ei säilytä metriikkaa ja energian kokonaismäärältä puuttuu määritelmä.

### Mitä kuva näyttää

Valkoiset pisteet ovat ainetta, joka on paineetonta pölyä. Pöly pysyy kuvan koordinaateissa paikallaan, joten jokainen pölyhiukkanen nousee suoraan pystyviivaa pitkin ajassa eteenpäin.

Kartiot muuttuvat aineen tullessa. Kartion leveys riippuu nyt sekä paikasta että hetkestä. Leveys on valon nopeus kuvan koordinaateissa, eli se kertoo, kuinka paljon etäisyys keskipisteestä muuttuu kuvan ajan yksikössä valon kulkiessa. Valon nopeus c on vakio, ja leveydet eroavat siitä, koska kuvan koordinaatit seuraavat kaarevaa metriikkaa. Hilan alimman hetken punainen kopio nousee ajan siirron mukana hilan välin ylöspäin samoin kuin osan 1 meripihkainen kopio. Ylempien pisteiden kartiot ovat eri levyisiä kuin alempien, joten kopion kartiot jäävät niiden viereen. Kohdassa 6 sekuntia keskimmäisen hetken kopio nousee samoin ylimmälle hetkelle, ja sekin menee ohi. Nimiö aikasiirto ξ seuraa neljällä viivalla kulloinkin nousevaa kopiota, ja punaiset kopiot pysyvät näkyvissä TGD-osan alkuun asti. Kohdassa 5,5 sekuntia, musiikin iskussa, ajan siirron nuolet hajoavat, kartiot tärisevät, ja energian kaava, Killing-yhtälö ja symmetrioiden luku hajoavat merkeiksi. Hajoaminen kuvaa sitä, että energialta katoaa määritelmä.

Kartioiden erilaiset leveydet eivät yksin todista mitään, koska samat pisteet voi nimetä uusilla koordinaateilla, ja silloin leveydet muuttuvat. Laakeassakin aika-avaruudessa vinot koordinaatit antaisivat eri pisteiden kartioille eri leveydet. Koordinaateista riippumaton tosiasia on se, montako Killing-vektoria aika-avaruudella on. Killing-yhtälö on tensoriyhtälö, joten jos jokin vektorikenttä toteuttaa sen yhdessä koordinaatistossa, sama kenttä toteuttaa sen kaikissa. Tämän ratkaisun Killing-vektorit ovat vain kolme kiertoa, joten sillä ei ole yhtään siirtoa, joka säilyttäisi metriikan, kirjoitettiinpa siirto millä koordinaateilla tahansa.

### Ratkaisu, josta kuva on laskettu

Kartiot on laskettu Einsteinin yhtälön tarkasta ratkaisusta, joka tunnetaan Lemaîtren, Tolmanin ja Bondin pölyratkaisuna. Sen metriikka on

$$\mathrm ds^2=\mathrm dt^2-R'(r,t)^2\,\mathrm dr^2-R(r,t)^2\,\mathrm d\Omega^2,\qquad R(r,t)=r\,\bigl(t-t_B(r)\bigr)^{2/3}.$$

Tässä r on pölyhiukkasen pysyvä nimi, joka kertoo, kuinka kaukana keskipisteestä hiukkanen on alkujaan, ja R on saman hiukkasen todellinen etäisyys hetkellä t, ja pilkku tarkoittaa derivaattaa r:n suhteen. Termi dΩ² on suunnan muutoksen osuus, sama kuin pallon pinnalla. Funktio t_B(r) on hetki, jolloin pölyn laajeneminen alkaa etäisyydellä r. Kuvan ratkaisussa laajeneminen alkaa keskellä myöhemmin, joten keskellä pöly on ehtinyt laajeta vähemmän ja on tiheämpää. Projektin [tarkistuslaskut](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) vahvistavat symbolisesti, että metriikka toteuttaa Einsteinin yhtälön pölylle.

Metriikan komponentit riippuvat ajasta t. Killing-yhtälön vasen puoli voidaan kirjoittaa koordinaateissa muotoon $\xi^\lambda\partial_\lambda g_{\mu\nu}+g_{\lambda\nu}\partial_\mu\xi^\lambda+g_{\mu\lambda}\partial_\nu\xi^\lambda$. Ajan siirron komponentit ovat tässäkin koordinaatistossa vakiot (1, 0, 0, 0), joten kaksi viimeistä termiä ovat nollia ja ensimmäisestä jää vain aikaderivaatta. Ajan siirron Killing-yhtälö supistuu siis muotoon

$$\frac{\partial g_{\mu\nu}}{\partial t}=0,$$

eli metriikan komponentit eivät saa riippua ajasta. Tämän ratkaisun komponentit riippuvat, joten ajan siirto ei ole Killing-vektori.

### Taulukko ja kaavat

Taulukosta jäävät voimaan vain kierrot. Ratkaisu on pallosymmetrinen, joten keskipisteen ympäri tehty kierto säilyttää metriikan, ja pyörimismäärä säilyy edelleen. Ajan siirto, paikan siirrot ja puskut menettävät Killing-vektorin aseman, joten energia, liikemäärä ja suure K yliviivautuvat, ja luku putoaa kymmenestä kolmeen.

Kaavarivit kertovat saman. Killing-yhtälön vasen puoli ei ole nolla, joten osan 1 päättelyn toinen termi ei häviä, ja virran $T^{\mu\nu}\xi_\nu$ divergenssi poikkeaa nollasta. Energian integraalista puuttuu se Killing-vektori, jolla energia-liikemäärätensori kerrottaisiin, ja kysymysmerkki on sen paikalla.

Paikallinen säilymislaki $\nabla_\mu T^{\mu\nu}=0$ pätee edelleen jokaisessa pisteessä. Kovariantin derivaatan metriikasta tulevat termit vaihtavat kuitenkin energiaa aineen ja kaarevan aika-avaruuden välillä, joten aineen energian integraali ei pysy vakiona, eikä gravitaatiolle ole koordinaateista riippumatonta energian tiheyttä, joka korjaisi vajeen. Pitkänen muotoilee tämän Einsteinin teorian energiaongelmaksi. Kaarevassa aika-avaruudessa Poincarén ryhmän varauksia, eli energiaa, liikemäärää, pyörimismäärää ja suuretta K, ei voi määritellä säilyvinä Noetherin varauksina.

### Mitä kuva jättää pois

- Kuvan ratkaisu säilyttää kolme kiertoa, koska se on pallosymmetrinen. Aika-avaruudessa, jossa ainetta on epäsymmetrisesti, Killing-vektoreita ei ole lainkaan.
- Kartioiden leveydet ovat valon nopeuksia kuvan koordinaateissa. Vapaasti putoavan havaitsijan oma mittaus antaa valon nopeudeksi aina c.

## 4. Koordinaatit niminä

Videon aika on 6–8 sekuntia.

Kuvassa energian integraali jää ruudulle kysymysmerkin kanssa, ja keskimmäisen hetken punainen kopio nousee ylimmälle hetkelle. Kopio on perillä kohdassa 7,5 sekuntia, toisessa musiikin iskussa, ja menee ohi. Samalla kuva välähtää punaisena, kartiot tärähtävät ja integraalin kysymysmerkki paisuu.

Video ei näytä, mitä Einsteinin teoria saa kymmenen symmetrian tilalle, ja tämä osa selittää sen. Tilalle tulee toinen symmetria, koordinaattien vapaa valinta, ja siitä seuraa identiteetti eikä säilyvää kokonaisenergiaa.

### Koordinaatit ovat vain nimiä

Koordinaatit ovat Einsteinin teoriassa aika-avaruuden pisteiden nimiä. Koordinaattimuunnos antaa samoille tapahtumille uudet nimet, ja kartiot ja aine pysyvät silloin paikallaan.

Markon esseessä Through the Wormhole on Spacetime Surface uudelleennimeämistä verrataan kartan kaupunkien nimien vaihtamiseen, joka ei muuta kaupunkien paikkoja eikä niiden välisiä etäisyyksiä. Ero osan 2 puskuun on tämä. Pusku siirtää tapahtumia toisiin paikkoihin ja säilyttää metriikan, kun taas uudelleennimeäminen jättää tapahtumat paikalleen ja muuttaa vain niiden nimet. Einsteinin teoria on rakennettu niin, että sen yhtälöt ovat samat kaikilla nimeämistavoilla. Tätä kutsutaan yleiseksi koordinaatti-invarianssiksi. Esseen mukaan se on vahvan ekvivalenssiperiaatteen ilmaus, eli sen periaatteen, jonka mukaan kaikki fysiikan lait ovat vapaasti putoavassa pienessä laboratoriossa samat kuin suppeassa suhteellisuusteoriassa.

### Identiteetti eikä säilymislaki

Koordinaattien vapaasta valinnasta seuraa identiteetti. Koordinaattimuunnos valitaan neljän mielivaltaisen funktion avulla, kun taas Poincarén ryhmän muunnos valitaan kymmenellä luvulla. Noetherin toinen lause koskee funktioiden määräämiä symmetrioita, ja niistä seuraa identiteetti eikä uutta säilyvää suuretta. Einsteinin teoriassa identiteetti on

$$\nabla_\mu G^{\mu\nu}\equiv 0.$$

G on Einsteinin tensori, joka lasketaan metriikasta. Merkki ≡ kertoo, että yhtälö pätee jokaisella metriikalla, myös sellaisella, joka ei toteuta Einsteinin yhtälöä. Einsteinin yhtälö on $G^{\mu\nu}=8\pi G_N T^{\mu\nu}$, jossa $G_N$ on gravitaatiovakio. Kun yhtälön molemmilta puolilta otetaan divergenssi, identiteetti antaa paikallisen säilymislain $\nabla_\mu T^{\mu\nu}=0$. Laakeassa aika-avaruudessa sama yhtälö antoi osassa 1 kokonaisenergian, koska siellä oli Killing-vektori, jolla tensori kerrottiin. Kaarevassa aika-avaruudessa Killing-vektoria ei ole, joten yhtälöstä jää vain paikallinen laki. Noether kutsui tällaisia säilymislakeja epäaidoiksi (improper), koska ne pätevät teorian rakenteen vuoksi eivätkä anna säilyvää kokonaismäärää.

### Mitä kuva jättää pois

- Kuva ei näytä koordinaattien vapaata valintaa eikä siitä seuraavaa identiteettiä. Ne kerrotaan vain tällä sivulla.

## 5. Pinta upotusavaruudessa

Videon aika on 8–10 sekuntia.

TGD-osan alussa kamera kiihtyy ja kiertää hilan ympäri kerran kokonaan, ja samaan aikaan kartiot muuttuvat jälleen laakeiksi. Oikean reunan punainen taulukko ja kaavat katoavat kierroksen aikana. Kun pinta ilmestyy, taulukko palaa niin, että jokainen rivi on voimassa ja siihen on tullut uusi rivi, ja TGD:n kolme kaavariviä tulevat kerralla. Kierroksen aikana vasemman alakulman akselin y nimi vaihtuu CP₂:ksi, ja akselit saavat värin sen avaruuden mukaan, johon suunta kuuluu. Akselit t ja x ovat M⁴:n suuntia ja sinisiä kuten otsikon M⁴, ja CP₂:n suunta on violetti kuten taulukon värivaraus, jonka CP₂:n kahdeksan Killing-vektoria antavat.

TGD eli topologinen geometrodynamiikka erottaa toisistaan kaksi asiaa, jotka Einsteinin teoriassa ovat sama. Aika-avaruus on TGD:ssä neliulotteinen pinta X⁴ kahdeksanulotteisessa avaruudessa H = M⁴ × CP₂, jota kutsutaan upotusavaruudeksi ja jota intro merkitsee H⁸. Pinta saa kaartua, mutta symmetriat kuuluvat upotusavaruudelle, jonka M⁴:n osa on laakea ja pysyy samana.

### Mitä kuva näyttää

Hilan kartiot palaavat laakean avaruuden kartioiksi ja pysyvät sellaisina loppuun asti. Hila on nyt viipale upotusavaruudesta H. Pystysuunta on edelleen aika t ja toinen vaakasuunta paikka x, mutta kolmas suunta on yksi CP₂:n suunta. Upotusavaruuden metriikka ei riipu siitä, mitä pintoja siinä on, joten sen kartiot eivät muutu koskaan. Kuvan viipaleessa metriikka on

$$\mathrm ds^2=\mathrm dt^2-\mathrm dx^2-\mathrm ds_{CP_2}^2.$$

Ajan suunnan etumerkki on vastakkainen kuin muiden seitsemän suunnan. Etumerkkien ero erottaa ajan suunnat paikan suunnista, ja siitä seuraa, että osa suunnista on valonkaltaisia ja niiden pituus on nolla. Se, kumpi saa plusmerkin, on sopimus, ja projektissa aika saa plusmerkin.

Lasilevy on aika-avaruuspinta, ja otsikon merkinnästä X⁴ lähtee siihen viiva. Kohdasta 9,6 sekuntia kamera lähestyy levyä, ja otsikko ja viiva häviävät, jotta kuvalla on enemmän tilaa. Levyn ohuet syvänsiniset ristit ovat pinnan omia valokartioita. Ne ovat samaa väriä kuin upotusavaruuden valokartiot, ja niiden kaksi suoraa kohtaavat siinä pinnan pisteessä, johon kartio kuuluu. Video ei nimeä ristejä, ja tämän osan kohta Pinnan valokartiot kertoo, mitä ne ovat ja miten ne liittyvät gravitaatioon.

### Pinnan muoto

TGD:ssä pinnan muodon määrää vaikutus. Vaikutus on luku, joka lasketaan pinnasta, ja kenttäyhtälöt ovat ehto, että luku ei muutu, kun pintaa muutetaan vähän. Vaikutuksen tilavuusosa on pinnan neliulotteinen tilavuus kerrottuna vakiolla, ja kuvan levy toteuttaa tämän osan kenttäyhtälöt. Kaksiulotteisessa tapauksessa tällaisen pinnan voi kirjoittaa muodossa

$$X(\sigma,\tau)=\Bigl(\tau,\ \tfrac12\bigl(a(\sigma-\tau)+a(\sigma+\tau)\bigr)\Bigr).$$

Parametri τ on aika ja σ paikka pinnalla. Kirjain s on kuvan CP₂-suunnan koordinaatti, ja a on käyrä tasossa (x, s), jonka pituus kasvaa yhtä nopeasti kuin sen parametri. Tämän pituusehdon ansiosta σ ja τ ovat pinnalla koordinaatit, joissa tilavuusosan kenttäyhtälö on aaltoyhtälö, ja jokainen kahden vastakkain kulkevan aallon summa ratkaisee aaltoyhtälön. Funktio a(σ − τ) on sama muoto siirrettynä matkan τ verran, joten se kulkee pinnalla valon nopeudella yhteen suuntaan, ja a(σ + τ) kulkee vastakkaiseen suuntaan. Pinnalla kulkee siis kaksi pulssia, ja kuvan hetkellä ne ovat juuri ohittaneet toisensa. Projektin [tarkistuslaskut](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) vahvistavat numeerisesti, että pinta toteuttaa kenttäyhtälön ja että ristit ovat valonkaltaisia.

### Pinnan valokartiot

Pinnan valokartio kertoo, mihin suuntiin valo voi kulkea itse aika-avaruudessa X⁴. Se kuuluu pinnalle, kun taas hilan kartiot kuuluvat upotusavaruudelle H.

Pinnan pisteessä ne suunnat, joihin pintaa pitkin voi lähteä, muodostavat pinnan tangenttiavaruuden. Metriikka on sääntö, joka antaa jokaiselle suunnalle pituuden. Neliulotteisella pinnalla tangenttiavaruus on neliulotteinen osa upotusavaruuden kahdeksanulotteisesta tangenttiavaruudesta. Kuvan kaksiulotteisella levyllä tangenttiavaruus on tangenttitaso, eli taso, joka koskettaa levyä pisteessä. Pinnan metriikka on upotusavaruuden metriikka laskettuna vain pinnan suuntaisille vektoreille, ja sitä kutsutaan indusoiduksi metriikaksi. Gravitaatio on TGD:ssä indusoidun metriikan kaarevuutta, ja kaarevuus näkyy kuvassa siten, että pinnan kartiot vaihtelevat pisteestä toiseen.

Valo kulkee suuntiin, joiden pituus metriikassa on nolla, eli joissa kuljettu matka on yhtä suuri kuin kulunut aika. Indusoitu metriikka antaa pinnan suunnalle saman pituuden kuin upotusavaruuden metriikka. Pinnan valonsuunta on siis upotusavaruuden valonsuunta, joka on myös pinnan tangenttiavaruudessa, ja pinnan valokartio on upotusavaruuden kartion ja tangenttiavaruuden leikkaus. Kuvassa kartion kärki on levyn pisteessä, ja tangenttitaso kulkee saman pisteen kautta. Pinnan aikasuunta osoittaa kartion sisään, ja taso, joka kulkee kartion kärjen kautta ja sisältää tällaisen suunnan, leikkaa kartion pintaa kahta suoraa pitkin. Siksi pinnan valokartio näkyy ristinä, ja ristin kaksi viivaa ovat ne suunnat, joihin valo kulkee levyllä, toinen eteen ja toinen taakse.

Ristin muodon näkee kahdella tavalla. Valokartio koostuu suorista valonsäteistä, jotka kaikki kulkevat sen kärjen kautta. Kärjen kautta kulkeva taso osuu vain niihin säteisiin, jotka ovat tasossa, ja niitä on kaksi, samoin kuin jäätelötötteröstä jää kaksi suoraa reunaa, kun sen leikkaa pystysuoraan kärjen kautta. Kaksoiskartiossa säteet jatkuvat kärjen läpi, ja niistä tulee risti. Toinen tapa on ajatella maailmaa, jossa on yksi aikasuunta ja yksi paikkasuunta, kuten kuvan levyllä. Siellä valo voi kulkea vain vasemmalle tai oikealle, joten valokartio on kaksi valonsädettä, jotka kohtaavat tapahtumassa. Neliulotteisella pinnalla valokartio on jälleen kolmiulotteinen kartio, kuten hilan kartiot.

Levy ulottuu M⁴:n suuntien lisäksi myös CP₂:n suuntaan. Kun valo kulkee levyä pitkin, osa sen liikkeestä menee CP₂:n suuntaan, ja M⁴:n suunnassa x valo etenee hitaammin kuin nopeudella c = 1. Yksinkertaisin esimerkki on pinta s = f(x), joka ei muutu ajassa. Pinnan suuntaisella siirtymällä (dt, dx) on CP₂-osa ds = f′(x) dx, ja valon suunnalle pätee dt² = dx² + f′(x)² dx². Kun yhtälöstä ratkaistaan dx/dt, saadaan

$$\frac{\mathrm dx}{\mathrm dt}=\frac{1}{\sqrt{1+f'(x)^2}}.$$

Valon nopeus x-suuntaan on siis pienempi kuin 1 aina, kun pinta kallistuu CP₂:n suuntaan. Pinnan ristin viivat ovat silloin lähempänä aika-akselia kuin upotusavaruuden kartion reunat, eli pinnan kartio on kapeampi. Kaventuminen on sitä suurempi, mitä jyrkemmin pinta kallistuu. Kuvan ristit ovat siksi eri pisteissä eri asennoissa ja eri levyisiä.

Kuvan levyllä ristin viivat ovat pinnan aikasuunnan ja paikkasuunnan summa ja erotus, $X_\tau+X_\sigma$ ja $X_\tau-X_\sigma$, joissa alaindeksi tarkoittaa derivaattaa. Kohdan Pinnan muoto kaavan X(σ, τ) derivaatat ovat $X_\tau=\bigl(1,\ \tfrac12(a'(\sigma+\tau)-a'(\sigma-\tau))\bigr)$ ja $X_\sigma=\bigl(0,\ \tfrac12(a'(\sigma+\tau)+a'(\sigma-\tau))\bigr)$, ja niiden summasta ja erotuksesta saadaan

$$X_\tau\pm X_\sigma=\bigl(1,\ \pm a'(\sigma\pm\tau)\bigr).$$

Käyrän a pituus kasvaa yhtä nopeasti kuin sen parametri, joten $\lvert a'\rvert=1$. Pituuden neliö on aikaosan neliö miinus tason (x, s) osan neliö, eli kummallekin suunnalle 1 − 1 = 0. Viivat ovat siis täsmälleen valonkaltaisia, ja ristit on laskettu suoraan pinnan muodosta.

TGD:ssä on näin kaksi kartiojoukkoa yhtä aikaa:

| Kartiot | Kenelle ne kuuluvat | Miltä ne näyttävät | Mitä niistä seuraa |
|---|---|---|---|
| H:n kartiot | upotusavaruus | samanlaiset joka pisteessä | symmetriat ja säilyvä energia |
| X⁴:n kartiot | aika-avaruuspinta | vaihtelevat pisteestä toiseen | gravitaatio |

Einsteinin teoriassa kartiojoukkoja on yksi. Kun sen kartiot vaihtelevat, symmetriat katoavat, kuten osa 3 näytti. TGD:ssä gravitaatio muuttaa pinnan kartioita, mutta energia määritellään upotusavaruuden kartioiden symmetrioista, jotka pysyvät.

### Taulukko syttyy uudelleen

M⁴:n kymmenen Killing-vektoria ovat taas voimassa, koska M⁴ on upotusavaruuden osana laakea. Lisäksi CP₂:lla on kahdeksan Killing-vektoria. CP₂ on kaareva, mutta jokaisen sen pisteen ympäristö on samanlainen, ja kahdeksan toisistaan riippumatonta kiertoa säilyttää sen metriikan. Kierrot muodostavat ryhmän SU(3), ja Pitkäsen mukaan niiden varaukset ovat hiukkasfysiikan värivaraukset. Killing-vektoreita on siksi 10 + 8.

Pitkänen muotoilee ratkaisun näin. Poincarén symmetriat siirretään aika-avaruudesta upotusavaruuden osaan M⁴, ja silloin ne ovat voimassa, olipa pinta millä tavalla tahansa kaareva.

### Mitä kuva jättää pois

- Pinta on kaksiulotteinen kolmiulotteisessa viipaleessa. TGD:n pinta on neliulotteinen kahdeksanulotteisessa avaruudessa, ja kuvassa kaksi suuntaa edustaa neljää.
- Kuvan levy näyttää seinältä, joka jakaa laatikon kahtia, koska levyltä puuttuu vain yksi laatikon kolmesta ulottuvuudesta. TGD:n pinnalta puuttuu neljä upotusavaruuden kahdeksasta ulottuvuudesta, joten pinta ei jaa upotusavaruutta, ja sen ohi pääsee aina. Kaksi tällaista pintaa leikkaavat yleensä vain erillisissä pisteissä, koska 4 + 4 − 8 = 0.
- Levy päättyy kuvassa laatikon sisällä, mutta laatikko on vain ikkuna upotusavaruuteen. Pinta on kokonaan upotusavaruuden sisällä ja jatkuu ikkunan ulkopuolelle.
- CP₂:sta kuva näyttää yhden suunnan neljästä. CP₂ on suljettu avaruus, joten tuo suunta palaa itseensä, vaikka kuva piirtää sen suorana.
- Levyn muoto on laskettu pelkästä tilavuusosasta. TGD:n vaikutukseen kuuluu myös Kähler-muodosta laskettu osa.

## 6. Siirretty pinta on ratkaisu, ja energia säilyy

Videon aika on 10–16 sekuntia.

Videon loppu näyttää, miksi globaali energia, eli koko avaruuden kokonaisenergia, säilyy TGD:ssä. Kun koko aika-avaruuspintaa verrataan sen kopioon, jonka upotusavaruuden ajan siirto on vienyt ylemmäs, kopio toteuttaa samat kenttäyhtälöt kuin alkuperäinen pinta. Noetherin ensimmäinen lause antaa tästä symmetriasta virran, joka kulkee pintaa pitkin katkeamatta.

### Pinnan siirretty kopio

Meripihkaiset nuolet ovat upotusavaruuden ajan siirto, ja ne ovat samat jokaisessa hilan pisteessä. Levy pysyy paikallaan, ja siirto nostaa sen meripihkaisen kopion ylöspäin, samoin kuin osien 1 ja 3 kartioiden kopiot nousivat. Siirto on vertailu eikä liike. Kysymys on, onko siirretty kopio yhtä hyvä aika-avaruus kuin alkuperäinen. Kohdassa 11 sekuntia, musiikin iskussa, kopio on perillä, ja kuva välähtää vihreänä ja kello soi. TGD-osassa vihreitä välähdyksiä on kaksi, ja ne vastaavat osien 3 ja 4 kahta punaista iskua. Punaisissa iskuissa symmetria ja energian määritelmä katosivat. Ensimmäisessä vihreässä symmetria toteutuu, sillä siirretty pinta toteuttaa samat kenttäyhtälöt, ja toisessa, kohdassa 13 sekuntia, energian integraali on valmis ja energia säilyy. Markon esseessä Through the Wormhole on Spacetime Surface Pitkänen kuvaa tätä vertaamalla pintaa jäykkään kappaleeseen, jota siirretään ja käännetään kokonaisena.

Ero Einsteinin teoriaan on siinä, mitä siirretään. Einsteinin teoriassa siirto olisi aika-avaruuden oma muunnos, ja osan 3 mukaan sellaista ei kaarevassa aika-avaruudessa ole. TGD:ssä siirto on upotusavaruuden muunnos, joka on olemassa aina, ja se vie pinnan toiseen paikkaan upotusavaruudessa.

Pinta itse muuttaa muotoaan, koska sen pulssit liikkuvat. Vertaus jäykkään kappaleeseen koskee siirtoa. Vaikutus lasketaan indusoidusta metriikasta, ja indusoitu metriikka lasketaan upotusavaruuden metriikasta, joka on siirron jälkeen sama. Siksi vaikutus on siirretylle pinnalle sama kuin alkuperäiselle, ja siirretty pinta toteuttaa samat kenttäyhtälöt.

### Siirron osa pinnan suuntaan

Seuraavaksi kamera lähestyy vielä levyn neljää pistettä, ja kuva jakaa siirron ξ niissä kahteen osaan. Jokaisesta pisteestä lähtee kaksi nuolta, meripihkainen ξ ja vihreä J, ja niiden nimiöt aikasiirto ξ ja energian virta J tulevat näkyviin yhtä aikaa. Levyn pisteiden meripihkaiset nuolet ovat yhtä pitkiä kuin upotusavaruuden nuolet, sillä ne ovat saman kentän arvoja. Ne eivät ole pinnan oma aikasiirto vaan upotusavaruuden aikasiirto pinnan kohdalla. Pinnalla ei voi olla omaa aikasiirtoa, jonka symmetria antaisi energian, koska sen pulssit liikkuvat ja pinta näyttää eri hetkinä erilaiselta. Kopio on noussut tasan yhden nuolen pituuden verran, joten jokainen meripihkainen nuoli vie pinnan pisteen kopion vastaavaan pisteeseen. Upotusavaruuden kartiot ja nuolet himmenevät lähennyksen alkaessa, ja hilan viivat ja tasot jäävät näkyviin. Vihreä nuoli on ξ:n pinnan suuntainen osa, ja se on energian virran J suunta.

### Siirron kaksi osaa

Pinnan kohdalla ξ osoittaa yleensä vinosti pintaan nähden, joten sen voi jakaa pinnan suuntaiseen osaan ja pintaa vastaan kohtisuoraan osaan $\xi_\perp$. Vaikutuksen tilavuusosalla energian virta on tarkalleen pinnan suuntainen osa, sillä virran $J^\alpha = T^{\alpha k}\xi_k$ tensori sisältää pinnan tangenttivektorit, ja niillä kertominen poimii ξ:stä pinnan suuntaisen osan. Kohtisuora osa ei esiinny energiassa, mutta se on se kohta, jossa energian säilyminen tarvitsee kenttäyhtälöitä. Virran divergenssi on

$$
\nabla_\alpha J^\alpha = (\nabla_\alpha T^{\alpha k})\,\xi_k + T^{\alpha k}\,\nabla_\alpha \xi_k .
$$

Jälkimmäinen termi häviää, koska ξ on upotusavaruuden Killing-vektori. Ensimmäisessä termissä pinnan suuntaisen osan vaikutus häviää geometrisena identiteettinä, ja kohtisuoran osan vaikutus häviää vain silloin, kun pinta toteuttaa kenttäyhtälöt. Pinnan suuntainen siirto vain liu'uttaa pisteitä pintaa pitkin, joten se nimeää pisteet uudelleen eikä muuta pintaa. Kopion ja alkuperäisen pinnan ero syntyy siksi kokonaan kohtisuorasta osasta. Video näyttää tämän kopiona eikä erillisenä nuolena. Ensimmäinen vihreä välähdys kertoo, että kohtisuorasti siirretty kopio toteuttaa samat kenttäyhtälöt, ja toinen, että virta J kulkee katkeamatta.

Vaikutuksen tilavuusosasta laskettu virta on vakiokerrointa vaille

$$T^{\alpha k}=\sqrt{|g|}\;g^{\alpha\beta}\,\partial_\beta X^k,\qquad J^\alpha=T^{\alpha k}\xi_k.$$

Indeksi α kulkee pinnan suuntia ja indeksi k upotusavaruuden suuntia. Merkintä |g| on pinnan indusoidun metriikan determinantin itseisarvo, ja sen neliöjuuri muuttaa koordinaattien pinta-alkiot todellisiksi pinta-aloiksi. Yläindeksinen $g^{\alpha\beta}$ on indusoidun metriikan käänteismatriisi, ja $\partial_\beta X^k$ on pinnan tangenttivektori. Tulo $\partial_\beta X^k\xi_k$ on siirron ξ ja tangenttivektorin pistetulo upotusavaruuden metriikalla. Kohtisuoran osan pistetulo jokaisen tangenttivektorin kanssa on nolla, joten virta riippuu vain ξ:n pinnan suuntaisesta osasta. Pitkänen kirjoittaa saman yleisesti katsausartikkelinsa TGD2024I kaavassa 2.4, jonka mukaan säilyvä isometriavirta on verrannollinen Killing-vektorin projektioon pinnan tangenttiavaruuteen.

### Virtaviivat ja nouseva aikaviipale

Vihreät viivat ovat energian virran virtaviivoja. Ne alkavat levyn alareunasta ja päättyvät sen yläreunaan, ja jokainen kulkee koko matkan katkeamatta. Viivat on piirretty niin, että kahden vierekkäisen viivan väliin jää aina sama määrä energiaa.

Energian kaavan ympärille tulee kehys viipaleen noustessa. Vaalea vaakataso Σ on aikaviipale, eli upotusavaruuden yksi hetki, ja se on samaa väriä kuin hilan aikaviipaleet. Viipale nousee levyn läpi, ja sen nouseminen on ajan kulkua. Viipale leikkaa levyä valkoisessa käyrässä. Käyrä on pinnan avaruus sillä hetkellä, ja täydessä teoriassa se on kolmiulotteinen. Käyrän pisteet ovat virtaviivojen leikkauspisteet. Joka korkeudella leikkauspisteitä on sama määrä, ja viipaleen läpi kulkeva energia on siksi kaikilla korkeuksilla sama. Projektin [tarkistuslaskussa](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) energia on yhdeksällä viipaleella sama luku 6,8 kuvan yksiköissä. Kohdassa 13 sekuntia viipale on noussut lähes yläreunaan ja energian kaava on kirjoitettu loppuun, ja kuva välähtää toisen kerran vihreänä. Kaavana sama asia on

$$E=\int T^{\alpha k}\xi_k\,\mathrm d\Sigma_\alpha,\qquad \nabla_\alpha\bigl(T^{\alpha k}\xi_k\bigr)=0.$$

Säilymislain päättely on samanlainen kuin osassa 1. Tulon derivoimissääntö antaa

$$\nabla_\alpha\bigl(T^{\alpha k}\xi_k\bigr)=(\nabla_\alpha T^{\alpha k})\,\xi_k+\sqrt{|g|}\,g^{\alpha\beta}\,\partial_\alpha X^l\,\partial_\beta X^k\,\nabla_l\xi_k.$$

Ensimmäinen termi on nolla, koska kenttäyhtälöt sanovat, että $T^{\alpha k}$ on divergenssitön. Toisessa termissä $g^{\alpha\beta}$ on symmetrinen, joten tulo $g^{\alpha\beta}\partial_\alpha X^l\partial_\beta X^k$ pysyy samana, kun indeksit k ja l vaihtavat paikkaa. Siksi derivaattojen $\nabla_l\xi_k$ paikalle voi kirjoittaa niiden keskiarvon, ja tämä keskiarvo on nolla, koska ξ on upotusavaruuden Killing-vektori. Kumpikin ehto pätee jokaisella kenttäyhtälöt toteuttavalla pinnalla, olipa pinta miten kaareva tahansa.

Loppukuvan lause "TGD säilyttää energian ja symmetriat" on tämä tulos. Säilymislaki tulee upotusavaruuden symmetriasta, joka on olemassa aina, eikä aika-avaruuden muodosta. Sama päättely koskee jokaista upotusavaruuden Killing-vektoria, joten säilyvät myös liikemäärä, pyörimismäärä, suure K ja CP₂:n kahdeksasta kierrosta tulevat värivaraukset, eli kaikki taulukon 10 + 8 suuretta.

### Mitä kuva jättää pois

- Virta on laskettu vaikutuksen tilavuusosasta. TGD:n vaikutuksessa on lisäksi Kähler-muodosta laskettu osa, ja sen virta lisätään samalla tavalla.
- Kuva näyttää yhden pinnan. Monilehtisessä aika-avaruudessa jokaisella lehdellä on oma virtansa, ja energiat lasketaan yhteen.
