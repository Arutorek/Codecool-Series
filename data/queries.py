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
        WHERE show_id = {show_id};
        """
    )


def get_show_count():
    return data_manager.execute_select(
        f"""
        SELECT COUNT(*) AS show_count 
        FROM shows;
        """
    )


def get_show_data(id):
    return data_manager.execute_select(
        f"""
        SELECT title, runtime, overview, trailer, rating
        FROM shows
        WHERE id = {id};
        """
    )


def get_show_actors(id):
    return data_manager.execute_select(
        f"""
        SELECT DISTINCT name
        FROM actors
        JOIN show_characters
        ON actors.id = show_characters.actor_id
        WHERE show_id = {id}
        LIMIT 3;
        """
    )


def get_seasons(id):
    return data_manager.execute_select(
        f"""
        SELECT season_number, title, overview
        FROM seasons
        WHERE {id} = show_id;
        """
    )


def get_100_actors():
    return data_manager.execute_select(
        f"""
        SELECT id, name
        FROM actors
        LIMIT 100;
        """
    )


def get_show_id_by_actor(actor_id):
    return data_manager.execute_select(
        f"""
        SELECT DISTINCT show_id, s.title
        FROM show_characters
        JOIN shows s on show_characters.show_id = s.id
        WHERE {actor_id} = actor_id;
        """
    )
