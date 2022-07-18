from typing import Callable

from fastapi import FastAPI
from loguru import logger

from src.core.settings.app import AppSettings


def create_start_app_handler(
    app: FastAPI,
    settings: AppSettings,
) -> Callable:  # type: ignore
    async def start_app() -> None:
        # NOTE: DB接続処理を書く
        pass

    return start_app


def create_stop_app_handler(app: FastAPI) -> Callable:  # type: ignore
    @logger.catch
    async def stop_app() -> None:
        # NOTE: DB切断処理を書く
        pass

    return stop_app
