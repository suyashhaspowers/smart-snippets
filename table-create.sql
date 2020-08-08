-- entity tables

-- model generated snippet table
CREATE TABLE snippet (
    snippet_id SERIAL PRIMARY KEY,
    query TEXT,
    generated_snippet TEXT
);

-- user reviewed snippet table
CREATE TABLE user_reviewed_snippet (
    snippet_id SERIAL PRIMARY KEY,
    query TEXT,
    reviewed_snippet TEXT
);

-- user table
CREATE TABLE ss_user (
    user_id TEXT PRIMARY KEY
);

-- relationship tables

-- map between the user and their reviwed snippet
CREATE TABLE user_snippet (
    snippet_id SERIAL REFERENCES user_reviewed_snippet (snippet_id),
    user_id TEXT REFERENCES ss_user (user_id)
);

-- map between model generated and user reviewed snippets
CREATE TABLE model_review_snippet (
    model_snippet_id SERIAL REFERENCES snippet (snippet_id),
    reviewed_snippet_id SERIAL REFERENCES user_reviewed_snippet (snippet_id)
);
