CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL default "xyz@example.com",
    password_hash TEXT NOT NULL default "None",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

insert or ignore into users (id, username) values (0, "System");

create table if not exists "decks" ("id" integer not null primary key autoincrement,
                                    "name" text,
                                    "description" text,
                                    "creator_id" integer default 0,
                                    foreign key (creator_id) references users(id));

create table if not exists "cards" ("id" integer not null primary key autoincrement,
                                    "front_side" text,
                                    "back_side" text,
                                    "deck_id" integer,
                                    foreign key (deck_id) references decks(id));