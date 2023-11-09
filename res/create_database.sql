CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    email TEXT NOT NULL default "xyz@example.com",
    password_hash TEXT NOT NULL default "None",
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT OR IGNORE INTO users (id, username) VALUES (0, "System");

CREATE TABLE if NOT EXISTS "decks" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "name" TEXT,
                                    "description" TEXT,
                                    "favorite_tag" INTEGER DEFAULT 0,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY (creator_id) REFERENCES users(id));

CREATE TABLE if NOT EXISTS "cards" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "front_side" TEXT,
                                    "back_side" TEXT);

create table if not exists "card_links" ("card_id" integer not null,
                                         "deck_id" integer not null,
                                         foreign key (card_id) references cards(id),
                                         foreign key (deck_id) references decks(id));