# Energian säilyminen 16 sekunnissa

Tämä 16 sekunnin video näyttää, miksi energia ja muut symmetrioiden säilyvät suureet ovat TGD:ssä määriteltyjä, vaikka ne yleisessä suhteellisuusteoriassa menettävät määritelmänsä. Videon kuvat on laskettu tarkoista malleista, ja tarkistuslaskut ovat repon kansiossa [`scripts/lyhytvideot/energia`](https://github.com/markomanninen/tgd-geometry-lab/tree/main/scripts/lyhytvideot/energia). Sen jälkeen jokainen videon osa selitetään erikseen samalla tavalla kuin edellisessä videossa. Lukijaksi on ajateltu videon katsoja, joka osaa lukion pitkän matematiikan.

<div class="video">
<iframe src="https://www.youtube-nocookie.com/embed/0curwKLR44w" title="Energian säilyminen 16 sekunnissa" loading="lazy" allow="encrypted-media; picture-in-picture" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
</div>

## 1. Killingin vektori ja säilyvä virta

Videon aika on 0–2,4 sekuntia.

Einsteinin teoriassa ja sen tasaisessa erikoistapauksessa energia säilyy silloin, kun ajan siirto ei muuta aika-avaruuden metriikkaa. Tämän ehdon täsmällinen muoto on Killingin yhtälö, ja videon ensimmäiset sekunnit näyttävät sen yhdessä pisteessä.

### Mitä kuva näyttää

Kuvassa aika kulkee ylöspäin ja kaksi vaakasuuntaa ovat paikan suuntia. Kuvan tapahtumien joukko on piirretty hilaksi, eli säännölliseksi pisteiden ruudukoksi, ja lähikuva näyttää sen yhden pisteen.

Pisteessä on valokartio. Valokartio on kaksoiskartio, jonka pintaa pitkin valo kulkee pisteeseen ja pisteestä pois. Kartion leveys kertoo, kuinka pitkän matkan valo kulkee yhdessä aikayksikössä, ja kuvan nimiö näyttää tämän valon nopeuden lukuna 1,00. Videossa aika ja matka mitataan yksiköissä, joissa valon nopeus tasaisessa aika-avaruudessa on 1.

Meripihkainen nuoli on vektori ξ, jonka komponentit ovat (1, 0, 0, 0). Ensimmäinen komponentti on ajan suunta ja kolme muuta ovat paikan suuntia, joten ξ osoittaa suoraan ajassa eteenpäin. Kuva vie kartion kopion tämän nuolen suuntaan yhden hilan välin ylöspäin. Kopio osuu täsmälleen siellä jo olevan kartion päälle, ja valon nopeus on ylemmässäkin pisteessä 1,00.

### Killingin yhtälö

Kun jokaiseen aika-avaruuden pisteeseen piirretään oma nuoli, syntyy vektorikenttä. Ajan siirron vektorikentässä jokainen nuoli on sama ξ. Vektorikenttää kutsutaan Killingin vektoriksi, kun siirto sen nuolten suuntaan säilyttää metriikan. Metriikka on se sääntö, jolla lasketaan kaikki aikavälit ja etäisyydet. Valokartiot ovat metriikan näkyvä osa. Ne kertovat, mitkä suunnat ovat valonkaltaisia, ja neliulotteisessa aika-avaruudessa nämä suunnat määräävät metriikan yhtä yhteistä kerrointa vaille. Kuvan tasaisessa tapauksessa myös tämä kerroin on joka pisteessä sama, joten kartioiden osuminen päällekkäin tarkoittaa koko metriikan säilymistä.

Killingin yhtälö on

$$\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu=0.$$

Indeksit μ ja ν saavat arvot 0, 1, 2 ja 3, joten yhtälö on kuusitoista yhtälöä. Merkki ∇ on kovariantti derivaatta. Se mittaa, kuinka paljon vektorikenttä muuttuu siirryttäessä pisteestä toiseen. Tasaisessa aika-avaruudessa, kun koordinaatit ovat suorakulmaiset, se on tavallinen derivaatta kunkin koordinaatin suhteen. Ajan siirron komponentit ovat samat joka pisteessä, joten derivaatat ovat nollia ja yhtälö toteutuu.

### Miksi juuri Killingin vektori

Kuvan toinen kaavarivi kertoo, miksi Killingin vektori on energian kannalta ratkaiseva. Energia-liikemäärätensori T on 4 × 4 -taulukko, joka kertoo jokaisessa pisteessä, paljonko siinä on energiaa ja liikemäärää ja miten ne virtaavat. Kun T kerrotaan vektorilla ξ, tulos on vektorikenttä J, jonka komponentit ovat

$$J^\mu=\sum_\nu T^{\mu\nu}\xi_\nu.$$

Kun ξ on ajan siirto, summasta jää vain T:n aikasarake. Sen ensimmäinen komponentti on energian tiheys ja kolme muuta energian virtauksen suuntia, joten J on energian virta. Tässä videossa kirjain J tarkoittaa tätä virtaa.

Virran divergenssi mittaa, paljonko virtaa lähtee pienestä alueesta enemmän kuin sinne tulee. Se lasketaan tulon derivoimissäännöllä,

$$\nabla_\mu(T^{\mu\nu}\xi_\nu)=(\nabla_\mu T^{\mu\nu})\,\xi_\nu+T^{\mu\nu}\,\nabla_\mu\xi_\nu,$$

jossa toistuvista indekseistä summataan. Ensimmäinen termi on nolla, koska aine noudattaa paikallista säilymislakia $\nabla_\mu T^{\mu\nu}=0$. Toinen termi on summa kuudestatoista tulosta. Taulukko T on symmetrinen, eli $T^{\mu\nu}=T^{\nu\mu}$. Kun summassa vaihdetaan indeksien μ ja ν paikat, summa pysyy samana, ja siksi derivaattojen $\nabla_\mu\xi_\nu$ paikalle voi kirjoittaa niiden keskiarvon $\tfrac12(\nabla_\mu\xi_\nu+\nabla_\nu\xi_\mu)$. Tämä keskiarvo on puolet Killingin yhtälön vasemmasta puolesta. Kun ξ on Killingin vektori, toinen termi on siis nolla aineesta riippumatta, ja energian virran divergenssi on nolla. Kun ξ ei ole Killingin vektori, jokin aineen jakauma tekee toisesta termistä nollasta poikkeavan. Killingin yhtälö on näin täsmälleen se ehto, jolla virta säilyy kaikenlaisen aineen kanssa.

Divergenssitön virta antaa säilyvän kokonaisenergian, kun virtaa ei tule avaruuden reunojen takaa. Virta vie energiaa paikasta toiseen, mutta ei luo eikä hävitä sitä, joten koko avaruuden yli laskettu energia on sama jokaisena hetkenä.

### Lähikuvan avautuminen

Aikavälillä 1,45–2,4 sekuntia kamera vetäytyy kauemmas. Lähikuvan kartio osoittautuu yhdeksi hilan kartioista ja nuoli yhdeksi vektorikentän nuolista. Tasaisessa aika-avaruudessa jokainen kartio on sama ja jokainen nuoli on sama, joten ajan siirto säilyttää metriikan kaikkialla.

### Mitä kuva jättää pois

- Kuva näyttää kolme aika-avaruuden neljästä suunnasta, ajan ja kaksi paikan suuntaa.
- Hila on otos pisteistä. Killingin yhtälö koskee jokaista pistettä, myös hilan pisteiden välisiä.
- Kartiot on piirretty lyhyiksi, ja valokartio jatkuu rajatta.

## 2. Kymmenen Killingin vektoria ja kymmenen säilyvää suuretta

Videon aika on 2,4–4 sekuntia.

Tasaisella aika-avaruudella, jota kutsutaan Minkowskin avaruudeksi M⁴, on kymmenen toisistaan riippumatonta Killingin vektoria. Jokainen niistä antaa oman säilyvän suureensa samalla päättelyllä, jolla ajan siirto antoi energian osassa 1.

### Mitä kuva näyttää

Ruudun oikeassa reunassa on taulukko, johon kertyvät Killingin vektorit ja niiden säilyvät suureet. Hilan nuolet vaihtuvat kolme kertaa, ja taulukon luku kasvaa jokaisella vaihdolla:
- Paikan siirrossa jokainen nuoli osoittaa samaan vaakasuuntaan ja on samanpituinen. Siirtoja on kolme, yksi kutakin paikan suuntaa kohti, ja ne antavat liikemäärän p.
- Kierrossa nuolet kiertävät ympyröitä kuvan vaakatasossa, ja nuoli on sitä pidempi, mitä kauempana piste on kierron keskeltä. Kierron akseli on kuvasta puuttuva kolmas paikan suunta, ja jokainen hetki kierretään samalla tavalla. Kiertoja on kolme, yksi kunkin paikan akselin ympäri, ja ne antavat pyörimismäärän L.
- Puskussa nuolet kallistuvat ajan ja paikan välillä. Pusku eli Lorentz-pusku siirtää jokaisen tapahtuman siihen paikkaan ja hetkeen, jossa tapahtuma näkyisi tasaisesti liikkuvalle havaitsijalle. Puskuja on kolme, yksi kutakin liikkeen suuntaa kohti, ja ne antavat suureen K.

Ajan siirron kanssa vektoreita on 1 + 3 + 3 + 3 = 10. Kuva näyttää kierroista ja puskuista vain yhden kummastakin, ja taulukon merkintä ×3 kertoo, että kumpaakin on kolme. Nämä kymmenen muunnosta muodostavat yhdessä Poincarén ryhmän.

Pusku ja kierto ovat todellisia muunnoksia, jotka siirtävät tapahtumia aika-avaruudessa ja säilyttävät metriikan. Tämä erottaa ne osan 4 koordinaattien uudelleennimeämisestä, joka jättää tapahtumat paikalleen.

### Mitä suure K tarkoittaa

Energia, liikemäärä ja pyörimismäärä ovat tuttuja säilyviä suureita. Puskun suure K on vähemmän tuttu. Yhden kappaleen tapauksessa sen komponentti on

$$K_x=t\,p_x-E\,x.$$

Kun K on vakio, kappaleen paikka on $x=(t\,p_x-K_x)/E$, ja tämä kasvaa tasaisesti ajan mukana, koska $p_x$ ja E ovat vakioita. Monen kappaleen järjestelmässä E, p ja K lasketaan yhteen, ja sama yhtälö antaa energialla painotetun keskipisteen paikan. Suureen K säilyminen tarkoittaa siis, että järjestelmän energian painopiste liikkuu tasaisella nopeudella suoraa viivaa pitkin. Taulukon nimi massakeskipiste viittaa tähän painopisteeseen.

### Energia integraalina

Taulukon alle kirjoittuu kokonaisenergian kaava

$$E=\int T^{\mu\nu}\xi_\nu\,\mathrm d\Sigma_\mu.$$

Integraali lasketaan aikaviipaleen Σ yli. Aikaviipale on koko avaruus yhtenä hetkenä, ja dΣ on sen pieni tilavuuden osa, jonka suunta on viipaleen normaali. Integraali laskee yhteen osan 1 energian virran J, joka kulkee viipaleen läpi. Osan 1 tuloksen mukaan virta on divergenssitön, joten mikä tahansa myöhempi viipale antaa saman luvun. Kun ξ korvataan toisella Killingin vektorilla, sama kaava antaa liikemäärän, pyörimismäärän tai suureen K.

Tämä vastaavuus on Emmy Noetherin ensimmäinen lause vuodelta 1918. Lauseen mukaan jokaista jatkuvaa symmetriaa vastaa säilymislaki. Jatkuva symmetria tarkoittaa muunnosta, jonka suuruuden voi valita vapaasti ja pienentää nollaan, kuten siirron matkan tai kierron kulman.

### Mitä kuva jättää pois

- Nuolten pituudet on skaalattu näkyviksi. Kierron ja puskun nuolten pituus kasvaa rajatta etäisyyden mukana.

## 3. Aine ja kadonnut siirtosymmetria

Videon aika on 4–6 sekuntia.

Yleisessä suhteellisuusteoriassa, eli Einsteinin gravitaatioteoriassa, aine kaareuttaa aika-avaruuden. Kaarevuus tarkoittaa, että mikään koordinaattien valinta ei tee metriikasta tasaisen aika-avaruuden metriikkaa kokonaisella alueella. Kaareva aika-avaruus muuttuu yleensä paikasta ja ajasta toiseen, ja silloin ajan siirto ei säilytä metriikkaa ja energian kokonaismäärältä puuttuu määritelmä.

### Mitä kuva näyttää

Valkoiset pisteet ovat ainetta, joka on paineetonta pölyä. Pöly pysyy kuvan koordinaateissa paikallaan, joten jokainen pölyhiukkanen nousee suoraan pystyviivaa pitkin ajassa eteenpäin.

Kartiot muuttuvat aineen tullessa. Kartion leveys riippuu nyt sekä paikasta että hetkestä. Osan 1 lähikuvan alempi piste saa valon nopeudeksi 1,15 ja ylempi 0,90. Molemmat ovat valon nopeuksia kuvan koordinaateissa. Punainen kopio, jonka ajan siirto vie hilan välin ylöspäin, ei siksi osu ylemmän pisteen kartion päälle. Kohdassa 5,5 sekuntia, musiikin iskussa, ajan siirron nuolet hajoavat, kartiot tärisevät, ja energian kaava, Killingin yhtälö ja taulukon luku hajoavat merkeiksi. Hajoaminen kuvaa sitä, että energialta katoaa määritelmä.

Erilaiset valon nopeudet eivät yksin todista mitään, koska samat pisteet voi nimetä uusilla koordinaateilla, ja silloin luvut muuttuvat. Tasaisessakin aika-avaruudessa vinot koordinaatit antaisivat eri pisteille eri lukuja. Koordinaateista riippumaton tosiasia on se, montako Killingin vektoria aika-avaruudella on. Killingin yhtälö on tensoriyhtälö, joten jos jokin vektorikenttä toteuttaa sen yhdessä koordinaatistossa, sama kenttä toteuttaa sen kaikissa. Tämän ratkaisun Killingin vektorit ovat vain kolme kiertoa, joten sillä ei ole yhtään siirtoa, joka säilyttäisi metriikan, kirjoitettiinpa siirto millä koordinaateilla tahansa.

### Ratkaisu, josta kuva on laskettu

Kartiot on laskettu Einsteinin yhtälön tarkasta ratkaisusta, joka tunnetaan Lemaîtren, Tolmanin ja Bondin pölyratkaisuna. Sen metriikka on

$$\mathrm ds^2=\mathrm dt^2-R'(r,t)^2\,\mathrm dr^2-R(r,t)^2\,\mathrm d\Omega^2,\qquad R(r,t)=r\,\bigl(t-t_B(r)\bigr)^{2/3}.$$

Tässä r on pölyhiukkasen pysyvä nimi, joka kertoo, kuinka kaukana keskipisteestä hiukkanen on alkujaan, ja R on saman hiukkasen todellinen etäisyys hetkellä t, ja pilkku tarkoittaa derivaattaa r:n suhteen. Termi dΩ² on suunnan muutoksen osuus, sama kuin pallon pinnalla. Funktio t_B(r) on hetki, jolloin pölyn laajeneminen alkaa etäisyydellä r. Kuvan ratkaisussa laajeneminen alkaa keskellä myöhemmin, joten keskellä pöly on ehtinyt laajeta vähemmän ja on tiheämpää. Projektin [tarkistuslaskut](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) vahvistavat symbolisesti, että metriikka toteuttaa Einsteinin yhtälön pölylle.

Metriikan komponentit riippuvat ajasta t. Killingin yhtälön vasen puoli voidaan kirjoittaa koordinaateissa muotoon $\xi^\lambda\partial_\lambda g_{\mu\nu}+g_{\lambda\nu}\partial_\mu\xi^\lambda+g_{\mu\lambda}\partial_\nu\xi^\lambda$. Ajan siirron komponentit ovat tässäkin koordinaatistossa vakiot (1, 0, 0, 0), joten kaksi viimeistä termiä ovat nollia ja ensimmäisestä jää vain aikaderivaatta. Ajan siirron Killingin yhtälö supistuu siis muotoon

$$\frac{\partial g_{\mu\nu}}{\partial t}=0,$$

eli metriikan komponentit eivät saa riippua ajasta. Tämän ratkaisun komponentit riippuvat, joten ajan siirto ei ole Killingin vektori.

### Taulukko ja kaavat

Taulukosta jäävät voimaan vain kierrot. Ratkaisu on pallosymmetrinen, joten keskipisteen ympäri tehty kierto säilyttää metriikan, ja pyörimismäärä säilyy edelleen. Ajan siirto, paikan siirrot ja puskut menettävät Killingin vektorin aseman, joten energia, liikemäärä ja suure K yliviivautuvat, ja luku putoaa kymmenestä kolmeen.

Kaavarivit kertovat saman. Killingin yhtälön vasen puoli ei ole nolla, joten osan 1 päättelyn toinen termi ei häviä, ja virran $T^{\mu\nu}\xi_\nu$ divergenssi poikkeaa nollasta. Energian integraalista puuttuu se Killingin vektori, jolla energia-liikemäärätensori kerrottaisiin, ja kysymysmerkki on sen paikalla.

Paikallinen säilymislaki $\nabla_\mu T^{\mu\nu}=0$ pätee edelleen jokaisessa pisteessä. Kovariantin derivaatan metriikasta tulevat termit vaihtavat kuitenkin energiaa aineen ja kaarevan aika-avaruuden välillä, joten aineen energian integraali ei pysy vakiona, eikä gravitaatiolle ole koordinaateista riippumatonta energian tiheyttä, joka korjaisi vajeen. Pitkänen muotoilee tämän Einsteinin teorian energiaongelmaksi. Kaarevassa aika-avaruudessa Poincarén ryhmän varauksia, eli energiaa, liikemäärää, pyörimismäärää ja suuretta K, ei voi määritellä säilyvinä Noetherin varauksina.

### Mitä kuva jättää pois

- Kuvan ratkaisu säilyttää kolme kiertoa, koska se on pallosymmetrinen. Aika-avaruudessa, jossa ainetta on epäsymmetrisesti, Killingin vektoreita ei ole lainkaan.
- Valon nopeudet 1,15 ja 0,90 ovat nopeuksia kuvan koordinaateissa. Vapaasti putoavan havaitsijan oma mittaus antaa valon nopeudeksi aina 1.

## 4. Ekvivalenssiperiaate ja koordinaatit niminä

Videon aika on 6–8 sekuntia.

Yleisessä suhteellisuusteoriassa tasaisen aika-avaruuden kymmenen symmetriaa jäävät voimaan vain kunkin pisteen pienessä ympäristössä. Einstein yritti pelastaa kokonaisenergian lisäämällä gravitaatiokentälle oman energiansa, pseudotensorin. Video näyttää, miksi tämä paikkaus ei toimi. Paikattu energia riippuu siitä, miten aika-avaruuden pisteet nimetään, ja nimet ovat Einsteinin teoriassa vapaasti valittavissa.

### Vapaasti putoava kehys

Valkoinen laatikko on kehys, eli pieni laboratorio, jonka seinät määräävät koordinaatit. Laatikko nousee kuvassa yhden pölyhiukkasen maailmanviivaa pitkin. Maailmanviiva on hiukkasen reitti aika-avaruudessa, ja kuvassa ylöspäin on ajassa eteenpäin. Paineettomaan pölyyn ei vaikuta mikään muu kuin gravitaatio, joten pöly putoaa vapaasti, ja laatikko putoaa sen mukana. Kuvan koordinaatit on valittu liikkumaan pölyn mukana, ja siksi pöly pysyy niissä paikallaan, vaikka se putoaa.

Laatikon sisällä oleva valokartio on tasaisen aika-avaruuden kartio, jonka valon nopeus on 1. Tämä on ekvivalenssiperiaatteen sisältö. Vapaasti putoavassa kehyksessä gravitaation vaikutus katoaa, kun kehys on niin pieni, että aika-avaruuden kaarevuus ei sen sisällä näy mittauksissa. Siksi vapaasti putoavan havaitsijan mittaus antaa valon nopeudeksi aina 1, vaikka osan 3 koordinaatit antoivat luvut 1,15 ja 0,90.

Tasaisen aika-avaruuden symmetriat ovat näin voimassa kunkin pisteen pienessä ympäristössä. Ne eivät kuitenkaan anna Killingin vektoria koko aika-avaruuteen, sillä osan 3 mukaan Killingin yhtälöllä ei ole tässä ratkaisussa siirtoja ratkaisuinaan. Noetherin ensimmäinen lause tarvitsee koko aika-avaruuden kattavan symmetrian, joten se ei anna niistä säilyvää kokonaisenergiaa.

### Pseudotensori

Kohdassa 6 sekuntia hajonneen energiakaavan merkit kokoontuvat uudeksi kaavaksi

$$E=\int\bigl(T^{\mu\nu}+t^{\mu\nu}\bigr)\,\mathrm d\Sigma_\mu.$$

Oranssi $t^{\mu\nu}$ on gravitaatiokentän pseudotensori. Einstein rakensi ensimmäisen pseudotensorin, ja Landau ja Lifšits rakensivat myöhemmin omansa. Kummassakin summalla $T+t$ on tavallinen divergenssi, joka on nolla, ja silloin summan integraali säilyy. Kaavan alla oleva luku on tämän integraalin arvo pallon sisällä, jonka säde on 2,5 kuvan yksikköä, laskettuna kuvan pölyratkaisulle. Projektin tiedosto [`pseudo.py`](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/pseudo.py) laskee luvun Landaun ja Lifšitsin pseudotensorilla. Laskutavan oikeellisuus on tarkistettu kahdella tunnetulla tuloksella. Tasaisen aika-avaruuden energia on suorakulmaisissa koordinaateissa nolla, ja Schwarzschildin ratkaisun energia on sen massa.

Pseudotensori ei ole tensori, eli sen arvot muuttuvat koordinaattimuunnoksessa eri tavalla kuin todellisen fysikaalisen suureen arvot. Video näyttää tämän kahdella tavalla. Vapaasti putoavassa kehyksessä pseudotensori on nolla, koska se lasketaan metriikan ensimmäisistä derivaatoista, ja ne ovat putoavan kehyksen pisteessä nollia. Gravitaation energiatiheyden saa siis katoamaan mistä tahansa pisteestä valitsemalla koordinaatit sopivasti. Toinen tapa on seuraavan alaotsikon nimien vaihto.

### Koordinaatit ovat vain nimiä

Kohdassa 7 sekuntia hilan viivat alkavat vaeltaa. Kartiot ja pöly pysyvät paikallaan, mutta kahden hilan pisteen koordinaattiluvut muuttuvat. Kuva näyttää koordinaattimuunnoksen, joka antaa samoille tapahtumille uudet nimet.

Samalla pseudotensorin energia muuttuu. Luku lasketaan jokaisessa videon ruudussa uudelleen niillä koordinaateilla, jotka hila sillä hetkellä näyttää. Tapahtumat ja aine ovat samat, mutta luku vaihtelee alkuperäisen arvon 0,0554 ympärillä, ja kahdeksalla eri nimeämisellä se saa arvoja väliltä 0,029–0,085 ja hetkellisesti negatiivisiakin arvoja. Suure, jonka arvo riippuu nimistä, ei ole fysikaalinen kokonaisenergia. Kohdassa 7,5 sekuntia, musiikin iskussa, myös paikattu kaava hajoaa, ja sen paikalle jää merkintä E = ?.

Markon esseessä Through the Wormhole on Spacetime Surface uudelleennimeämistä verrataan kartan kaupunkien nimien vaihtamiseen, joka ei muuta kaupunkien paikkoja eikä niiden välisiä etäisyyksiä. Ero osan 2 puskuun on tämä. Pusku siirtää tapahtumia toisiin paikkoihin ja säilyttää metriikan, kun taas uudelleennimeäminen jättää tapahtumat paikalleen ja muuttaa vain niiden nimet. Einsteinin teoria on rakennettu niin, että sen yhtälöt ovat samat kaikilla nimeämistavoilla. Tätä kutsutaan yleiseksi koordinaatti-invarianssiksi. Esseen mukaan se on vahvan ekvivalenssiperiaatteen ilmaus. Vahva ekvivalenssiperiaate on alussa kuvatun periaatteen laajin muoto, jonka mukaan kaikki fysiikan lait ovat vapaasti putoavassa kehyksessä samat kuin suppeassa suhteellisuusteoriassa, ja laatikon kartio on sen yksi tapaus.

### Identiteetti eikä säilymislaki

Hajonneen paikkauksen alle kirjoittuu se, mitä koordinaattien vapaasta valinnasta seuraa. Koordinaattimuunnos valitaan neljän mielivaltaisen funktion avulla, kun taas Poincarén ryhmän muunnos valitaan kymmenellä luvulla. Noetherin toinen lause koskee funktioiden määräämiä symmetrioita, ja niistä seuraa identiteetti eikä uutta säilyvää suuretta. Einsteinin teoriassa identiteetti on

$$\nabla_\mu G^{\mu\nu}\equiv 0.$$

G on Einsteinin tensori, joka lasketaan metriikasta. Merkki ≡ kertoo, että yhtälö pätee jokaisella metriikalla, myös sellaisella, joka ei toteuta Einsteinin yhtälöä. Einsteinin yhtälö on $G^{\mu\nu}=8\pi G_N T^{\mu\nu}$, jossa $G_N$ on gravitaatiovakio. Kun yhtälön molemmilta puolilta otetaan divergenssi, identiteetti antaa paikallisen säilymislain $\nabla_\mu T^{\mu\nu}=0$. Tasaisessa aika-avaruudessa sama yhtälö antoi osassa 1 kokonaisenergian, koska siellä oli Killingin vektori, jolla tensori kerrottiin. Kaarevassa aika-avaruudessa Killingin vektoria ei ole, joten yhtälöstä jää vain paikallinen laki. Noether kutsui tällaisia säilymislakeja epäaidoiksi (improper), koska ne pätevät teorian rakenteen vuoksi eivätkä anna säilyvää kokonaismäärää.

### Mitä kuva jättää pois

- Putoava laatikko on piirretty isoksi. Ekvivalenssiperiaate koskee niin pientä aluetta, että kaarevuus ei siinä näy.
- Vaeltavat viivat näyttävät yhden koordinaattimuunnoksen. Mahdollisia muunnoksia on rajattomasti.

## 5. Pinta upotusavaruudessa

Videon aika on 8–10 sekuntia.

TGD eli topologinen geometrodynamiikka erottaa toisistaan kaksi asiaa, jotka Einsteinin teoriassa ovat sama. Aika-avaruus on TGD:ssä neliulotteinen pinta X⁴ kahdeksanulotteisessa avaruudessa H = M⁴ × CP₂, jota kutsutaan upotusavaruudeksi ja jota intro merkitsee H⁸. Pinta saa kaartua, mutta symmetriat kuuluvat upotusavaruudelle, jonka M⁴:n osa on tasainen ja pysyy samana.

### Mitä kuva näyttää

Hilan kartiot palaavat yksikköleveyteen ja pysyvät sellaisina loppuun asti. Hila on nyt viipale upotusavaruudesta H. Pystysuunta on edelleen aika t ja toinen vaakasuunta paikka x, mutta kolmas suunta on yksi CP₂:n suunta. Upotusavaruuden metriikka ei riipu siitä, mitä pintoja siinä on, joten sen kartiot eivät muutu koskaan. Kuvan viipaleessa metriikka on

$$\mathrm ds^2=\mathrm dt^2-\mathrm dx^2-\mathrm ds_{CP_2}^2.$$

Ajan suunnan etumerkki on vastakkainen kuin muiden seitsemän suunnan, ja tämä ero tekee ajasta ajan. Se, kumpi saa plusmerkin, on sopimus, ja projektissa aika saa plusmerkin.

Lasilevy on aika-avaruuspinta. Levyn siniset ristit ovat pinnan omia valokartioita. Pinnan tangenttitaso on taso, joka koskettaa pintaa pisteessä, ja upotusavaruuden kartio leikkaa sen pinnan valokartiossa. Kaksiulotteisella pinnalla leikkaus on kaksi viivaa, joita pitkin valo kulkee pinnalla. Pinnan metriikka on upotusavaruuden metriikka laskettuna vain pinnan suuntaisille vektoreille, ja sitä kutsutaan indusoiduksi metriikaksi. Gravitaatio on TGD:ssä indusoidun metriikan kaarevuutta.

### Pinnan muoto

TGD:ssä pinnan muodon määrää vaikutus. Vaikutus on luku, joka lasketaan pinnasta, ja kenttäyhtälöt ovat ehto, että luku ei muutu, kun pintaa muutetaan vähän. Vaikutuksen tilavuusosa on pinnan neliulotteinen tilavuus kerrottuna vakiolla, ja kuvan levy toteuttaa tämän osan kenttäyhtälöt. Kaksiulotteisessa tapauksessa tällaisen pinnan voi kirjoittaa muodossa

$$X(\sigma,\tau)=\Bigl(\tau,\ \tfrac12\bigl(a(\sigma-\tau)+a(\sigma+\tau)\bigr)\Bigr).$$

Parametri τ on aika ja σ paikka pinnalla. Kirjain s on kuvan CP₂-suunnan koordinaatti, ja a on käyrä tasossa (x, s), jonka pituus kasvaa yhtä nopeasti kuin sen parametri. Tämän pituusehdon ansiosta σ ja τ ovat pinnalla koordinaatit, joissa tilavuusosan kenttäyhtälö on aaltoyhtälö, ja jokainen kahden vastakkain kulkevan aallon summa ratkaisee aaltoyhtälön. Funktio a(σ − τ) on sama muoto siirrettynä matkan τ verran, joten se kulkee pinnalla valon nopeudella yhteen suuntaan, ja a(σ + τ) kulkee vastakkaiseen suuntaan. Pinnalla kulkee siis kaksi pulssia, ja kuvan hetkellä ne ovat juuri ohittaneet toisensa. Projektin [tarkistuslaskut](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) vahvistavat numeerisesti, että pinta toteuttaa kenttäyhtälön ja että ristit ovat valonkaltaisia.

### Taulukko syttyy uudelleen

M⁴:n kymmenen Killingin vektoria ovat taas voimassa, koska M⁴ on upotusavaruuden osana tasainen. Lisäksi CP₂:lla on kahdeksan Killingin vektoria. CP₂ on kaareva, mutta jokaisen sen pisteen ympäristö on samanlainen, ja kahdeksan toisistaan riippumatonta kiertoa säilyttää sen metriikan. Kierrot muodostavat ryhmän SU(3), ja Pitkäsen mukaan niiden varaukset ovat hiukkasfysiikan värivaraukset. Taulukon luku on siksi 10 + 8.

Pitkänen muotoilee ratkaisun näin. Poincarén symmetriat siirretään aika-avaruudesta upotusavaruuden osaan M⁴, ja silloin ne ovat voimassa, olipa pinta millä tavalla tahansa kaareva.

### Mitä kuva jättää pois

- Pinta on kaksiulotteinen kolmiulotteisessa viipaleessa. TGD:n pinta on neliulotteinen kahdeksanulotteisessa avaruudessa, ja kuvassa kaksi suuntaa edustaa neljää.
- CP₂:sta kuva näyttää yhden suunnan neljästä. CP₂ on suljettu avaruus, joten tuo suunta palaa itseensä, vaikka kuva piirtää sen suorana.
- Levyn muoto on laskettu pelkästä tilavuusosasta. TGD:n vaikutukseen kuuluu myös Kähler-muodosta laskettu osa.

## 6. Koko pinta siirtyy ja energia säilyy

Videon aika on 10–16 sekuntia.

Videon loppu näyttää, miksi globaali energia, eli koko avaruuden kokonaisenergia, säilyy TGD:ssä. Upotusavaruuden ajan siirto liikuttaa koko aika-avaruuspintaa, ja siirretty pinta toteuttaa samat kenttäyhtälöt kuin alkuperäinen. Noetherin ensimmäinen lause antaa tästä symmetriasta virran, joka kulkee pintaa pitkin katkeamatta.

### Koko pinta siirtyy

Meripihkaiset nuolet ovat upotusavaruuden ajan siirto, ja ne ovat samat jokaisessa hilan pisteessä. Siirto nostaa koko lasilevyn ylöspäin, ja levyn vanha paikka jää katkoviivaksi. Markon esseessä Through the Wormhole on Spacetime Surface Pitkänen kuvaa tätä vertaamalla pintaa jäykkään kappaleeseen, jota siirretään ja käännetään kokonaisena.

Ero Einsteinin teoriaan on siinä, mitä siirretään. Einsteinin teoriassa siirto olisi aika-avaruuden oma muunnos, ja osan 3 mukaan sellaista ei kaarevassa aika-avaruudessa ole. TGD:ssä siirto on upotusavaruuden muunnos, joka on olemassa aina, ja se vie pinnan toiseen paikkaan upotusavaruudessa.

Pinta itse muuttaa muotoaan, koska sen pulssit liikkuvat. Vertaus jäykkään kappaleeseen koskee siirtoa. Vaikutus lasketaan indusoidusta metriikasta, ja indusoitu metriikka lasketaan upotusavaruuden metriikasta, joka on siirron jälkeen sama. Siksi vaikutus on siirretylle pinnalle sama kuin alkuperäiselle, ja siirretty pinta toteuttaa samat kenttäyhtälöt.

### Siirron osa pinnan suuntaan

Seuraavaksi kuva jakaa siirron ξ neljässä levyn pisteessä kahteen osaan. Toinen osa on pinnan suuntainen ja toinen pintaa vastaan kohtisuora. Paksu nuoli on pinnan suuntainen osa, ja se on energian virran J suunta.

Vaikutuksen tilavuusosasta laskettu virta on vakiokerrointa vaille

$$T^{\alpha k}=\sqrt{|g|}\;g^{\alpha\beta}\,\partial_\beta X^k,\qquad J^\alpha=T^{\alpha k}\xi_k.$$

Indeksi α kulkee pinnan suuntia ja indeksi k upotusavaruuden suuntia. Merkintä |g| on pinnan indusoidun metriikan determinantin itseisarvo, ja sen neliöjuuri muuttaa koordinaattien pinta-alkiot todellisiksi pinta-aloiksi. Yläindeksinen $g^{\alpha\beta}$ on indusoidun metriikan käänteismatriisi, ja $\partial_\beta X^k$ on pinnan tangenttivektori. Tulo $\partial_\beta X^k\xi_k$ on siirron ξ ja tangenttivektorin pistetulo upotusavaruuden metriikalla. Kohtisuoran osan pistetulo jokaisen tangenttivektorin kanssa on nolla, joten virta riippuu vain ξ:n pinnan suuntaisesta osasta. Pitkänen kirjoittaa saman yleisesti katsausartikkelinsa TGD2024I kaavassa 2.4, jonka mukaan säilyvä isometriavirta on verrannollinen Killingin vektorin projektioon pinnan tangenttiavaruuteen.

### Virtaviivat ja nouseva aikaviipale

Meripihkaiset viivat ovat energian virran virtaviivoja. Ne alkavat levyn alareunasta ja päättyvät sen yläreunaan, ja jokainen kulkee koko matkan katkeamatta. Viivat on piirretty niin, että kahden vierekkäisen viivan väliin jää aina sama määrä energiaa.

Vaakataso on aikaviipale, joka nousee levyn läpi. Viipale leikkaa levyä valkoisessa käyrässä, ja käyrän pisteet ovat virtaviivojen leikkauspisteet. Joka korkeudella leikkauspisteitä on sama määrä, ja viipaleen läpi kulkeva energia on siksi kaikilla korkeuksilla sama. Projektin [tarkistuslaskussa](https://github.com/markomanninen/tgd-geometry-lab/blob/main/scripts/lyhytvideot/energia/check.py) energia on yhdeksällä viipaleella sama luku 6,8 kuvan yksiköissä. Kaavana sama asia on

$$E=\int T^{\alpha k}\xi_k\,\mathrm d\Sigma_\alpha,\qquad \nabla_\alpha\bigl(T^{\alpha k}\xi_k\bigr)=0.$$

Säilymislain päättely on samanlainen kuin osassa 1. Tulon derivoimissääntö antaa

$$\nabla_\alpha\bigl(T^{\alpha k}\xi_k\bigr)=(\nabla_\alpha T^{\alpha k})\,\xi_k+\sqrt{|g|}\,g^{\alpha\beta}\,\partial_\alpha X^l\,\partial_\beta X^k\,\nabla_l\xi_k.$$

Ensimmäinen termi on nolla, koska kenttäyhtälöt sanovat, että $T^{\alpha k}$ on divergenssitön. Toisessa termissä $g^{\alpha\beta}$ on symmetrinen, joten tulo $g^{\alpha\beta}\partial_\alpha X^l\partial_\beta X^k$ pysyy samana, kun indeksit k ja l vaihtavat paikkaa. Siksi derivaattojen $\nabla_l\xi_k$ paikalle voi kirjoittaa niiden keskiarvon, ja tämä keskiarvo on nolla, koska ξ on upotusavaruuden Killingin vektori. Kumpikin ehto pätee jokaisella kenttäyhtälöt toteuttavalla pinnalla, olipa pinta miten kaareva tahansa.

Loppukuvan lause "energia ja symmetriat säilyvät" on tämä tulos. Säilymislaki tulee upotusavaruuden symmetriasta, joka on olemassa aina, eikä aika-avaruuden muodosta. Sama päättely koskee jokaista upotusavaruuden Killingin vektoria, joten säilyvät myös liikemäärä, pyörimismäärä, suure K ja CP₂:n kahdeksasta kierrosta tulevat värivaraukset, eli kaikki taulukon 10 + 8 suuretta.

### Mitä kuva jättää pois

- Virta on laskettu vaikutuksen tilavuusosasta. TGD:n vaikutuksessa on lisäksi Kähler-muodosta laskettu osa, ja sen virta lisätään samalla tavalla.
- Kuva näyttää yhden pinnan. Monilehtisessä aika-avaruudessa jokaisella lehdellä on oma virtansa, ja energiat lasketaan yhteen.
