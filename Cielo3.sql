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
with aa as (SELECT a.codice as ae,count(ap.arrivo) as nta
from ArrPart ap
JOIN Aeroporto a ON ap.arrivo = a.codice
group by a.codice
),
--media tutte le citta--
cm as(
    SELECT avg(aa.nta) as numero
    FROM aa
    JOIN LuogoAeroporto la on la.aeroporto = aa.ae
    JOIN ArrPart ap on ap.arrivo = aa.ae
)
--calcolo citta sopra media
select la.citta, count(ap.arrivo) as numero
from cm,aa
JOIN LuogoAeroporto la on la.aeroporto = aa.ae
JOIN ArrPart ap on ap.arrivo = aa.ae
group by la.citta,cm.numero
having count(ap.arrivo) > cm.numero

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
    SELECT l.citta as citta,AVG(v.durataMinuti) as media
    FROM Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a
    WHERE v.codice = ap.codice and v.comp = ap.comp
        AND ap.arrivo = a.codice
        AND l.aeroporto = a.codice
    GROUP BY l.citta
)
SELECT l.citta, AVG(v.durataMinuti) as durata_media
FROM Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a,media
WHERE v.codice = ap.codice and v.comp = ap.comp
        AND arrivo = a.codice
        AND l.aeroporto = a.codice
GROUP BY l.citta,media.media
HAVING AVG(v.durataMinuti) = (STDDEV(v.durataMinuti) + media.media)

--Query6--

WITH codice as (SELECT partenza from ArrPart)
SELECT l.nazione, count(distinct l.citta) as citta
from Volo v, LuogoAeroporto l, ArrPart ap, Aeroporto a,codice
where v.codice = ap.codice and v.comp = ap.comp
    AND ap.arrivo = a.codice
    AND ap.partenza <> codice.partenza
    AND l.aeroporto = a.codice
GROUP by l.nazione,l.citta

--------------------------------------------

SELECT DISTINCT la.citta, count(ap.arrivo) --query 3 da rivedere--
    FROM ArrPart ap, LuogoAeroporto la
    WHERE ap.arrivo = la.aeroporto
    group by DISTINCT la.citta, ap.arrivo


    