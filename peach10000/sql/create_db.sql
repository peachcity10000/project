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
    store_web TEXT,
    store_addr TEXT,
    store_open_time TEXT
);

CREATE TABLE post(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    post_store_id TEXT NOT NULL,
    post_title TEXT NOT NULL,
    post_context TEXT NOt NULL,
    post_author_id TEXT NOT NULL,
    post_date REAL NOT NULL,
    post_title_img TEXT NOT NULL
);

CREATE TABLE img(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    store_id TEXT NOT NULL,
    img_addr TEXT NOT NULL
);

CREATE TABLE postcast(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    store_id TEXT,
    post_addr TEXT NOT NULL
)