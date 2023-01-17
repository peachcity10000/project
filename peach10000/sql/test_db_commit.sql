INSERT INTO
    account(account_id, account_name, account_password)
values
    (
        'david0970',
        '陳冠宇',
        'apple1234'
    );

INSERT INTO 
    store(store_name, store_html_id, store_date, store_tel, store_web, store_addr, store_open_time)
values
    (
        "AMON",
        "g16913-26-3-51-5-18-54-70-6-1-43",
        '1659268899.2852724',
        '05 222 2670',
        'https://www.facebook.com/AMONCafe666/',
        '嘉義市東區市宅街22巷5弄5號',
        '09:00–12:00、13:00–18:00 一二公休'
    );
    
INSERT INTO
    post (post_store_id, post_title, post_context, post_author_id, post_date, post_title_img)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-43',
        'AMON',
        '',
        'david0970',
        '1659268899.2852724',
        'https://i.imgur.com/iQhslEE.jpg'
    );


INSERT INTO
    img(store_id, img_addr)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-43',
        "CIVAAkL"
    );

INSERT INTO
    postcast(store_id, post_addr)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-43',
        ""
    );

