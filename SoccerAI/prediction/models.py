from django.db import models

class Matches(models.Model):
    Date = models.DateField('Дата')
    Country = models.CharField('Страна')
    Tournament = models.CharField('Турнир')
    Time = models.TimeField('Время')
    Teams = models.CharField('Команды')
    PreviewLink = models.URLField('Ссылка на матч')
    HomeTeam = models.CharField('Хозяева')
    AwayTeam = models.CharField('Гости')
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
    HTLastMatches = models.CharField('Последние матчи Хозяев')
    ATLastMatches = models.CharField('Последние матчи Гостей')
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
    WhoScoredPrediction = models.CharField('Пронгоз WhoScored')
    Prediction = models.CharField('Прогноз')
    ExpressPrediction = models.CharField('Пронгоз для Экспресс-пула')
    Result = models.CharField('Результат матча')
    
    def __str__(self):
        return self.Teams
    