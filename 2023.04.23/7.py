inp = input()
# ИСПОЛЬЗОВАТЬ: круглые скобки вокруг строкового литерала не нужны
print(''.join(_ for _ in inp if _ not in '''.,:;!?–—\'\"()*/'''))

# КОММЕНТАРИЙ: то есть вы всё же знаете, как работают генераторные выражения? что тогда мешало применить их в предыдущей задаче?


# C:\Users\user\Desktop\Учеба\Python\Rozdjalovskij\2023.04.23>py 7.py
# Было темно в гостиной. Лаптев, не садясь и держа шляпу в руках, стал извиняться за беспокойство; он спросил, что делать, чтобы сестра спала по ночам, и отчего она так страшно худеет, и его смущала мысль, что, кажется, эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита.
# Было темно в гостиной Лаптев не садясь и держа шляпу в руках стал извиняться за беспокойство он спросил что делать чтобы сестра спала по ночам и отчего она так страшно худеет и его смущала мысль что кажется эти самые вопросы он уже задавал доктору сегодня во время его утреннего визита


# ИТОГ: отлично — 3/3
