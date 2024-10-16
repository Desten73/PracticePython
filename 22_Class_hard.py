from time import sleep

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return "".join(self.nickname)


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user
                print("Вы успешно вошли в UrTube!")
                break
        print("Вход не успешен!")

    def register(self, nickname, password, age):
        if nickname in self.users:
            print(f"Пользователь {nickname} уже существует!")
        else:
            self.current_user = User(nickname, password, age)
            self.users.append(self.current_user)

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        for vi in video:
            if vi not in self.videos:
                self.videos.append(vi)

    def get_videos(self, find_word):
        res = []
        for video in self.videos:
            if find_word.lower() in video.title.lower():
                res.append(video.title)
        return res

    def watch_video(self, video_name):
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео!")
            return
        for video in self.videos:
            if video.title == video_name:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу!")
                    return
                for i in range(video.duration):
                    print(i+1, end=" ")
                    sleep(1)
                print("Конец видео!")
                return
        print("Видео не найдено!")


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
