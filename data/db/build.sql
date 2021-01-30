CREATE TABLE IF NOT EXISTS users (
    UserID integer PRIMARY KEY,
    RoyalJelly integer DEFAULT 0,
    Honey integer DEFAULT 0,
    HoneyCooldown text DEFAULT CURRENT_TIMESTAMP
);