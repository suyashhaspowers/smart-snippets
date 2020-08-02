-- entity tables
CREATE TABLE snippet (
    snippet_id SERIAL PRIMARY KEY,
    query TEXT,
    generated_snippet TEXT
);

CREATE TABLE ss_user (
    user_id SERIAL PRIMARY KEY
);

-- relationship tables
CREATE TABLE user_snippet (
    snippet_id SERIAL REFERENCES snippet (snippet_id),
    user_id SERIAL REFERENCES ss_user (user_id)
);
