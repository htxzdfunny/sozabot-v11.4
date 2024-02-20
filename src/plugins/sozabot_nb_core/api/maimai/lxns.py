import requests
import json


class MaiApiLxns:
    """
    Maimai.LXNS API Python SDK
    @author chitsanfei soyorin@outlook.com
    """

    # API 地址
    API_URL = "https://maimai.lxns.net/api"

    _token = ""

    # 请求头
    # todo: 记得删除token，并改为从外部的config传入
    HEADERS = {"Authorization": _token}

    # 初始化
    """
    :param token: API Token from maimai.lxns.net
    """

    def __init__(self, token):
        self._token = token

    # 获取玩家信息
    """
    :param friend_code: 玩家好友码
    :return: 玩家信息
    """

    def get_player_info(self, friend_code):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 获取玩家 Best 50
    """
    :param friend_code: 玩家好友码
    :return: 玩家 Best 50
    """

    def get_player_bests(self, friend_code):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/bests"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data["data"]
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 上传玩家成绩
    """
    :param friend_code: 玩家好友码
    :param scores: 玩家成绩
    :return: 成功返回 True，失败返回 False
    """

    def upload_player_scores(self, friend_code, scores):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/scores"
        data = {"scores": scores}
        response = requests.post(url, headers=self.HEADERS, json=data)
        if response.status_code == 200:
            return True
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 获取玩家 Recent 50
    """
    :param friend_code: 玩家好友码
    :return: 玩家 Recent 50
    """

    def get_player_recents(self, friend_code):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/recents"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 获取玩家姓名框进度
    """
    :param friend_code: 玩家好友码
    :param plate_id: 姓名框 ID
    :return: 玩家姓名框进度
    """

    def get_player_plate_progress(self, friend_code, plate_id):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/plate/{plate_id}"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    def get_song_list(self):
        url = f"{self.API_URL}/v0/maimai/song/list"
        response = requests.get(url, headers=self.HEADERS)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")


# region

# 使用示例
# friend_code = 123456789

# # 获取玩家信息
# player_info = get_player_info(friend_code)
# print(player_info)

# # 获取玩家 Best 50
# player_bests = get_player_bests(friend_code)
# print(player_bests)

# # 上传玩家成绩
# scores = [
#     {
#         "id": 834,
#         "type": "standard",
#         "level_index": 4,
#         "achievements": 101,
#         "fc": None,
#         "fs": None,
#         "dx_score": 0,
#         "play_time": "2023-12-31T16:00:00Z",
#     },
# ]
# upload_player_scores(friend_code, scores)

# # 获取玩家 Recent 50
# player_recents = get_player_recents(friend_code)
# print(player_recents)

# # 获取玩家姓名框进度
# plate_progress = get_player_plate_progress(friend_code, 1)
# print(plate_progress)

# # 获取曲目列表
# todo: 记得测试完把这里删了
if __name__ == "__main__":
    MaiApiLxns = MaiApiLxns("")  # API Token
    result = MaiApiLxns.get_song_list()
    print(result)


# endregion


class _Score:
    def __init__(
        self,
        id: int,
        type_: str,
        level_index: int,
        achievements: int,
        dx_score: int,
        play_time: str,
        fc: object = None,
        fs: object = None,
    ):
        self.id = id
        self.type = type_
        self.level_index = level_index
        self.achievements = achievements
        self.fc = fc
        self.fs = fs
        self.dx_score = dx_score
        self.play_time = play_time


def process_scores(scores_data):
    scores_template = [
        _Score(
            id=item["id"],
            type_=item["type"],
            level_index=item["level_index"],
            achievements=item["achievements"],
            dx_score=item["dx_score"],
            play_time=item["play_time"],
            fc=item.get("fc"),
            fs=item.get("fs"),
        )
        for item in scores_data
    ]

    return scores_template if scores_data else []


# 示例数据
# scores = [
#     {
#         "id": 834,
#         "type": "standard",
#         "level_index": 4,
#         "achievements": 101,
#         "dx_score": 0,
#         "play_time": "2023-12-31T16:00:00Z",
#     },
# ]
#
# # 使用示例
# scores_instances = process_scores(scores)
#
# for score in scores_instances:
#     print(score.__dict__)
