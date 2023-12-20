--- Users Table
CREATE TABLE IF NOT EXISTS "users" ("id" INTEGER PRIMARY KEY AUTOINCREMENT,
                                    "username" TEXT NOT NULL UNIQUE,
                                    "email" TEXT NOT NULL UNIQUE,
                                    "password_hash" TEXT NOT NULL,
                                    "salt" TEXT NOT NULL,
                                    "created_at" TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                                    "is_locked" INTEGER DEFAULT 0,
                                    "is_email_verified" INTEGER DEFAULT 0,
                                    "pfp_image_location" TEXT DEFAULT "https://i0.wp.com/sbcf.fr/wp-content/uploads/2018/03/sbcf-default-avatar.png");
CREATE INDEX IF NOT EXISTS "idx_users_email" ON "users" ("email");
CREATE INDEX IF NOT EXISTS "idx_users_username" ON "users" ("username");

--- Use the password "password123" for logging in to system
INSERT OR IGNORE INTO "users"("id", "username", "email", "password_hash", "salt") VALUES (0, "System", "xyz@example.com", "scrypt:32768:8:1$9DZGmU2AKfgPKdga$73746b31d395388b8e4438b1aa02ba8ebd4978d55bb83dad483a16af97797b2a7f4536e3737aa562980232661dbfaef10c0375f9cd02fb9b9d0e7800f614aadb", "salt");

--- Decks Table
CREATE TABLE IF NOT EXISTS "decks" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "name" TEXT,
                                    "description" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    "is_public" INTEGER DEFAULT 1,
                                    FOREIGN KEY ("creator_id") REFERENCES "users"("id"));
CREATE INDEX IF NOT EXISTS "idx_decks_creator_id" ON "decks" ("creator_id");

--- Cards Table
CREATE TABLE IF NOT EXISTS "cards" ("id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                                    "front_side" TEXT,
                                    "back_side" TEXT,
                                    "creator_id" INTEGER DEFAULT 0,
                                    FOREIGN KEY ("creator_id") REFERENCES "users"("id"));
CREATE INDEX IF NOT EXISTS "idx_cards_creator_id" ON "cards" ("creator_id");

--- Card Links Table , where cards are linked to decks
CREATE TABLE IF NOT EXISTS "card_links" ("card_id" INTEGER NOT NULL,
                                         "deck_id" INTEGER NOT NULL,
                                         "deck_variation_id" INTEGER,
                                         PRIMARY KEY ("card_id", "deck_id"),
                                         FOREIGN KEY ("card_id") REFERENCES "cards"("id"),
                                         FOREIGN KEY ("deck_id") REFERENCES "decks"("id"),
                                         FOREIGN KEY ("deck_variation_id") REFERENCES "deck_variations"("id"));
CREATE INDEX IF NOT EXISTS "idx_card_links_card_id" ON "card_links" ("card_id");
CREATE INDEX IF NOT EXISTS "idx_card_links_deck_id" ON "card_links" ("deck_id");

--- Deck variations, for modifying user-shared content and lighten up the db
CREATE TABLE IF NOT EXISTS "deck_variations" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT,
    "original_deck_id" INTEGER NOT NULL,
    "user_id" INTEGER NOT NULL,
    "variation_details" TEXT,  -- Could be JSON describing the changes for instance "add" : 5,18,6, "remove" : 14,7
    FOREIGN KEY ("original_deck_id") REFERENCES "decks"("id"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id")
);
CREATE INDEX IF NOT EXISTS "idx_deck_variations_original_deck_id" ON "deck_variations" ("original_deck_id");
CREATE INDEX IF NOT EXISTS "idx_deck_variations_user_id" ON "deck_variations" ("user_id");

--- User Links Table, where users are linked to their decks 
CREATE TABLE IF NOT EXISTS "users_links" ("user_id" INTEGER NOT NULL,
                                          "deck_id" INTEGER NOT NULL,
                                          "favorite_tag" INTEGER DEFAULT 0,
                                          PRIMARY KEY ("user_id", "deck_id"),
                                          FOREIGN KEY ("user_id") REFERENCES "users"("id"),
                                          FOREIGN KEY ("deck_id") REFERENCES "decks"("id"));
CREATE INDEX IF NOT EXISTS "idx_users_links_user_id" ON "users_links" ("user_id");
CREATE INDEX IF NOT EXISTS "idx_users_links_deck_id" ON "users_links" ("deck_id");

--- Tracking failed login attempts and ips to prevent brute-force attackers when using different IPs
CREATE TABLE IF NOT EXISTS "failed_login_attempts" (
    "user_id" INTEGER NOT NULL,
    "ip_address" VARCHAR(45),
    "attempts" INTEGER DEFAULT 1,
    "last_failed_login" TIMESTAMP,
    PRIMARY KEY ("user_id", "ip_address"),
    FOREIGN KEY ("user_id") REFERENCES "users"("id")
);
CREATE INDEX "idx_failed_login_user_id" ON "failed_login_attempts"("user_id");
CREATE INDEX "idx_failed_login_ip_address" ON "failed_login_attempts"("ip_address");


