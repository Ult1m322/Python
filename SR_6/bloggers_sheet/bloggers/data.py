
class BloggerData:

    BLOGGERS = {
        'Wylsacom': {
            'id': 1,
            'name': 'Валентин',
            'category': 'Технології',
            'description': 'Огляди гаджетів та новини IT.',
            'social': {'youtube': 'link_yt_1', 'instagram': 'link_ig_1'},
            'publications': ['Останній огляд смартфону', 'Топ-5 програм'],
        },
        'mcodeg': {
            'id': 2,
            'name': 'Максим',
            'category': 'Програмування',
            'description': 'Пайтон розробник, фрілансер, блогер',
            'social': {'youtube': 'link_yt_2', 'telegram': 'link_tg_2'},
            'publications': ['Покращувач якості', 'Програма для підрахунку калорій'],
        },
        'mikola-prigorilskiy': {
            'id': 3,
            'name': 'Микола',
            'category': 'Економіка',
            'description': 'Блогер, що консультуе та розказує про бізнес',
            'social': {'telegram': 'link_tg_3'},
            'publications': ['Картини на металі', 'Помилки при веденні тт аккаунту '],
        }
    }

    @classmethod
    def get_all(cls):
        return list(cls.BLOGGERS.values())

    @classmethod
    def get_by_slug(cls, slug):
        return cls.BLOGGERS.get(slug)

    @classmethod
    def get_news(cls):
        return [
            {'id': 1, 'title': 'Новий телефон', 'slug': 'iphone17'},
            {'id': 2, 'title': 'Микола Пригорілський випустив книгу', 'slug': 'book'},
        ]