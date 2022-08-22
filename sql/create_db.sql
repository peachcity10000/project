CREATE TABLE account(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    account_id TEXT NOT NULL,
    account_name TEXT NOT NULL,
    account_password TEXT NOT NULL
);

CREATE TABLE post(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    post_title TEXT NOT NULL,
    post_context TEXT NOt NULL,
        post_position_x_a REAL NOT NULL,
        post_position_y_a REAL NOT NULL,
        post_position_x_b REAL NOT NULL,
        post_position_y_b REAL NOT NULL,
    post_author_id TEXT NOT NULL,
    post_photo_addr TEXT,
    post_date REAL NOT NULL,
    post_tel TEXT,
    post_web TEXT
);


CREATE TABLE postcast(
    
)