from typing import Any

from app.sdk.plugin import _PluginBase


class HelloPlugin(_PluginBase):
    """一个最小的 MoviePilot V3 插件。"""

    plugin_name = "Hello 插件"
    plugin_desc = "一个用于演示的 MoviePilot V3 插件。"
    plugin_icon = "Moviepilot_A.png"
    plugin_version = "1.0.0"
    plugin_author = "your-name"
    author_url = "https://github.com/your-name"

    plugin_config_prefix = "helloplugin_"
    plugin_order = 50
    auth_level = 1

    _enabled = False
    _message = "Hello MoviePilot"

    def init_plugin(self, config: dict | None = None) -> None:
        """插件启动或配置变更时调用。"""
        config = config or {}

        self._enabled = bool(config.get("enabled", False))
        self._message = str(
            config.get("message") or "Hello MoviePilot"
        )

    def get_state(self) -> bool:
        """返回插件是否启用。"""
        return self._enabled

    @staticmethod
    def get_command() -> list[dict[str, Any]]:
        """没有远程命令时返回空列表。"""
        return []

    def get_api(self) -> list[dict[str, Any]]:
        """没有 API 时返回空列表。"""
        return []

    def get_form(self) -> tuple[list[dict], dict[str, Any]]:
        """返回配置页面和默认配置。"""
        return [
            {
                "component": "VForm",
                "content": [
                    {
                        "component": "VSwitch",
                        "props": {
                            "model": "enabled",
                            "label": "启用插件",
                        },
                    },
                    {
                        "component": "VTextField",
                        "props": {
                            "model": "message",
                            "label": "展示文本",
                        },
                    },
                ],
            }
        ], {
            "enabled": False,
            "message": "Hello MoviePilot",
        }

    def get_page(self) -> list[dict]:
        """插件详情页。"""
        return [
            {
                "component": "VAlert",
                "props": {
                    "type": "info",
                    "variant": "tonal",
                    "text": self._message,
                },
            }
        ]

    def _save_config(self) -> bool:
        """保存当前配置。"""
        return self.update_config({
            "enabled": self._enabled,
            "message": self._message,
        })

    def stop_service(self) -> None:
        """停止插件并释放资源。"""
        self._enabled = False
