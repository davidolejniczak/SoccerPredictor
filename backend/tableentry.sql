--Postgres SQL schema, and script to create the tables 

CREATE TABLE matches (
  MatchId VARCHAR(10) PRIMARY KEY,
  teamA VARCHAR(255), 
  teamB VARCHAR(255),
  date DATE,
  time TIME,
  teamAprob VARCHAR(10),
  drawprob VARCHAR(10),
  teamBprob VARCHAR(10),
  FOREIGN KEY (teamA) REFERENCES standingStats(Team),
  FOREIGN KEY (teamB) REFERENCES standingStats(Team)
);

CREATE TABLE standingStats (
  Position INT NOT NULL,        -- Position in the league
  Team VARCHAR(100) PRIMARY KEY,
  MP INT NOT NULL,              -- Matches Played
  W INT NOT NULL,               -- Wins
  D INT NOT NULL,               -- Draws
  L INT NOT NULL,               -- Losses
  GF INT NOT NULL,              -- Goals For
  GA INT NOT NULL,              -- Goals Against
  GD VARCHAR(10) NOT NULL,      -- Goal Difference (string to include "+" and "-")
  Pts INT NOT NULL,             -- Points
  Last5 VARCHAR(10),            -- Last 5 Match Results
  PPG FLOAT,                    -- Points Per Game
  CS VARCHAR(10),               -- Clean Sheets Percentage
  BTTS VARCHAR(10),             -- Both Teams to Score Percentage
  xGF FLOAT,                    -- Expected Goals For
  Plus1_5 VARCHAR(10),          -- Percentage of Matches with Over 1.5 Goals
  Plus2_5 VARCHAR(10),          -- Percentage of Matches with Over 2.5 Goals
  AVG FLOAT                     -- Average Goals Per Match
);

CREATE TABLE btts (
  Team VARCHAR(100) PRIMARY KEY,     -- Team name
  MP INT NOT NULL,                 -- Matches Played
  BTTS INT NOT NULL,               -- Number of matches where Both Teams Scored
  BTTS_Percentage VARCHAR(10),     -- Percentage of BTTS matches
  Home_Percentage VARCHAR(10),     -- Home BTTS percentage
  Away_Percentage VARCHAR(10),     -- Away BTTS percentage
  FOREIGN KEY (Team) REFERENCES standingStats(Team)
);
