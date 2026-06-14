from src.game import Game
import asyncio
import pygame


async def main():
    game = Game()
    await game.run()

asyncio.run(main())
