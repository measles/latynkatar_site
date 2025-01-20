""" 
BSD 3-Clause License

Copyright (c) 2024, Andrej Zacharevicz

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

from dataclasses import dataclass


@dataclass
class Razdzieł:
    nazva: str
    zagalovak: str
    spasylki: tuple


pravapis = (
    (
        "https://languagetool.org/ ",
        "Цэлы камбайн па праверцы правапісу розных моў, у тым ліку беларускай. Ёсць плагіны для браўзэраў. Часта ім карыстаюся.",
    ),
    (
        "https://bnkorpus.info/spell.html",
        'Праверка правапісу ад праекту "Беларускі N-корпус"',
    ),
    (
        "https://bnkorpus.info/grammar.be.html",
        "Граматычная база Корпусу. Не вычэрпны даведнік, але бывае вельмі карысным для пошука форм слова.",
    ),
    (
        "https://bnkorpus.info/korpus.be.html",
        "Пошук слова па корпусе беларускіх тэкстаў.",
    ),
    (
        "https://slounik.org",
        "Процьма розных слоўнікаў і энцыклапедый. Але варта ўлічваць, што ў 20-30 мінулага стагоддзя было шмат эксперыментаў з мовай, так што слоўнікі таго перыяду трэба ўспрымаць з лёгкім скепсісам.",
    ),
    ("https://verbum.by", "Карысны набор слоўнікаў."),
)

knihi = (
    ("https://knihauka.com", 'Анлайн-кнігарня "Кнігаўка" выдавецтва Андрэя Янушкевіча'),
    ("https://allegro.pl/uzytkownik/Knihauka", '"Кнігаўка" на Allegro.pl'),
    (
        "https://gutenbergpublisher.eu/",
        "Еўрапейскае беларускае выдавецтва Gutenberg Publisher ",
    ),
    ("https://skarynapress.com/", "Выдавецтва Скарына"),
    (
        "https://knihi.by/",
        "Добрая анлайн-кнігарня з гісторыяй і традыцыямі. Працуе ў Мінску, але высылае і за мяжу. Калі браць досыць шмат кніг, то кошт высылкі не такі балючы.",
    ),
    (
        "https://kamunikat.shop/?v=9b7d173b068d",
        "Книгарня выдавецтва пры фондзе Камуникат. Вельми раю!"
    )
)

biblijateki = (
    (
        "https://kamunikat.org/",
        "Вялізны праект па збору ўсіх матэрыялаў (кнігі, аўдыёкнігі, газэты, часопісы, відэа і іншае) выданых па-беларуску ці пра Беларусь на іншых мовах. Ад 2021 яшчэ і выдае папяровы кнігі.",
    ),
    (
        "https://knihi.com/",
        "Наколькі я ведаю, старэйшая беларускай анлайн-бібліятэка (працуе ад 1996 года). Процьма самых розных выдпанняў.",
    ),
    (
        "https://audiobooks.by/",
        "Каталог беларускіх аўдыё-кніг. Вельмі раю, калі любіце гэты фармат.",
    ),
    (
        "https://knizhnyvoz.com/app/",
        "Аўдыёвыдавецтва, якое рупліва і старана агучвае беларускія кнігі. Кнігі можна паслухаць на сайце, альбо праз іх мабільныя аплікацыі.",
    ),
    (
        "https://knihi-online.com/",
        "Вельмі цікавая анлайн-бібліятэка, дзе ў PDF даступныя шмат якія выбітныя класічныя кнігі і шмат што з цікавага сучаснага.",
    ),
)

kanviertary = (
    (
        "https://baltoslav.eu/lat/index.php?mova=bx",
        "Лацінізатар ад праекта БалтаСлав. Апроч, уаласна, канвертэра змяшчае яшчэ цікавыя матэрыяла пра лацінку.",
    ),
    (
        "https://slounik.org/lat",
        "Нажаль, не цалкам цункцыянальны канвертэр ад Слоўніка. ",
    ),
)

dzieciam = (
    (
        "https://www.youtube.com/@gavarun-cartoons",
        "Гаварун — мультфільмы па-беларуску. Выдатны канал з перакладамі мульікаў і мультсерыялаў на беларускую мову. Якасныя і цікавыя мульцікі, асабіста вельмі люблю 'Хамфа'. 'Паляўнічых на цмовакаў', 'Пакаё' і 'Эрнэст і Селестына' ",
    ),
    (
        "https://gavarun.by/p/support",
        "Падтрымаць рэгулярны выпуск перакладаў і арыгінальных праектаў Гаваруна для дзяцей. Падтрымайце, калі вы глядзіце Гаварна, падтрымайце калі вы не глядзіце, але хочаце дапамагчы беларускім дзеям. Ці нават калі ўсё абрыдла — падтрымайце, зрабіце добрую справу.",
    ),
    (
        "https://www.youtube.com/@baybusby",
        'Канал з вельмі цікавымі дзіцячымі відэа: тут і відэаадаптацыя коміксаў "Асцярожна дзеці" і "Казкі з Маляванычам"',
    ),
    (
        "https://www.youtube.com/@vozhykibel3467",
        "Блізняты-важаняты. Выдатны і вельмі мілы мультсерыял на беларускай. Нажаль, выпуск перарваны, але я спадзяюся некалі ўбачыць працяг.",
    ),
    (
        "https://www.youtube.com/@bielamult",
        "Беламульт. Яшчэ адзін даволі вялікі рэсурс з мульцікамі па-беларуску.",
    ),
    (
        "https://knizhnyvoz.com/app/",
        "Аўдыёвыдавецтва, якое рупліва і старана агучвае беларускія кнігі. Шмат кніг для дзяцей і падлеткаў. Ёсць мабільныя аплікацыі, але можна слухаць і з браўзэра.",
    ),
    (
        "https://youtube.com/playlist?list=PLZvkfSDlL6yjg2IVRkUVXxh1P740mK2D1",
        'Пяцьдзесят серый "Свінкі Пэпы" па-беларуску.',
    ),
    (
        "https://dzietkam.knihi.com/",
        "Краіна казак. Процьма казак, дыяфільмаў, мульцікаў, песенек, калыханак. Нажаль, у мяне не працуе з сайту, але можна паставіць на тэлефон аплікацыю, там ўсё будзе.",
    ),
    (
        "https://youtube.com/playlist?list=PLZvkfSDlL6yjg2IVRkUVXxh1P740mK2D1",
        "English з Наталкай. Цудоўныя заняткі па ангельскай для вучняў пятых класаў ад Наталлі Харытанюк.",
    ),
    (
        "https://www.youtube.com/@historyjabielarusi",
        "Гісторыя Беларусі | Альгерд ужо ня той. Гістарычны канал для дзяцей, бацькоў і настаўнікаў.",
    ),
)

filmy = (
    (
        "https://youtube.com/@gavarun-movie",
        "Цяпер можна глядзець фільмы і серыялы ў цудоўным перакладзе Гаваруна. Не забывайце падтрымаць праект грашыма!",
    ),
    (
        "https://kinakipa.site/",
        "Праект Кінакіпа і яго вялізная калекцыя фільмаў для ўсёй сям'і па-беларуску.",
    ),
    (
        "https://anibel.net/",
        "Вялікая калекцыя анімэ (перакладзеных голасам і тытрамі) і фільмаў па-беларуску.",
    ),
    ("https://baravik.org/", "Беларускі торэнт-трэкер."),
)


RAZDZIEŁY = (
    Razdzieł(nazva="Filmy", zagalovak="Фільмы па-беларуску", spasylki=filmy),
    Razdzieł(
        nazva="Biblijateki",
        zagalovak="Анлайн бібліятэкі беларускіх кніг",
        spasylki=biblijateki,
    ),
    Razdzieł(
        nazva="Knihi",
        zagalovak="Выдавецтвы і кнігарні дзе можна купіць беларускія кнігі за мяжою",
        spasylki=knihi,
    ),
    Razdzieł(nazva="Dzieciam", zagalovak="Для дзяцей па-беларуску", spasylki=dzieciam),
    Razdzieł(
        nazva="Slouniki",
        zagalovak="Праверка правапісу, даведнікі, слоўнікі",
        spasylki=pravapis,
    ),
    Razdzieł(
        nazva="Kanviertary", zagalovak="Канвертары ў лацінку", spasylki=kanviertary
    ),
)
