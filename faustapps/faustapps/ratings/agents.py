from faustapps.app import app
from .models import Rating

ratings_topic = app.topic('ratings', value_type=Rating)

ratings_sum = app.Table('ratings_sum', default=int)
ratings_cnt = app.Table('ratings_cnt', default=int)

@app.agent(ratings_topic)
async def rate(ratings):
    async for rating in ratings.group_by(Rating.ratable_id):
        print(rating)
        ratings_cnt[rating.ratable_id] += 1
        ratings_sum[rating.ratable_id] += rating.value
        print("[%s]ratings_cnt: %s, ratings_sum: %s"%(rating.ratable_id, ratings_cnt[rating.ratable_id],
            ratings_sum[rating.ratable_id]))
