create table theme (
    id int auto_increment,
    title varchar(200),
    store varchar(200),
    address varchar(400),
    genre varchar(200),
    difficult int,
    recommended_people varchar(100),
    maximum_people int,
    play_time int,
    primary key(id)
);