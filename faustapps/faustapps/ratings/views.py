from faustapps.app import app
from .models import Rating
from .agents import ratings_sum, ratings_cnt

@app.page('/count/{ratable_id}/')
@app.table_route(table=ratings_cnt, match_info='ratable_id')
async def get_cnt(web, request, ratable_id):
    return web.json({
        ratable_id: ratings_cnt[ratable_id],
    })

@app.page('/sum/{ratable_id}/')
@app.table_route(table=ratings_sum, match_info='ratable_id')
async def get_sum(web, request, ratable_id):
    return web.json({
        ratable_id: ratings_sum[ratable_id],
    })
