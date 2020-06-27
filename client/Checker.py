class Checker:
    @staticmethod
    def check_reg(login: str, name: str, password: str):
        if login == '' or name == '' or password == '':
            return 'there are empty spaces'

        if len(login) < 5:
            return 'login is too short'
        if len(name) < 5:
            return 'name is too short'
        if len(password) < 6:
            return 'password is too short'

        if not login.isalnum() or not name.isalnum() or not password.isalnum():
            return 'there are invalid characters'

        return ''

    @staticmethod
    def check_auth(login: str, password: str):
        if login == '' or password == '':
            return 'there are empty spaces'

        if not login.isalnum() or not password.isalnum():
            return 'there are invalid characters'

        return ''

    @staticmethod
    def check_film(title: str, desc: str, year: str, actors: str, filmmaker: str):
        if title == '' or desc == '' or year == '' or actors == '' or filmmaker == '':
            return 'there are empty spaces'

        if len(desc) > 128:
            return 'description mustn\'t exceed 128 symbols'

        if len(actors) > 64:
            return 'too many actors'

        if len(filmmaker.strip().split(' ')) > 2 or len(filmmaker.split(',')) > 1:
            return 'there should be the only one filmmaker'

        if not year.isdigit():
            return 'wrong year'

        # 1900-2020 - possible
        if not int(year) in range(1900, 2021):
            return 'date is impossible'

        if title.find('&') != -1 or desc.find('&') != -1 or year.find('&') != -1 or actors.find('&') != -1 or filmmaker.find('&') != -1:
            return 'there are invalid symbols'

        return ''


print(Checker.check_film('title', 'desc desc desc', '2017', 'Elon Mask, Tim Cook', 'Bill Gates'))