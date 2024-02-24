from ..api.maimai import lxns


class MaiHandler:
    _mai_api_class = None  # 决策使用哪一个API
    _mai_api_token = None  # 传入的Token

    # 传入API类和Token
    def __init__(self, mai_api_class, mai_api_token):
        self._mai_api_class = mai_api_class
        self._mai_api_token = mai_api_token

    # 获取玩家信息，从LxAPI
    # todo:重构到使用图片渲染，应调用tool的方法。
    async def get_player_info_lxns(self, friend_code):
        data = await lxns.MaiApiLxns(self._mai_api_token).get_player_info(friend_code)
        print(data)
        name = data["data"]["name"]
        rating = data["data"]["rating"]

        reply = f"已获取到信息\n" f"名称：{name}\n" f"Rating：{rating}" ""

        return reply

    # 获取玩家最佳成绩，从LxAPI
    async def get_player_bests_lxns(self, friend_code):
        return await lxns.MaiApiLxns(self._mai_api_token).get_player_bests(friend_code)

    # 获取玩家最近成绩，从LxAPI
    async def get_player_recent_lxns(self, friend_code):
        return await lxns.MaiApiLxns(self._mai_api_token).get_player_recents(
            friend_code
        )

    # 获取玩家指定谱面进度，从LxAPI
    async def get_player_plate_progress_lxns(self, friend_code, plate_id):
        return await lxns.MaiApiLxns(self._mai_api_token).get_player_plate_progress(
            friend_code, plate_id
        )

    # 获取谱面列表，从LxAPI
    async def get_song_list_lxns(self):
        return await lxns.MaiApiLxns(self._mai_api_token).get_song_list()
