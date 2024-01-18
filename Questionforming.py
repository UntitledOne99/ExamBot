import random

from aiogram import types

class Form:

    def __init__(self, question: str, id: str, answer: list):
        self.question = question
        self.answer = answer
        self.id = id
        random.shuffle(self.answer)

    def make_a_question(self, builder):
        x = []
        for i in range(len(self.answer)):
            y = builder.add(types.InlineKeyboardButton(
                text=f"{self.answer[i]}",
                callback_data=f"{self.answer[i]} {self.id}"))
            x.append(y)
        return x
