CREATE TABLE leaders (
	leader_in VARCHAR(50),
    name VARCHAR(50),
    value FLOAT
);

CREATE TABLE player_stats(
	name VARCHAR(50),
	GP INTEGER,
    GS INTEGER,
    MIN FLOAT,
    PTS FLOAT,
    OFR FLOAT,
    DR FLOAT,
    REB FLOAT,
    AST FLOAT,
    STL FLOAT,
    BLK FLOAT,
    TNO FLOAT,
    PF FLOAT,
    AST_TNO FLOAT,
    PER FLOAT
);
CREATE TABLE shooting_stats (
	name VARCHAR(50),
    FGM FLOAT,
    FGA FLOAT,
    FG FLOAT,
    _3PM FLOAT,
    _3PA FLOAT,
    _3PP FLOAT,
    FTM FLOAT,
    FTA FLOAT,
    FTP FLOAT,
	_2PM FLOAT,
    _2PA FLOAT,
    _2PP FLOAT,
    SC_EFF FLOAT,
    SH_EFF FLOAT
);
SELECT *
FROM leaders;
SELECT *
FROM player_stats;
SELECT *
FROM shooting_stats;