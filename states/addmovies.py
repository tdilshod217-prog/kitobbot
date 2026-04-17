from aiogram.fsm.state import StatesGroup,State

class AddMovies(StatesGroup):
    title=State()
    file_id=State()
    code=State()