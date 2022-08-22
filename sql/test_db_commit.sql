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
    post (
        post_title,
        post_context,
        post_position_x_a,
        post_position_y_a,
        post_position_x_b,
        post_position_y_b,
        post_author_id,
        post_photo_addr,
        post_date,
        post_tel,
        post_web
    )
values
    (
        '國立嘉義大學',
        '我整個人都在嘉義大學啦，你想怎麼樣',
        100.0,
        101.0,
        102.0,
        103.0,
        'david0970',
        'https://cdn.ftvnews.com.tw/manasystem/FileData/News/d06d1396-f59b-4518-9f50-d9662f1d6909.jpg' ,
        '1659268899.2852724',
        '09123456789',
        'https://www.google.com'
    );

