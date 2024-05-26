HELP_1 = """<b><u>YÖNETİCİ KOMUTLARI :</b></u>

Komutların başına <b>c</b> ekleyerek bunları kanalda kullanabilirsiniz.


/pause : Şu anda çalan yayını duraklatır.
/resume : Duraklatılmış yayını devam ettirir.
/skip : Şu anda çalan yayını atlar ve sıradaki parçayı çalmaya başlar.
/end veya /stop : Sırayı temizler ve şu anda çalan yayını sonlandırır.
/player : Etkileşimli bir çalma paneli alırsınız.
/queue : Sıraya eklenen parçaların listesini gösterir.
"""

HELP_2 = """
<b><u>AUTH KULLANICILAR :</b></u>

Auth kullanıcılar botu yönetici olmadan kullanabilirler.

/auth [kullanıcı adı/kullanıcı ID'si] : Bir kullanıcıyı botun auth listesine ekler.
/unauth [kullanıcı adı/kullanıcı ID'si] : Bir kullanıcıyı auth kullanıcılar listesinden çıkarır.
/authusers : Botun auth kullanıcılar listesini gösterir.
"""

HELP_3 = """
<b><u>YAYIN YAPMA ÖZELLİĞİ</b></u> [Sadece sudoerler için] :

/broadcast [mesaj veya mesaja yanıt olarak] : Botun sunucu sohbetlerine bir mesaj yayınlamasını sağlar.

<b>Yayın Modları :</b>
<b>-pin</b> : Yayınladığınız mesajları sunucu sohbetlerinde sabitleyebilir.
<b>-pinloud</b> : Yayınladığınız mesajları sunucu sohbetlerinde sabitleyip üyelere bildirim gönderebilir.
<b>-user</b> : Mesajı botu başlatan kullanıcılara yayınlar.
<b>-assistant</b> : Mesajı botun asistan hesabından yayınlar.
<b>-nobot</b> : Botun mesajı yayınlamasını engeller.

<b>Örnek:</b> <code>/broadcast -user -assistant -pin Test yayını</code>
"""

HELP_4 = """<b><u>SOHBET KARA LİSTESİ ÖZELLİĞİ :</b></u> [Sadece sudoerler için]

Değerli botumuzu kullanarak, gereksiz sohbetleri sınırlayın.

/blacklistchat [sohbet ID'si] : Botu kullanarak bir sohbeti kara listeye alır.
/whitelistchat [sohbet ID'si] : Kara listeye alınan bir sohbeti beyaz listeye alır.
/blacklistedchat : Kara listeye alınan sohbetlerin listesini gösterir.

"""

HELP_5 = """
<u><b>Kullanıcı Engelleme:</b></u> [Yalnızca sudo'lar]

Siyah listelenen kullanıcıları engellemeye başlar, böylece bot komutlarını kullanamazlar.

/block [kullanıcı adı veya bir kullanıcıya yanıt ver] : Kullanıcıyı botumuzdan engeller.
/unblock [kullanıcı adı veya bir kullanıcıya yanıt ver] : Engellenen kullanıcının engelini kaldırır.
/blockedusers : Engellenen kullanıcıların listesini gösterir.
"""

HELP_6 = """
<u><b>Kanal Oynatma Komutları:</b></u>

Kanaldan ses/video yayını yapabilirsiniz.

/cplay : Kanalın video sohbetinde istenen ses parçasını çalmaya başlar.
/cvplay : Kanalın video sohbetinde istenen videoyu çalmaya başlar.
/cplayforce veya /cvplayforce : Devam eden yayını durdurur ve istenen parçayı çalmaya başlar.

/channelplay [sohbet kullanıcı adı veya ID] veya [devre dışı] : Kanalı bir gruba bağlar ve grup içinde gönderilen komutlarla parçaları çalmaya başlar.
"""

HELP_7 = """
<u><b>Global Engelleme Özelliği</b></u> [Yalnızca sudo'lar]:

/gban [kullanıcı adı veya bir kullanıcıya yanıt ver] : Kullanıcıyı tüm sunuculardaki sohbetlerden global olarak engeller ve botu kullanmasını engeller.
/ungban [kullanıcı adı veya bir kullanıcıya yanıt ver] : Global olarak engellenen kullanıcının engelini kaldırır.
/gbannedusers : Global olarak engellenen kullanıcıların listesini gösterir.
"""

HELP_8 = """
<b><u>Akış Döngüsü:</b></u>

<b>Devam eden akışı döngüde çalmaya başlar</b>

/loop [etkinleştir/devre dışı] : Mevcut akışı döngüye alır/devre dışı bırakır.
/loop [1, 2, 3, ...] : Belirtilen değere kadar döngüyü etkinleştirir.
"""

HELP_9 = """
<u><b>Bakım Modu</b></u> [Yalnızca sudo'lar]:

/logs : Botun günlüklerini alır.

/logger [etkinleştir/devre dışı] : Botun etkinliklerini kaydetmeye başlar/devre dışı bırakır.

/maintenance [etkinleştir/devre dışı] : Botun bakım modunu etkinleştirir veya devre dışı bırakır.
/help : ɢᴇᴛ ʜᴇʟᴩ ᴍᴇɴᴜ ᴡɪᴛʜ ᴇxᴩʟᴀɴᴀᴛɪᴏɴ ᴏғ ᴄᴏᴍᴍᴀɴᴅs.

/ping : Botun pingini ve sistem istatistiklerini gösterir.

/stats : Botun genel istatistiklerini gösterir.

<u><b>Oynat Komutları :</b></u>

<b>v :</b> video için.

<b>force :</b> zorla için.

/play veya /vplay : talep edilen şarkıyı video sohbetinde çalmaya başlar.

/playforce veya /vplayforce : devam eden akışı durdurur ve talep edilen şarkıyı çalmaya başlar.

<b><u>Karışık Kuyruk :</b></u>

/shuffle : kuyruğu karıştırır.

/queue : karıştırılmış kuyruğu gösterir.

<b><u>Akış Arama :</b></u>

/seek [saniye cinsinden süre] : akışı verilen süreye getirir.

/seekback [saniye cinsinden süre] : akışı verilen süre kadar geriye alır.

<b><u>Şarkı İndirme</b></u>

/song [şarkı adı/yt url] : YouTube'dan herhangi bir parçayı mp3 veya mp4 formatında indirir.

<b><u>Hız Komutları :</b></u>

Çalan akışın hızını kontrol edebilirsiniz. [Yalnızca yöneticiler]

/speed veya /playback : gruptaki ses oynatma hızını ayarlar.

/cspeed veya /cplayback : kanaldaki ses oynatma hızını ayarlar.
