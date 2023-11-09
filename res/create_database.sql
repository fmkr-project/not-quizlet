--- Users Table
CREATE TABLE IF NOT EXISTS "users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                    "username" TEXT NOT NULL UNIQUE,
                                    "email" TEXT NOT NULL default "xyz@example.com",
                                    "password_hash" TEXT NOT NULL default "None",
                                    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
--- The password_hash values for System corresponds to the hash of the password "None123"
INSERT OR IGNORE INTO "users"("id", "username", "email", "password_hash") VALUES (0, "System", "xyz@example.com", "1faebba052902f1abba80cddc553f8d8f213e00e0e128da7dc628ddb0688cf0a");
--- Decks Table
CREATE TABLE IF NOT EXISTS "decks" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "name" TEXT,
                                    "description" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY (creator_id) REFERENCES users(id));
CREATE INDEX IF NOT EXISTS "idx_decks_creator_id" ON "decks" ("creator_id");
--- Cards Table
CREATE TABLE IF NOT EXISTS "cards" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "front_side" TEXT,
                                    "back_side" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY (creator_id) REFERENCES users(id));
CREATE INDEX IF NOT EXISTS "idx_cards_creator_id" ON "cards" ("creator_id");
--- Card Links Table , where cards are linked to decks
CREATE TABLE IF NOT EXISTS "card_links" ("card_id" INTEGER NOT NULL,
                                         "deck_id" INTEGER NOT NULL,
                                         PRIMARY KEY ("user_id", "deck_id"),
                                         FOREIGN KEY (card_id) REFERENCES cards(id),
                                         FOREIGN KEY (deck_id) REFERENCES decks(id));
CREATE INDEX IF NOT EXISTS "idx_card_links_card_id" ON "card_links" ("card_id");
CREATE INDEX IF NOT EXISTS "idx_card_links_deck_id" ON "card_links" ("deck_id");

--- User Links Table, where users are linked to their decks
CREATE TABLE IF NOT EXISTS "users_links" ("user_id" INTEGER NOT NULL,
                                          "deck_id" INTEGER NOT NULL,
                                          "favorite_tag" INTEGER DEFAULT 0,
                                          PRIMARY KEY (user_id, deck_id),
                                          FOREIGN KEY (user_id) REFERENCES users(id),
                                          FOREIGN KEY (deck_id) REFERENCES decks(id));
CREATE INDEX IF NOT EXISTS "idx_users_links_user_id" ON "users_links" ("user_id");
CREATE INDEX IF NOT EXISTS "idx_users_links_deck_id" ON "users_links" ("deck_id");