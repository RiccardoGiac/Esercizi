--Query1--



--Query2--



--Query3--



--Query4--

WITH mb as(

    SELECT p.nome,p.id
    FROM Progetto p, Progetto pr
    group by p.nome,p.budget,p.id
    having p.budget > avg(pr.budget)
)

SELECT per.nome, per.cognome
FROM Persona per, mb, AttivitaProgetto ap
WHERE mb.id = ap.progetto 
AND ap.persona = per.id

--Query5--

WITH mb as(

    SELECT p.nome,p.id
    FROM Progetto p, Progetto pr
    group by p.nome,p.budget,p.id
    having p.budget < avg(pr.budget)
)

SELECT mb.nome
FROM mb, AttivitaProgetto ap, AttivitaProgetto apr
WHERE ap.progetto = mb.id
AND apr.progetto = ap.progetto
AND ap.tipo = 'Ricerca e Sviluppo'
group by ap.oreDurata, apr.oreDurata, mb.nome
having count(ap.oreDurata) > avg(apr.oreDurata)

-----------------------

