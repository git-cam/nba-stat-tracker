# In your Django app directory, create a folder named 'management' if it doesn't exist
# Inside 'management', create a folder named 'commands'
# Inside 'commands', create a Python file (e.g., update_nba_stats.py)

# update_nba_stats.py
from django.core.management.base import BaseCommand
import requests
from models import Player, Season, PlayerSeasonStat # Import your model

class Command(BaseCommand):
    help = 'Update NBA stats from the NBA Stats API'

    def handle(self, *args, **kwargs):
        # Make API call to NBA Stats API
        url = 'https://api.nba.com/stats/your_endpoint'
        headers = {'Authorization': 'Bearer YOUR_API_KEY'}
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # API call successful, process data and update database
            data = response.json()

            for item in data['results']:
                # Process data and update database
                nba_stat = NBAStat.objects.get_or_create(
                    player_name=item['player_name'],
                    defaults={
                        'points': item['points'],
                        'assists': item['assists'],
                        # Add more fields as needed
                    }
                )
                if not nba_stat[1]:  # Check if the record already existed
                    nba_stat[0].points = item['points']
                    nba_stat[0].assists = item['assists']
                    # Update more fields as needed
                    nba_stat[0].save()

            self.stdout.write(self.style.SUCCESS('Successfully updated NBA stats'))
        else:
            # API call failed
            self.stdout.write(self.style.ERROR('Failed to update NBA stats. Status code: {}'.format(response.status_code)))
