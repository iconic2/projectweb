
create table klanten(id integer primary key autoincrement,emailadres varchar(50), gebruikersnaam varchar(25), wachtwoord varchar(128),UNIQUE(emailadres, gebruikersnaam));


create table docenten(id integer primary key autoincrement, emailadres varchar(50), gebruikersnaam varchar(25), wachtwoord varchar(128), UNIQUE(emailadres, gebruikersnaam));


create table lessen(id integer primary key autoincrement, docent_id integer, taal_id integer, start date, locatie varchar(20) , foreign key(docent_id) references docenten(id), foreign key(taal_id) references lessen(id));


create table programmeer_talen(id integer primary key autoincrement, naam varchar(20), UNIQUE(id,naam));


create table klant_lessen(k_id,L_id integer primary key, foreign key(k_id) references klanten(id) foreign key (k_id) references lessen(id));











