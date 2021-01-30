CREATE TABLE IF NOT EXISTS honey (
    UserID integer PRIMARY KEY,
    RoyalJelly integer DEFAULT 0,
    Honey integer DEFAULT 0,
    HoneyCooldown text DEFAULT CURRENT_TIMESTAMP
);