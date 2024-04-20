from dataclasses import dataclass

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
    headers = {}

    # 初始化
    """
    :param token: API Token from maimai.lxns.net
    """

    def __init__(self, token):
        self._token = token
        self.update_headers()

    # 更新请求头
    def update_headers(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (compatible; MyClientApp/1.0)",
            "Authorization": self._token,
        }

    # 获取玩家信息
    """
    :param friend_code: 玩家好友码
    :return: 玩家信息
    """

    async def get_player_info(self, friend_code):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}"
        response = requests.get(url, headers=self.headers)
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

    async def get_player_bests(self, friend_code):

        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/bests"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 上传玩家成绩
    """
    :param friend_code: 玩家好友码
    :param scores: 玩家成绩
    :return: 成功返回 True，失败返回 False
    """

    async def upload_player_scores(self, friend_code, scores):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/scores"
        data = {"scores": scores}
        response = requests.post(url, headers=self.headers, json=data)
        if response.status_code == 200:
            return True
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 获取玩家 Recent 50
    """
    :param friend_code: 玩家好友码
    :return: 玩家 Recent 50
    """

    async def get_player_recents(self, friend_code):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/recents"
        response = requests.get(url, headers=self.headers)
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

    async def get_player_plate_progress(self, friend_code, plate_id):
        url = f"{self.API_URL}/v0/maimai/player/{friend_code}/plate/{plate_id}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")

    # 获取歌曲列表
    async def get_song_list(self):
        url = f"{self.API_URL}/v0/maimai/song/list"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            data = json.loads(response.content)
            return data
        else:
            raise RuntimeError(f"请求失败：{response.status_code}")


# todo: 这里需要测试，请到 get_player_bests 测试
@dataclass
class _Score:
    id: int
    song_name: str
    level: str
    level_index: str
    achievements: float
    fc: str
    fs: str
    dx_score: int
    dx_rating: float
    rate: str
    type: str
    play_time: str
    upload_time: str
