from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(page, order_by='rating', order_direction='desc'):
    if order_by is None:
        order_by = 'rating'
    if order_direction is None:
        order_direction = 'desc'
    return data_manager.execute_select(
        f'''
        SELECT id, title, year, runtime, rating, trailer, homepage 
        FROM shows
        ORDER BY {order_by} {order_direction}
        LIMIT 15
        OFFSET ({page}-1)*15;
        '''
    )


def get_genres_from_show(show_id):
    return data_manager.execute_select(
        f"""
        SELECT genres.name, show_id
        FROM show_genres
        JOIN genres ON genres.id = genre_id
        WHERE show_id = {show_id}
        """
    )


def get_show_count():
    return data_manager.execute_select(
        f"""
        SELECT COUNT(*) AS show_count 
        FROM shows
        """
    )