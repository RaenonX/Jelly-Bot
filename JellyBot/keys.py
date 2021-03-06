# Cookies Keys
class Cookies:
    USER_TOKEN = "utoken"


# Session Keys
class Session:
    USER_ROOT_ID = "x-root-id"

    class APIStatisticsCollection:
        API_ACTION = "x-stats-api-action"
        DICT_PARAMS = "x-stats-param-dict"
        DICT_RESPONSE = "x-stats-resp-dict"
        SUCCESS = "x-stats-success"

        COLLECT = "x-stats-collect"


# Param Dict Prefix
class ParamDictPrefix:
    PostKey = "x-"  # Used in http POST params from HTML forms
