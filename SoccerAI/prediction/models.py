from django.db import models

class Matches(models.Model):
    Date = models.DateField('Дата')
    Country = models.CharField('Страна', max_length=50)
    Tournament = models.CharField('Турнир', max_length=50)
    Time = models.TimeField('Время')
    Teams = models.CharField('Команды', max_length=100)
    PreviewLink = models.URLField('Ссылка на матч')
    HomeTeam = models.CharField('Хозяева', max_length=50)
    AwayTeam = models.CharField('Гости', max_length=50)
    HomeHref = models.URLField('Ссылка на Хозяев')
    AwayHref = models.URLField('Ссылка на Гостей')
    HTRating = models.FloatField('Рейтинг Хозяев')
    ATRating = models.FloatField('Рейтинг Гостей')
    HTAR = models.FloatField('Рейтинг Атаки Хозяев')
    ATAR = models.FloatField('Рейтинг Атаки Гостей')
    HTMR = models.FloatField('Рейтинг Полузащиты Хозяев')
    ATMR = models.FloatField('Рейтинг Полузащиты Гостей')
    HTDR = models.FloatField('Рейтинг Защиты Хозяев')
    ATDR = models.FloatField('Рейтинг Защиты Гостей')
    HTMGS = models.FloatField('Забитые голы Хозяев (среднее)')
    ATMGS = models.FloatField('Забитые голы Гостей (среднее)')
    HTMGC = models.FloatField('Пропущенные голы Хозяев (среднее)')
    ATMGC = models.FloatField('Пропущенные голы Гостей (среднее)')
    HomeGoalDif = models.FloatField('Разница з/п голов Хозяев')
    AwayGoalDif = models.FloatField('Разница з/п голов Гостей')
    HTMatches = models.IntegerField('Кол-во матчей Хозяев')
    ATMatches = models.IntegerField('Кол-во матчей Гостей')
    HTLastMatches = models.CharField('Последние матчи Хозяев', max_length=50)
    ATLastMatches = models.CharField('Последние матчи Гостей', max_length=50)
    HTPoints = models.FloatField('Очки Хозяев за последние матчи')
    ATPoints = models.FloatField('Очки Гостей за последние матчи')
    AvgCH = models.FloatField('1')
    AvgCD = models.FloatField('X')
    AvgCA = models.FloatField('2')
    DoubleChanceHD = models.FloatField('1X')
    DoubleChanceHA = models.FloatField('12')
    DoubleChanceAD = models.FloatField('X2')
    HomeProb = models.FloatField('1 Вероятность')
    DrawProb = models.FloatField('X Вероятность')
    AwayProb = models.FloatField('2 Вероятность')
    HD_Prob = models.FloatField('1X Вероятность')
    HA_Prob = models.FloatField('12 Вероятность')
    AD_Prob = models.FloatField('X2 Вероятность')
    WhoScoredDifference = models.IntegerField('Разница мячей в прогнозе WhoScored')
    WhoScoredPrediction = models.CharField('Пронгоз WhoScored', max_length=20)
    Prediction = models.CharField('Прогноз', max_length=20)
    ExpressPrediction = models.CharField('Пронгоз для Экспресс-пула', max_length=20)
    Result = models.CharField('Результат матча', max_length=20)
    
    def __str__(self):
        return self.Teams
    
    class Meta:
        verbose_name = 'Матч'
        verbose_name_plural = 'Матчи'
    