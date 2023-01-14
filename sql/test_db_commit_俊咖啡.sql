-- insert
-- INSERT INTO
--     account(account_id, account_name, account_password)
-- values
--     (
--         'david0970',
--         '陳冠宇',
--         'apple1234'
--     );

INSERT INTO 
    store(store_name, store_html_id, store_date, store_tel, store_web, store_addr, store_open_time)
values
    (
        "俊咖啡",
        "g16913-26-3-51-5-18-54-70-6-1-52",
        '1659268899.2852724',
        '0970 953 353',
        'https://drinkkaffa.business.site/',
        '嘉義市西區遠東街22-5號',
        '09:30–14:00'
    );
    
INSERT INTO
    post (post_store_id, post_title, post_context, post_author_id, post_date, post_title_img)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-52',
        '俊咖啡',
        '如果有在聽我們Podcast的聽眾應該就知道，我們還常提到俊哥的名字。那麼沒錯，今天要來介紹的就是俊哥的店，俊咖啡！

Drink Kaffa最早是只有外送的，靠著一台摩托車在北港路農會、文化路OK超商等等嘉義市各地標都可以看到俊哥的身影。但是在疫情的肆虐下，現在已經不太會去文化路擺攤了。現在的俊咖啡與佐丿籽乾燥花在共同經營，開放些許座位，並且提供外送服務。

Drink Kaffa很特別，在第三波咖啡的潮流中，淺焙咖啡盛行，甚至出現了極淺焙來追求原豆風味。俊哥對每一階的烘焙產生的風味都會為學生們介紹，中焙咖啡對於大一剛入門的力編來說，是會盡量少碰的。除了印象中傳統咖啡的苦澀，也少了淺焙的酸香以及甜感。但是在某一次坐下來跟俊哥好好喝一杯時，經過俊哥的介紹，發現中焙咖啡具有淺焙咖啡所缺乏的豐富度與厚實感，而且烘焙度也還沒有到完全失去風味，仔細品嘗還是可以找到些許的酸香。另外，烘焙過程中火力賦予草本菸絲味，但是經過俊哥的烘焙和比例的調整，除了常見的堅果調，降低草本菸絲味轉變帶出巧克力甜感。味蕾堆疊出醇厚度，就是俊哥要的複雜度。

俊哥其實算是一種典型會打破砂鍋問到底的人，不被繁文縟節所拘束，講究事情的細節，尋找核心並透過實驗去探索新的技術。另外值得一提的是俊哥也喜歡玩攝影，FB和IG的照片都記錄著努力生活的痕跡。或許是因為出國的經歷讓這裡總是這麼自由，每日自我練習的累積讓這家店變得完整。這裡總是很平凡，但也很美好。',
        'david0970',
        '1659268899.2852724',
        'https://i.imgur.com/zfTlew1.jpg'
    );


INSERT INTO
    img(store_id, img_addr)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-52',
        "z1PF7PB"
    );

INSERT INTO
    postcast(store_id, post_addr)
values
    (
        'g16913-26-3-51-5-18-54-70-6-1-52',
        ""
    );

