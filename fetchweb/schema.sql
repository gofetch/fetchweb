drop table if exists users;
create table users (
       uid integer primary key autoincrement,
       username string not null,
       email string not null,
       pw_hash string not null,
       UNIQUE(email),
       UNIQUE(username)
);

drop table if exists pending_users;
create table if not exists pending_users (
       username string not null,
       email string not null,
       pw_hash string not null,
       UNIQUE(email),
       UNIQUE(username)
);
