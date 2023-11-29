DROP TABLE IF EXISTS activities;

CREATE TABLE activities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    nightlife INTEGER,
    restaurant INTEGER,
    bakery INTEGER,
    activity INTEGER,
    adult_ent INTEGER,
    nighclub INTEGER,
    music_venue INTEGER,
    comedy_club INTEGER,
    outdoors INTEGER,
    visited INTEGER
);