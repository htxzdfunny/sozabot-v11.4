from nonebot.plugin import PluginMetadata
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg

from nonebot import get_plugin_config

from .api.maimai.lxns import MaiApiLxns
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="sozabot-nb-core",
    description="This is a core nonebot plugin for sozabot.",
    usage="",
    config=Config,
)

from .handler.maimai_handler import MaiHandler

plugin_config = get_plugin_config(Config)

# region 指令
# maimai指令
mai_get_player_info = on_command("mai", priority=5)
mai_get_song_list = on_command("", priority=5)


# endregion

# region 指令处理
# 获取mai玩家信息
@mai_get_player_info.handle()
async def handle_mai_get_player_info(args: Message = CommandArg()):
    # todo: 去除直接调用子方法，而应该让handler处理
    mai = MaiHandler("", plugin_config.sozabot_mai_lxns_api_token)
    reply = await mai.get_player_info_lxns(args.extract_plain_text())
    await mai_get_player_info.finish(reply)


# 获取mai歌曲列表
# todo:修改到handler，而不是直接调用api
@mai_get_song_list.handle()
async def handle_mai_get_song_list():
    mai = MaiApiLxns(plugin_config.sozabot_mai_lxns_api_token)
    reply = await mai.get_song_list()
    await mai_get_song_list.finish(reply)


# endregion
