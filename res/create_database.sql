CREATE TABLE IF NOT EXISTS "users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                    "username" TEXT NOT NULL UNIQUE,
                                    "email" TEXT NOT NULL default "xyz@example.com",
                                    "password_hash" TEXT NOT NULL default "None",
                                    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);

INSERT OR IGNORE INTO users(id, username) VALUES (0, "System");

CREATE TABLE IF NOT EXISTS "decks" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "name" TEXT,
                                    "description" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY (creator_id) REFERENCES users(id));

CREATE TABLE IF NOT EXISTS "cards" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "front_side" TEXT,
                                    "back_side" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY (creator_id) REFERENCES users(id));

CREATE TABLE IF NOT EXISTS "card_links" ("card_id" INTEGER NOT NULL,
                                         "deck_id" INTEGER NOT NULL,
                                         FOREIGN KEY (card_id) REFERENCES cards(id),
                                         FOREIGN KEY (deck_id) REFERENCES decks(id));

ALTER TABLE "card_links" ADD CONSTRAINT "no_duplicate_card_links" UNIQUE (deck_id, card_id);

CREATE TABLE IF NOT EXISTS "users_links" ("user_id" INTEGER NOT NULL,
                                          "deck_id" INTEGER NOT NULL,
                                          "favorite_tag" INTEGER DEFAULT 0,
                                          FOREIGN KEY (user_id) REFERENCES users(id),
                                          FOREIGN KEY (deck_id) REFERENCES decks(id));

ALTER TABLE "card_links" ADD CONSTRAINT "no_duplicate_users_links" UNIQUE (user_id, deck_id);