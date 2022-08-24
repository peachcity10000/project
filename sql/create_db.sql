CREATE TABLE account(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    account_id TEXT NOT NULL,
    account_name TEXT NOT NULL,
    account_password TEXT NOT NULL
);

CREATE TABLE store(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    store_name TEXT NOT NULL,
    store_html_id TEXT NOT NULL,
    store_date REAL NOT NULL,
    store_tel TEXT,
    store_web TEXT
);

CREATE TABLE post(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    post_store INTEGER NOT NULL,
    post_title TEXT NOT NULL,
    post_context TEXT NOt NULL,
    post_author_id TEXT NOT NULL,
    post_date REAL NOT NULL
);

CREATE TABLE img(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    store_id INTEGER NOT NULL,
    img_addr TEXT NOT NULL
);

CREATE TABLE postcast(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    store_id INTEGER,
    post_addr TEXT NOT NULL
)