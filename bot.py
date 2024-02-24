import nonebot
from nonebot.adapters.onebot.v12 import Adapter as ONEBOT_V12Adapter

from nonebot.adapters.telegram import Adapter as TELEGRAMAdapter

from nonebot.adapters.qq import Adapter as QQAdapter

from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V12Adapter)

driver.register_adapter(TELEGRAMAdapter)

driver.register_adapter(QQAdapter)

driver.register_adapter(ONEBOT_V11Adapter)


nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run()
