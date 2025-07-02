import requests
import os
from dotenv import load_dotenv
from app import create_app, db
from app.models import Event

load_dotenv()
app = create_app()

api_key = os.getenv("API_KEY")
url = "https://app.ticketmaster.com/discovery/v2/events.json"

params = {
    "apikey": api_key,
    "size": 200,
    "countryCode": "IN"  # You can change this for variety
}

response = requests.get(url, params=params)
data = response.json()
events = data.get('_embedded', {}).get('events', [])

with app.app_context():
    for event in events:
        event_id = event.get('id')
        name = event.get('name')
        image = event.get('images', [{}])[0].get('url')

        venue = event.get('_embedded', {}).get('venues', [{}])[0]
        address = venue.get('address', {}).get('line1', 'N/A')
        city = venue.get('city', {}).get('name', 'N/A')
        state = venue.get('state', {}).get('name', 'N/A')

        date = event.get('dates', {}).get('start', {}).get('localDate')
        time = event.get('dates', {}).get('start', {}).get('localTime')

        info = event.get('info')
        if not info:
            info = event.get('pleaseNote', 'No info available.')

        # ✅ Handle price range correctly
        price_data = event.get('priceRanges')
        if price_data and isinstance(price_data, list):
            first_price = price_data[0]
            min_price = first_price.get('min')
            max_price = first_price.get('max')
            currency = first_price.get('currency', '$')

            if isinstance(min_price, (int, float)) and isinstance(max_price, (int, float)):
                price = f"{currency} {min_price:.2f} - {max_price:.2f}"
            else:
                price = "Not Available"
        else:
            price = "Not Available"

        # ✅ Get broader genre segment
        genre = (
            event.get('classifications', [{}])[0]
            .get('segment', {})
            .get('name', 'Other')
        )

        existing = Event.query.get(event_id)
        if not existing:
            new_event = Event(
                id=event_id,
                name=name,
                image=image,
                address=address,
                city=city,
                state=state,
                date=date,
                time=time,
                info=info,
                price_range=price,
                genre=genre
            )
            db.session.add(new_event)

    db.session.commit()
    print("✅ Events saved to database.")
