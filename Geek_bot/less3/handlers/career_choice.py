from aiogram import types, F, Router
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import less3.keyboards.prof_keyboards

router = Router()

available_prof_names = ["Разработчик", "Аналитик", "Тестировщик", "UX-UI-дизайнер", "Веб-дизайнер", "Системный администратор", "Продакт-менеджер"]
available_prof_grades = ["Junior", "Middle", "Senior"]

average_salaries = {
    ("Разработчик", "Junior"): "от 50000 руб.",
    ("Разработчик", "Middle"): "от 80000 руб.",
    ("Разработчик", "Senior"): "от 120000 руб.",
    ("Аналитик", "Junior"): "от 45000 руб.",
    ("Аналитик", "Middle"): "от 70000 руб.",
    ("Аналитик", "Senior"): "от 100000 руб.",
    ("Тестировщик", "Junior"): "от 40000 руб.",
    ("Тестировщик", "Middle"): "от 60000 руб.",
    ("Тестировщик", "Senior"): "от 90000 руб.",
    ("UX-UI-дизайнер", "Junior"): "от 55000 руб.",
    ("UX-UI-дизайнер", "Middle"): "от 85000 руб.",
    ("UX-UI-дизайнер", "Senior"): "от 130000 руб.",
    ("Веб-дизайнер", "Junior"): "от 50000 руб.",
    ("Веб-дизайнер", "Middle"): "от 75000 руб.",
    ("Веб-дизайнер", "Senior"): "от 110000 руб.",
    ("Системный администратор", "Junior"): "от 45000 руб.",
    ("Системный администратор", "Middle"): "от 70000 руб.",
    ("Системный администратор", "Senior"): "от 100000 руб.",
    ("Продакт-менеджер", "Junior"): "от 60000 руб.",
    ("Продакт-менеджер", "Middle"): "от 90000 руб.",
    ("Продакт-менеджер", "Senior"): "от 130000 руб."
}

class ChoiceProfNames(StatesGroup):
    choice_prof_names = State()
    choice_prof_grades = State()

@router.message(Command('prof'))
async def cmd_prof(message: types.Message, state: FSMContext):
    name = message.chat.first_name
    await message.answer(f'Привет, {name}, выбери свою профессию', reply_markup=less3.keyboards.prof_keyboards.make_row_keyboard(available_prof_names))
    await state.set_state(ChoiceProfNames.choice_prof_names)

@router.message(ChoiceProfNames.choice_prof_names, F.text.in_(available_prof_names))
async def prof_chosen(message: types.Message, state: FSMContext):
    await state.update_data(chosen_prof=message.text.lower())
    await message.answer(text='Спасибо, теперь выбери свой уровень', reply_markup=less3.keyboards.prof_keyboards.make_row_keyboard(available_prof_grades))
    await state.set_state(ChoiceProfNames.choice_prof_grades)

@router.message(ChoiceProfNames.choice_prof_names)
async def prof_chosen_incorrectly(message: types.Message):
    await message.answer('Я не знаю такой профессии', reply_markup=less3.keyboards.prof_keyboards.make_row_keyboard(available_prof_names))

@router.message(ChoiceProfNames.choice_prof_grades, F.text.in_(available_prof_grades))
async def grade_chosen(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    prof = user_data.get("chosen_prof").capitalize()
    grade = message.text.capitalize()
    salary = average_salaries.get((prof, grade))
    if salary:
        await message.answer(f'Вы выбрали {grade} уровень. Ваша профессия {prof}. Средняя зарплата: {salary}', reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer('Извините, средняя зарплата для данной комбинации профессии и уровня не найдена.', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()
