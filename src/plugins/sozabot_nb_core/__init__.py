from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from nonebot import on_command

from .config import Config

__plugin_meta__ = PluginMetadata(
    name="sozabot-nb-core",
    description="This is a core nonebot plugin for sozabot.",
    usage="",
    config=Config,
)

config = get_plugin_config(Config)

