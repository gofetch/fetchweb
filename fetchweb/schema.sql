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
create table pending_users (
       username string not null,
       email string not null,
       pw_hash string not null,
       UNIQUE(email),
       UNIQUE(username)
);


drop table if exists torrents;
create table torrents (
       tid string primary key autoincrement,
       media_type integer default 0,
       tracker_id integer default 1,
       external_id integer not null,
       name string not null,
       size integer not null,
       status integer default -1,
       image_url string,
       UNIQUE(tracker_id, external_id)
);

drop table if exists fetches;
create table fetches (
       uid integer not null,
       tid integer not null,
       date_added integer default current_timestamp,
       UNIQUE(uid, tid),
       FOREIGN KEY (uid) REFERENCES users(uid),
       FOREIGN KEY (tid) REFERENCES torrents(tid)
);

drop table if exists files;
create table files {
       fid integer primary key autoincrement,
       tid integer not null,
       size integer not null,
       filepath string not null,
       FOREIGN KEY (tid) REFERENCES torrents(tid)
}

