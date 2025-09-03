from django.db import transaction
from django.utils import timezone

from .models import Player, Level, PlayerLevel, LevelPrize, PlayerPrize


def assign_prize_to_player(player: Player, level: Level):
    """
    Присваивает игроку приз за завершённый уровень
    """
    player_level = PlayerLevel.objects.filter(
        player=player,
        level=level,
        is_completed=True
    ).first()

    if not player_level:
        raise ValueError("Уровень не завершён игроком.")

    level_prizes = LevelPrize.objects.filter(level=level)

    with transaction.atomic():
        for level_prize in level_prizes:
            PlayerPrize.objects.get_or_create(
                player=player,
                level=level,
                prize=level_prize.prize,
                defaults={'received': timezone.now().date()}
            )
