-- insert
INSERT INTO
    account(account_id, account_name, account_password)
values
    (
        'david0970',
        '陳冠宇',
        'apple1234'
    );

INSERT INTO 
    store(store_name, store_html_id, store_date, store_tel, store_web)
values
    (
        "小口品S",
        "g16913-26-3-51-5-18-54-70-6-4-2",
        '1659268899.2852724',
        '0912345678',
        'https://www.facebook.com/xiaokoupin/'
    );
    
INSERT INTO
    post (post_store, post_title, post_context, post_author_id, post_date)
values
    (
        1,
        '國立嘉義大學',
        '我整個人都在嘉義大學啦，你想怎麼樣',
        'david0970',
        '1659268899.2852724'
    );


INSERT INTO
    img(store_id, img_addr)
values
    (
        1,
        "https://imgur.com/jkUWERl"
    );

INSERT INTO
    postcast(store_id, post_addr)
values
    (
        1,
        "https://imgur.com/jkUWERl"
    );

