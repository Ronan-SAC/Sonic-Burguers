create database sonicBurguer;
use sonicBurguer;
 
create table Usuários(

idUser int auto_increment primary key,

Nome varchar(100) not null,

Telefone char(11) not null,

Cpf char(11) not null,

Senha varchar(30) not null

);
 
create table Histórico(

idHistory int auto_increment primary key,

idUser int not null,

NotaFiscal varchar(255),

PrecoTotal decimal(5,2) not null,

FOREIGN KEY (idUser) REFERENCES Usuários(idUser

)

);
 