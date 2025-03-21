import telebot
from telebot import types

bot = telebot.TeleBot('7632418148:AAHe757NGrLH4Qr8X1ObxGFUMKoiOZnFlgA')

user_answers = {}

def create_reply_markup(options):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    for option in options:
        markup.add(types.KeyboardButton(option))
    return markup

@bot.message_handler(commands=['start', 'restart'])
def handle_start_restart(message):
    user_answers[message.chat.id] = []  # Очищаем ответы пользователя
    if message.text == '/start':
        bot.send_message(
            message.chat.id,
            f'Привет, {message.from_user.first_name}! Давай знакомиться! Я задам тебе пару вопросов, только отвечай честно! Готов?...',
            reply_markup=create_reply_markup(['Конечно! Начнем'])
        )
    elif message.text == '/restart':
        bot.send_message(
            message.chat.id,
            'Снова привет! Взглянем иначе на эти вопросы, готов?',
            reply_markup=create_reply_markup(['Конечно! Начнем'])
        )
    bot.register_next_step_handler(message, on_1click)

def on_1click(message):
    if message.text == 'Конечно! Начнем':
        bot.send_message(message.chat.id, 'Ну что ж! Первый вопрос..')
        first_q(message)

def first_q(message):
    options = ['A1', 'B1', 'C1', 'D1', 'E1']
    options_text = ['Целеустремленность и амбиции', 'Харизма и веселье', 'Упорство и стабильность', 'Беззаботность и неторопливость', 'Рассудительность и независимость']
    markup = create_reply_markup(options_text)
    bot.send_message(message.chat.id, 'Что из этого про вас?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: callback_w1(msg, options, options_text))

def callback_w1(message, options, options_text):
    selected_option = options[options_text.index(message.text)]  # Получаем идентификатор опции
    user_answers[message.chat.id].append(selected_option)  # Сохраняем идентификатор опции
    bot.send_message(message.chat.id, 'Запомню : )')
    sec_q(message)

def sec_q(message):
    options = ['A2', 'B2', 'C2', 'D2', 'E2']
    options_text = ['Спорт и физическая активность', 'Близкие люди', 'Медитация и чтение', 'Творчество', 'Достижение целей']
    markup = create_reply_markup(options_text)
    bot.send_message(message.chat.id, 'Что помогает вам поддерживать бодрость духа?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: callback_w2(msg, options, options_text))

def callback_w2(message, options, options_text):
    selected_option = options[options_text.index(message.text)]
    user_answers[message.chat.id].append(selected_option)
    bot.send_message(message.chat.id, 'Класс!')
    third_q(message)

def third_q(message):
    options = ['A3', 'B3', 'C3', 'D3', 'E3']
    options_text = ['Минимализм', 'Классика', 'Что-то романтичное', 'Декор по настроению', 'Рандомный артхаус']
    markup = create_reply_markup(options_text)
    bot.send_message(message.chat.id, 'Какой стиль для оформления вашего дома предпочтительнее?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: callback_w3(msg, options, options_text))

def callback_w3(message, options, options_text):
    selected_option = options[options_text.index(message.text)]
    user_answers[message.chat.id].append(selected_option)
    bot.send_message(message.chat.id, 'Мы все ближе! Осталось чуть-чуть.')
    fourth_q(message)

def fourth_q(message):
    options = ['A4', 'B4', 'C4', 'D4']
    options_text = ['С утра', 'К обеду', 'Вечером-ночью', 'Как получится']
    markup = create_reply_markup(options_text)
    bot.send_message(message.chat.id, 'В какое время дня свернем горы?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: callback_w4(msg, options, options_text))

def callback_w4(message, options, options_text):
    selected_option = options[options_text.index(message.text)]
    user_answers[message.chat.id].append(selected_option)
    bot.send_message(message.chat.id, 'ОГО!')
    fifth_q(message)

def fifth_q(message):
    options = ['A5', 'B5', 'C5', 'D5', 'E5', 'F5']
    options_text = ['Душа компании', 'Ма-мо-чка', 'Кайфолом', 'Мудрый друг', 'Авантюрист', 'Слушаюсь и повинуюсь']
    markup = create_reply_markup(options_text)
    bot.send_message(message.chat.id, 'Кто ты в компании?', reply_markup=markup)
    bot.register_next_step_handler(message, lambda msg: callback_w5(msg, options, options_text))

def callback_w5(message, options, options_text):
    selected_option = options[options_text.index(message.text)]
    user_answers[message.chat.id].append(selected_option)
    bot.send_message(message.chat.id, 'С вопросами покончено! Теперь результат!..')
    send_result(message)

coffee_recipes = {
    "americano": "Кофе американо (americano) — это напиток на основе эспрессо с добавлением горячей воды. Американо популярен во всем мире, хотя появился совершенно случайно. Поклонников привлекает яркий аромат, насыщенный и в то же время мягкий вкус и благородный глубокий цвет напитка.Турка, или джезва, понадобится, чтобы приготовить основу для будущего американо. Добавьте 2 чайные ложки кофе сверхмелкого помола в турку и прогрейте на медленном огне в течение минуты. После появления кофейного аромата добавьте сахар по вкусу и 50 мл воды. Важно не доводить напиток до кипения и снять турку с плиты, как только появится пена. После ее оседания повторно нагрейте турку, чтобы аромат и вкус кофе лучше раскрылись. Готовый эспрессо перелейте в кружку и добавьте горячую воду в пропорции 1:1, 1:2 или 1:4. Бодрящий американо готов!",
    "cappuccino": "Капучино (Cappuccino) — это кофейный напиток объемом 150-180 мл, в котором гармонично сочетаются эспрессо и молоко. Для приготовления капучино берут одну порцию эспрессо, а молоко предварительно взбивают: толщина шапочки из пены должна быть не менее 1 см.Сварить основу для капучино можно и в турке: получится, конечно, не классический вариант эспрессо, а крепкий черный кофе с насыщенным вкусом.На 100 мл воды достаточно двух ложек молотого кофе. Турку прогрейте на огне, засыпьте кофе и еще немного прогрейте. Добавьте воду и дождитесь образования пенки на поверхности напитка. Снимите турку с огня и немного остудите, затем еще раз доведите напиток до образования пенки. Но не до кипения! Снимите турку с огня и перелейте черный кофе в кружку для капучино. Молоко нужно разогреть до температуры 50-65°C, перелить в удобную емкость и взбивать до образования пышной пенки. По готовности — перелить в чашку с кофе. ",
    "latte": "Кофе латте («caffè latte») — в переводе с итальянского языка «кофе с молоком», — кофейно-молочный напиток на основе эспрессо. Деликатный молочный вкус латте придется по душе тем, кто любит не слишком крепкие кофейные напитки. Для кофе латте готовят одну стандартную порцию эспрессо. Для этого нужно вскипятить воду и смешать 1 чайную ложку растворимого кофе и 30 миллилитров горячей воды. Затем эспрессо наливают в прогретый стеклянный стакан или чашку большого объема. Если у вас под рукой нет автоматической или рожковой кофемашины, то приготовить основу для латте можно в турке.Для взбивания молочной пенки понадобится ручной капучинатор или френч-пресс. Температура молока должна быть от 60 °C до 65 °C, тогда напиток получится с характерным сладковатым сливочным вкусом. Если температура молока будет выше, то во вкусе кофе латте появятся горьковатые нотки, а пенка будет рыхлой и «сухой». Когда на поверхности молока образуется устойчивая пенка, его аккуратно переливают в кружку с горячим эспрессо.",
    "ice_latte": "Рецепт айс-латте:\n1. Заварите 30 мл эспрессо и охладите его\n2. В стакан насыпьте лёд\n3. Добавьте 150 мл холодного молока\n4. Влейте сверху эспрессо.",
    "raf": "Кофе раф — сладкий кофейно-молочный напиток на основе эспрессо. Нежный сливочный вкус и шелковистая обволакивающая текстура рафа придутся по душе тем, кто не любит слишком крепкий кофе или только начинает свое знакомство с популярным напитком. Его также оценят сладкоежки, особенно — версии с различными добавками.Для стандартного рафа понадобится 30 мл эспрессо, 100 мл 10%-ных сливок, 1 ч. л. ванильного сахара и 1 ч. л. тростникового сахара.Порцию эспрессо можно сварить в автоматической или рожковой кофемашине. Также можно воспользоваться туркой.Для взбивания понадобится ручной капучинатор, френч-пресс или стимер. Оптимальная температура сливок от 60 °C до 65 °C, но если планируете использовать стимер, то берите холодные сливки: тогда раф получится воздушным и нежным.Принцип приготовления простой: в отдельной емкости смешайте кофе, сливки и сахар и взбейте до образования нежной пенки и множества микропузырьков.Украсить раф можно любимыми специями или шоколадной стружкой, а можно оставить как есть — это дело вкуса!",
    "flat-white": "Флэт уайт (flat white — дословно переводится как «плоский белый») — напиток на основе эспрессо и горячего молока, с тонким слоем шелковистой пенки. Взбить молочную пенку для флэт уайт можно с помощью ручного капучинатора, френч-пресса или стимера — встроенной в кофемашину трубки, из которой подается пар. Молоко лучше брать цельное, жирностью 3,2%. Чтобы пенка получилась эластичная, с правильной шелковистой текстурой, температура молока должна быть не выше 60 °C, а взбивать его нужно до тех пор, пока не появятся мелкие пузырьки воздуха. По готовности — аккуратно перелить в чашку с горячим эспрессо.Основу для напитка можно приготовить не только в кофемашине, но и в турке или из растворимого кофе. Для этого достаточно смешать 1 чайную ложку кофе и 30 мл горячей воды, а затем добавить 150 мл молока, предварительно взбитого до образования пенки. ",
    "mocha": "Мокко – это напиток на основе кофе, молока и шоколада. Но этим вашу креативность никто не ограничивает и смело можно использовать варианты добавления разных ингредиентов по своему вкусу: взбитые сливки, маршмеллоу, ваниль, корица и т. п.Разделите шоколад на 2 порции: 10 и 50 г. 50 г шоколада растопите. Для этого сделайте водяную баню и добавьте в шоколад ложку молока.Пока та часть тает, оставшиеся 10 г шоколада посредством терки превратите в стружку. Когда шоколад будет растоплен, вылейте его в бокал.Сварите черный кофе, если желаете – с добавлением сахара. Перелейте его в бокал, но не размешивайте с растаявшим шоколадом.Взбейте молоко при помощи капучинатора до температуры 65 градусов.Добавьте молоко в кофе. Чтобы оно не смешалось, его аккуратно льют по лезвию ножа.Если используете взбитые сливки, самое время выложить их сверху на молоко.Посыпьте композицию шоколадной стружкой",
    "unknown": "Пока у нас нет точного рецепта для тебя, но попробуй экспериментировать с вкусами! 😉"
}
user_coffee_choice = {}

def send_result(message):
    answers = user_answers.get(message.chat.id, [])

    if ('A1' in answers or 'C1' in answers or 'E1' in answers) and (
            'C2' in answers or 'E2' in answers or 'A2' in answers) and (
            'C3' in answers or 'A3' in answers or 'B3' in answers) and (
            'A5' in answers or 'D5' in answers or 'E5' in answers or 'C5' in answers):
        result = "Что может сказать о вас американо? Точно ничего плохого! Вероятнее всего, ваша главная черта — прямолинейность. У вас всегда порядок не только на столе, но и в голове. Ваш кофе не содержит в себе ни молока, ни сахара, ни сливок — это подчеркивает вашу серьезность. Вас легко можно назвать человеком действия, полным амбиций. Споры и конфликты — не ваш метод, возможно потому, что с вами никто не рискует вступать в противостояние. Четко и сурово :) В общем, американо отличный напиток. Кстати, именно его предпочитают Анджелина Джоли и Квентин Тарантино."
        result_image = 'https://www.roastmarket.de/magazin/wp-content/uploads/2016/05/Caffe-Americano-in-Tasse.jpg'
        coffee_type = "americano"
    elif ('B1' in answers or 'D1' in answers) and ('B2' in answers or 'D2' in answers or 'C2' in answers) and (
            'C3' in answers or 'D3' in answers or 'E3' in answers) and (
            'A5' in answers or 'E5' in answers or 'B5' in answers):
        result = "Капучино: нежность или практичность? Чувствуете себя звездой, как Николь Кидман или Бритни Спирс? Тогда этот напиток точно ваш! Капучино выбирают открытые и позитивные личности. Вам нравится быть среди людей, вы всегда честны со своими близкими и не отказываетесь от новых знакомств и возможностей. Творчество — ваше все, как и мотивация. Дух романтики и приключений вас не отпускает, вы всегда в поисках чего-то интересного. Однообразие точно не про вас, особенно если вы любите добавлять в свой кофе сиропы. "
        result_image = 'https://i-coffee.me/wp-content/uploads/2022/02/Coffee_Cappuccino_Cream_Cup_Saucer_525045_2048x1152.jpg'
        coffee_type = "cappuccino"
    elif ('A1' in answers or 'E1' in answers or 'C1' in answers) and (
            'C2' in answers or 'D2' in answers or 'A2' in answers) and (
            'A3' in answers or 'B3' in answers or 'D3' in answers) and (
            'C5' in answers or 'D5' in answers or 'A5' in answers):
        result = "Ваш напиток легкий и воздушный латте! Тейлор Свифт большая поклонница латте и карамельного сиропа. Если вы точно так же любите этот напиток, то ваши способности к многозадачности и эффективность делают вас выдающимся лидером. Кроме того, вы точно знаете, как выполнить свою работу хорошо. И если речь заходит о вознаграждении за упорный труд, отдаете предпочтение чему-то легкому и сладкому. Иногда это просто латте, иногда — латте с сиропом. "
        result_image = 'https://agropererobka.com.ua/content/recipes/show/ice_late_tiramisu_1702561265.jpg'
        coffee_type = "latte"
    elif ('B1' in answers or 'D1' in answers) and ('A2' in answers or 'B2' in answers) and (
            'E3' in answers or 'C3' in answers or 'D3' in answers) and (
            'B5' in answers or 'E5' in answers or 'A5' in answers):
        result = "Ice-Latte!Если вы постоянно покупаете холодный кофе, порой добавляя в него карамель или взбитые сливки, то вы не боитесь быть законодателем мод. Вы всегда видите луч надежды в каждой ситуации, даже самой безвыходной. Вы любите пробовать что-то новое и иногда можете казаться беззаботным. В вашей жизни нет скучных моментов, а ваши воображение и непосредственность заставляют всех улыбаться. Вы, определенно, душа компании."
        result_image = 'https://cookhousediary.com/wp-content/uploads/2023/04/foamy-iced-oat-milk-latte-in-jar-cover.jpeg'
        coffee_type = "ice-latte"
    elif ('E1' in answers or 'D1' in answers or 'A1' in answers) and ('E2' in answers or 'B2' in answers) and (
            'B3' in answers or 'D3' in answers) and ('A5' in answers or 'D5' in answers or 'F5' in answers):
        result = "Раф! Да прибудет с вами сила. Несмотря на то, что раф мягкий и нежный, все равно он можем перетянуть вас со светлой стороны на темную. Тем не менее, вы индивидуальность, предпочитаете делать все в своем собственном темпе и верите в то, что сможете справиться с любыми ударами судьбы.Раф-кофе — выбор мягких, заботливых людей, которые любят радовать себя и окружающих уютными мелочами. Это те, кто ценит комфорт, тепло и романтику в повседневной жизни."
        result_image = 'https://www.cremashop.eu/content/www.crema.fi/media/recipe/raf-coffee/ingredients_7be4fbcfbcca29905a1ddc9288fe409a.jpeg'
        coffee_type = "raf"
    elif ('E1' in answers or 'C1' in answers or 'A1' in answers) and (
            'B2' in answers or 'A2' in answers or 'C2' in answers) and (
            'D3' in answers or 'C3' in answers or 'A3' in answers) and (
            'E5' in answers or 'F5' in answers or 'C5' in answers or 'D5' in answers or 'B5' in answers):
        result = "Флэт-уайт ваш напиток) Флэт-уайт любят те люди, которых часто называют самыми разумными среди друзей. К вам стекаются все знакомые, друзья и друзья друзей, когда им нужен дельный совет. Все знают, что вы голос разума и вряд ли сделаете что-то непрактичное. К тому же, вам нравится руководить, давать советы и делать людей счастливыми. Вы смягчаете резкость этой жизни, точно так же, как молоко смягчает шот эспрессо. Вы — особая, хорошо выверенная смесь. И по-настоящему разносторонний человек. Посмотрите на Хью Джекмана, он большой фанат такого напитка."
        result_image = 'https://images.arla.com/recordid/8763AA65-2EDD-4328-80C50FD4BB9B9EFE/picture.jpg?width=375&height=265&mode=crop&format=webp'
        coffee_type = "flat-white"
    elif ('B1' in answers or 'C1' in answers) and ('B2' in answers or 'C2' in answers) and (
            'C3' in answers or 'D3' in answers) and (
            'A5' in answers or 'D5' in answers or 'B5' in answers or 'E5' in answers):
        result = "Мокко выбирают люди, которые любят яркость и интенсивность в жизни. Они страстны, эмоциональны и не боятся проявлять свои чувства. Это те, кто всегда в поиске новых вкусов и эмоций, любят экспериментировать и обожают насыщенность жизни, как в шоколадно-кофейных сочетаниях мокки."
        result_image = 'https://images.immediate.co.uk/production/volatile/sites/2/2021/11/Mocha-1fc71f7.png?quality=90&resize=556,505'
        coffee_type = "mocha"
    else:
        result = "Ты уникален, попробуй разное и выбери свой вкус!"
        result_image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSSdp-A_xvjqcqDaN4KnjXTFVPDyRAVkYeqjQ&s'
        coffee_type = "unknown"

    user_coffee_choice[message.chat.id] = coffee_type
    bot.send_photo(message.chat.id, result_image)
    bot.send_message(message.chat.id, result)

    keyboard = types.InlineKeyboardMarkup()

    recipe_button = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    recipe_button.add(types.KeyboardButton("📜 Хочу рецепт!"))
    bot.send_message(message.chat.id, "Хочешь получить рецепт этого кофе?", reply_markup=recipe_button)
    del user_answers[message.chat.id]

def create_inline_keyboard(exclude_option=None):
        markup = types.InlineKeyboardMarkup(row_width=1)
        buttons = [
            types.InlineKeyboardButton(text="Пройти тест заново", callback_data="restart"),
            types.InlineKeyboardButton(text="Узнать интересные факты", callback_data="coffee_facts"),
            types.InlineKeyboardButton(text="Узнать особенности приготовления в разных странах",
                                       callback_data="coffee_countries")
        ]

        # Исключаем нажатую кнопку
        for button in buttons:
            if button.callback_data != exclude_option:
                markup.add(button)

        return markup


@bot.message_handler(func=lambda message: message.text == "📜 Хочу рецепт!")
def get_recipe(message):
    coffee_type = user_coffee_choice.get(message.chat.id, "unknown")
    recipe = coffee_recipes.get(coffee_type,
                                "Пока у нас нет точного рецепта для тебя, но попробуй экспериментировать с вкусами! 😉")

    # Отправляем рецепт
    bot.send_message(message.chat.id, recipe)
    bot.send_message(message.chat.id, "Что ещё хочешь узнать?", reply_markup=create_inline_keyboard())

coffee_facts_photo = "https://interesnyefakty.org/wp-content/uploads/Interesnye-fakty-o-kofe.jpg"
coffee_countries_photo = "https://coffee.spb.ru/upload/iblock/a7a/a7ad14bdb28b2eeac9b848d8add5231b.jpg"


# Обработчик inline-кнопки "coffee_facts"
@bot.callback_query_handler(func=lambda call: call.data == "coffee_facts")
def send_coffee_facts(call):
    facts = (
        "Интересные факты о кофе:\n"
        "❃ Американо – кофейный напиток, который появился во время Второй Мировой войны. Американские военные не могли пить европейский кофе из-за его крепости и просили разбавлять напиток водой.\n"
        "❃ Кофеин способствует снижению аппетита, ускоряет процесс расхода калорий и метаболизм в организме. \n"
        "❃ Кофейную гущу от молотого кофе женщины во всём мире добавляют в домашние скрабы и пилинги, поскольку кофеин отлично расщепляет жиры.\n"
        "❃ Кофе невероятно многогранен — ведь он содержит почти 800 ароматических соединений. Какая грань вкуса раскроется в вашей чашке, во многом зависит от обжарки. \n"
        "❃ Кофеин стимулирует центральную нервную систему, что может помочь уменьшить усталость, повысить бдительность и улучшить настроение. \n"
        "❃ Кофе официально запрещено Международным Олимпийским Комитетом. Если при проверке в крови спортсмена будет обнаружено свыше 12 микрограмм кофеина при расчете на литр, олимпиец будет снят с соревнований сразу. \n"
        "❃ Элементы, которые содержаться в кофе, благоприятно сказываются на зубной эмали, не давая бактериям оседать на ней. Благодаря этому кофеманы значительно реже обращаются к стоматологу. "
    )
    bot.send_message(call.message.chat.id, facts)
    bot.send_photo(call.message.chat.id, coffee_facts_photo, caption=facts)

    # Показываем оставшиеся кнопки (исключаем "coffee_facts")
    bot.send_message(call.message.chat.id, "Что ещё хочешь узнать?",
                     reply_markup=create_inline_keyboard(exclude_option="coffee_facts"))


# Обработчик inline-кнопки "coffee_countries"
@bot.callback_query_handler(func=lambda call: call.data == "coffee_countries")
def send_coffee_countries(call):
    countries = (
        "Особенности приготовления кофе в разных странах:\n"
        "Кафе де олла — «кофе в горшке» по-мексикански: Легко догадаться по названию, в чем особенность мексиканского напитка. Кафе де олла готовят в специальном глиняном горшке, добавляя тростниковый сахар и корицу или другие пряности — гвоздику, шоколад, анис, цедру лимона или апельсина.\n"
        "Крепкий кофе с кунжутом: подача по-мароккански: Деловые или дружеские встречи в Марокко редко обходятся без традиционного кофе. И он настолько крепок, что не каждый может выпить напиток, не разбавляя водой или молоком. Зато, если вас одолела жара, бодрящий эффект не заставит себя ждать.Еще одна отличительная черта кофе по-мароккански — его пряность. Напиток варят с кунжутом, имбирем, кардамоном, перцем или другими ароматными добавками.\n"
        "Кофейная церемония по-эфиопски: в Эфиопии — на родине любимого всеми напитка — ему принято посвящать целые кофейные церемонии. Процесс может длиться до 2-х часов.Варят напиток исключительно женщины. И используют для этого специальный глиняный кувшин — джебену. К кофе также добавляют сливочное масло, соль или мед.\n "
        "Кофе по-вьетнамски: для тех, кто любит послаще: Вьетнамцы заваривают кофе в пресс-фильтре. А перед приготовлением на дно чашки обязательно наливают сгущенку, которую они просто обожают. При желании также можно добавить лед.\n"
        "Согревающий кофе по-ирландски: Если быть точнее, это кофейный коктейль. Напиток включен в список Международной ассоциации барменов, и его состав неизменен: черный кофе, ирландский виски, коричневый сахар и взбитые сливки. Горячая смесь и то, что нужно, чтобы согреться сырой ирландской осенью.\n"
        "«Черный как ад, сильный как смерть, сладкий как любовь»: Турецкая поговорка прекрасно характеризует кофе, поданный в лучших национальных традициях: свежесваренный, крепкий, с восточными сладостями и часто со стаканом холодной воды.Прежде чем сделать первый глоток, рекомендуется немного подождать и дать осадку осесть на дне чашки. Его бывает достаточно много в напитке, приготовленном из свежемолотых кофейных зерен и в специальной посуде — турке.\n"
        "Фика: как пить кофе по-шведски: Шведский подход — полная противоположность концепции «кофе с собой». Фика — это не просто перерыв на кофе, а возможность остановиться на мгновение и прочувствовать настоящий момент.В Швеции официально разрешено делать такие перерывы во время рабочего дня каждые 2-3 часа. И главное правило фики — не обсуждать деловые вопросы."
    )
    bot.send_message(call.message.chat.id, countries)
    bot.send_photo(call.message.chat.id, coffee_countries_photo, caption=countries)
    # Показываем оставшиеся кнопки (исключаем "coffee_countries")
    bot.send_message(call.message.chat.id, "Что ещё хочешь узнать?",
                     reply_markup=create_inline_keyboard(exclude_option="coffee_countries"))


# Обработчик inline-кнопки "restart"
@bot.callback_query_handler(func=lambda call: call.data == "restart")
def restart_test(call):
    # Отправляем сообщение, как при команде /restart
    user_answers[call.message.chat.id] = []  # Очищаем ответы пользователя
    bot.send_message(
        call.message.chat.id,
        'Снова привет! Взглянем иначе на эти вопросы, готов?',
        reply_markup=create_reply_markup(['Конечно! Начнем'])
    )
    # Регистрируем следующий шаг
    bot.register_next_step_handler(call.message, on_1click)

bot.polling(none_stop=True)