import math


class AutoReply:
    MaxResponses = 5
    MaxContentLength = 2000
    TagSplittor = "|"
    CaseInsensitive = True


class Database:
    StatisticsExpirySeconds = 15811200  # 183 Days
    TokenActionExpirySeconds = 86400  # 24 Hrs
    CacheExpirySeconds = 172800  # 3 Days
    BulkWriteCount = 300

    class PopularityConfig:
        TimeDiffIntersectHr = 168
        TimeFunctionCoeff = 40

        AppearanceIntersect = 100
        AppearanceFunctionCoeff = 1.4
        AppearanceEquivalentWHr = 5

        TimeCoeffA = 2 * TimeDiffIntersectHr
        TimeCoeffB = -1 / TimeFunctionCoeff
        AppearanceCoeffA = 1 / math.pow(AppearanceIntersect, AppearanceFunctionCoeff - 1)


class DataQuery:
    TagPopularitySearchCount = 10


class ChannelConfig:
    VotesToPromoteMod = 7
    VotesToPromoteAdmin = 20


class Email:
    DefaultSubject = "Email Notification from Jelly BOT"
    DefaultPrefix = "Jelly BOT - "


class TokenAction:
    ChannelRegisterTokenCooldownSeconds = 60


class System:
    PingSpamWaitSeconds = 29 * 60  # 29 mins because Heroku sleep on 30 mins
