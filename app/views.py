import csv
from django.http import StreamingHttpResponse
from .models import PlayerLevel, LevelPrize


class Echo:
    """
    Псевдо-буфер, который реализует метод write() и сразу возвращает строку.
    Используется для передачи данных построчно в StreamingHttpResponse.
    """
    def write(self, value):
        return value


def export_player_level_data_csv(request):
    """
    экспортирует CSV с данными об уровнях игроков и призах.
    """

    queryset = PlayerLevel.objects.select_related('player', 'level').iterator()

    def row_generator():
        yield ['player_id', 'level_title', 'is_completed', 'prizes']

        for player_level in queryset:
            prizes = LevelPrize.objects.filter(level=player_level.level)
            prize_titles = [p.prize.title for p in prizes if p.received]

            yield [
                player_level.player.player_id,
                player_level.level.title,
                'Yes' if player_level.is_completed else 'No',
                ', '.join(prize_titles) or '—'
            ]

    pseudo_buffer = Echo()
    writer = csv.writer(pseudo_buffer)

    response = StreamingHttpResponse(
        (writer.writerow(row) for row in row_generator()),
        content_type="text/csv"
    )
    response['Content-Disposition'] = 'attachment; filename="player_levels.csv"'
    return response
