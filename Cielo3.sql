--Query1--

WITH ai as (
    SELECT *
    FROM Aeroporto a, LuogoAeroporto la
    WHERE la.nazione = 'Italy'
)
SELECT v.comp, avg(v.durataMinuti) as MediaDurata
FROM ai, Volo v, ArrPart ap
WHERE ap.partenza = ai.aereoporto
and v.codice = ap.codice
group by v.comp

--oppure--

SELECT v.comp, avg(v.durataMinuti) as durataMediaVolo
FROM Volo v, LuogoAeroporto la, Aeroporto a, ArrPart ap
WHERE v.codice = ap.codice
    AND ap.partenza = a.codice
    AND la.aeroporto = a.codice
    AND la.nazione = 'Italy'
    group by v.comp

--Query2--
--Quali sono le compagnie che operano voli con durata media maggiore della durata media di tutti i voli--

WITH dmv as(
    SELECT avg(v.durataMinuti) as mediaVoli
    FROM Volo v
    WHERE true
)

SELECT v.comp, avg(v.durataMinuti)
FROM Volo v, dmv
WHERE true
group by v.comp, dmv.mediaVoli
having avg(v.durataMinuti) > dmv.mediaVoli

--Query3--
--Quali sono le città dove il numero totale di voli in arrivo è maggiore
--del numero medio dei voli in arrivo per ogni città?--

WITH cc as(
SELECT  la.citta, count(ap.arrivo) 
    FROM ArrPart ap, LuogoAeroporto la
    WHERE ap.arrivo = la.aeroporto
    group by la.citta
)

SELECT cc_a.citta, cc_a.count as countavg
FROM cc cc_a, cc cc_b
WHERE true
group by cc_a.citta,cc_a.count
having cc_a.count > avg(cc_b.count)

--Query4--

WITH dmv as(
SELECT avg(v.durataMinuti) as durataMediaVolo
    FROM ArrPart ap, LuogoAeroporto la, Volo v
    WHERE la.nazione = 'Italy'
    AND ap.partenza = la.aeroporto
    AND v.codice = ap.codice
)
--DA VEDERE PERCHE' DA RISULTATI DIVERSI MA IN TEORIA GIUSTI?--
SELECT ap.comp, avg(v.durataMinuti) as durataMediaVolo
    FROM ArrPart ap, LuogoAeroporto la, Volo v, dmv
    WHERE la.nazione = 'Italy'
    AND ap.partenza = la.aeroporto
	AND v.codice = ap.codice
	group by ap.comp, dmv.durataMediaVolo
	having avg(v.durataMinuti) < dmv.durataMediaVolo


--Query5--

WITH media as
(
    SELECT l.citta as citta,avg(v.durataMinuti) as media
    FROM Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a
    WHERE v.codice = ap.codice 
    AND v.comp = ap.comp
        AND ap.arrivo = a.codice
        AND l.aeroporto = a.codice
    GROUP BY l.citta
)
SELECT l.citta, avg(v.durataMinuti) as durata_media
FROM Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a,media
WHERE v.codice = ap.codice 
        AND v.comp = ap.comp
        AND arrivo = a.codice
        AND l.aeroporto = a.codice
GROUP BY l.citta,media.media
HAVING avg(v.durataMinuti) = (STDDEV(v.durataMinuti) + media.media)

--Query6--

WITH codice as (SELECT partenza FROM ArrPart)
SELECT l.nazione, count(DISTINCT l.citta) as citta
FROM Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a,codice
WHERE v.codice = ap.codice 
    AND v.comp = ap.comp
    AND ap.arrivo = a.codice
    AND ap.partenza <> codice.partenza
    AND l.aeroporto = a.codice
GROUP by l.nazione,l.citta




    