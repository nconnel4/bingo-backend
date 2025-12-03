from uuid import UUID

from bingo_backend.card.models import Card
from bingo_backend.cardspace.models import CardSpace
from bingo_backend.cardspace.services import get_card_spaces_by_card_id, get_card_space
from bingo_backend.bingo.utils.bingohelper import check_has_bingo
from bingo_backend.bingo.services import get_bingo_gif
from bingo_backend.card.services import get_card_by_id
from bingo_backend.database.redis import redis
from bingo_backend.notification.dtos import NotificationMessage


async def check_bingo(*, session, space_id: UUID):
    card_space = get_card_space(session=session, space_id=space_id)

    if card_space.is_complete:
        card_spaces: list[CardSpace] = get_card_spaces_by_card_id(session=session, card_id=card_space.card_id)
        card: Card = get_card_by_id(session=session, card_id=card_space.card_id)

        complete_spaces = [space.position for space in card_spaces if space.is_complete]

        has_bingo, remaining_spaces = check_has_bingo(complete_spaces, card_space.position)
        notification = None

        if has_bingo:
            gif = get_bingo_gif(session=session)
            notification = NotificationMessage(event="bingo", message=f"{card.user} has bingo!", link=gif.link, description=gif.description)
        elif remaining_spaces <= 1:
            notification = NotificationMessage(event="message", message=f"⚠ {card.user} has {remaining_spaces} remaining space!")


        if notification:
            await redis.publish("notifications", notification.model_dump_json())
