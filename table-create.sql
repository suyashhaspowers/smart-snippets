-- entity tables
CREATE TABLE snippet (
    snippet_id SERIAL PRIMARY KEY,
    query TEXT,
    generated_snippet TEXT
);

CREATE TABLE ss_user (
    user_id TEXT PRIMARY KEY
);

-- relationship tables
CREATE TABLE user_snippet (
    snippet_id SERIAL REFERENCES snippet (snippet_id),
    user_id TEXT REFERENCES ss_user (user_id)
);
