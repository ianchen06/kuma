import faust

class Rating(faust.Record):
    ratable_id: str
    rater_id: str
    value: int
