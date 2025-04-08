create database SonicBurger;
use SonicBurger;

create table usuarios(
id int not null auto_increment primary key,
nome varchar(250) not null,
cpf int(11) not null,
senha varchar(500) not null
);

select * from usuarios