CREATE TABLE Anagrafe{
    codice_fiscale VARCHAR(16) PRIMARY KEY,
    nome VARCHAR(100) not null,
    cognome VARCHAR(100) not null,
    data_nascita DATE not null
} 
CREATE TABLE Utenti {
    email VARCHAR(100) PRIMARY KEY,
    password VARCHAR(100) not null,
    privilegi VARCHAR(5) not null,
    note VARCHAR(255)
}
INSERT INTO Anagrafe (codice_fiscale, nome, cognome, data_nascita)
VALUES 
('dctnst34b56h501u', 'Mario', 'de martino', '1980-05-21'),
('dctnst34b56h501a', 'Gianni', 'de martino', '1980-05-21'),
('dctnst34b56h502w', 'Silvia', 'de martino', '1980-05-21'),
('aaaaa', 'Paolo', 'Rossi', '1990-02-24'),
('asddsa', 'adsadads', 'asdadsads', '1999-01-10'),  
('dsds', 'Roberto', 'Malatesta', '2000-01-10'),
('VLDPTN02H04Z145J', 'Vladimir', 'Putin', '1998-04-14'),
('GVNBNN01L04R132E', 'Gio', 'Ban', '2001-02-21'),
('CHTGPT01G01K000J', 'Chat', 'GPT', '2001-01-01'); 
INSERT INTO Utenti (email, password, privilegi, note)
VALUES 
('admincomune@comune.zagarolo.it', 'root_01', 'w', 'amministratore del sistema'),
('mariorossi@comune.zagarolo.it', 'mario01', 'w', 'sportello frazione 1'),
('gianni@gmail.com', 'gianni_123', 'r', 'sportello frazione 1');
