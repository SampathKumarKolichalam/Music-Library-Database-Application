from bottle import Bottle, run, template, request, redirect
import sqlite3

app_project = Bottle()

# Connecting with SQLite database:-
conn_project = sqlite3.connect('music.db')
cursor_project = conn_project.cursor()

cursor_project.execute('''
    CREATE TABLE IF NOT EXISTS artist (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

cursor_project.execute('''
    CREATE TABLE IF NOT EXISTS song (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        album_id INTEGER,
        FOREIGN KEY (album_id) REFERENCES album(id)
    )
''')

conn_project.commit()
@app_project.route('/')
def start():
    return template('index_temp')


@app_project.route('/artist')
def artist_fun():
    cursor_project.execute('SELECT * FROM artist')
    artists_var = cursor_project.fetchall()
    return template('ar_table', artists=artists_var)


@app_project.route('/create/artist', method='GET')
def create_artist_form_fun():
    return template('cre_ar')

@app_project.route('/create/artist', method='POST')
def create_artist_fun():
    name_rf = request.forms.get('name')
    cursor_project.execute('INSERT INTO artist (name) VALUES (?)', (name_rf,))
    conn_project.commit()
    redirect('/')

@app_project.route('/update/artist/<artist_id>', method='GET')
def update_artist_form_fun(artist_id):
    cursor_project.execute('SELECT * FROM artist WHERE id = ?', (artist_id,))
    artist_uaf= cursor_project.fetchone()
    return template('upd_artist', artist=artist_uaf)

@app_project.route('/update/artist/<artist_id>', method='POST')
def update_artist_fun(artist_id):
    name_rfg= request.forms.get('name')
    cursor_project.execute('UPDATE artist SET name = ? WHERE id = ?', (name_rfg, artist_id))
    conn_project.commit()
    redirect('/')

@app_project.route('/delete/artist/<artist_id>', method='GET')
def delete_artist_form_fun(artist_id):
    cursor_project.execute('SELECT * FROM artist WHERE id = ?', (artist_id,))
    artist_daf = cursor_project.fetchone()
    return template('del_ar', artist=artist_daf)

@app_project.route('/delete/artist/<artist_id>', method='POST')
def delete_artist_fun(artist_id):
    cursor_project.execute('DELETE FROM artist WHERE id = ?', (artist_id,))
    conn_project.commit()
    redirect('/')


#SONGS:-
#Show SONGS:-
@app_project.route('/song')
def album_fun():
    cursor_project.execute('SELECT * FROM song')
    song_var= cursor_project.fetchall()
    return template('song_table', song=song_var)


@app_project.route('/create/song', method='GET')
def create_song_form_fun():
    return template('c_song', album_id=None)

@app_project.route('/create/song', method='POST')
def create_song_fun():
    title_var= request.forms.get('title')
    cursor_project.execute('INSERT INTO song (title) VALUES (?)', (title_var,))
    conn_project.commit()
    redirect('/')

@app_project.route('/update/song/<album_id:int>', method='GET')
def update_song_form_fun(album_id):
    cursor_project.execute('SELECT * FROM song WHERE id = ?', (album_id,))
    song_var= cursor_project.fetchone()
    if song_var:
        return template('upd_song', song=song_var)
    else:
        return "Song not found in playlist"

@app_project.route('/update/song/<album_id:int>', method='POST')
def update_song_fun(album_id):
    title_var= request.forms.get('title')
    cursor_project.execute('UPDATE song SET title = ? WHERE id = ?', (title_var, album_id))
    conn_project.commit()
    redirect('/')

@app_project.route('/delete/song/<album_id>', method='GET')
def delete_song_form_fun(album_id):
    cursor_project.execute('SELECT * FROM song WHERE id = ?', (album_id,))
    song_dsf= cursor_project.fetchone()
    return template('del_song', song=song_dsf)

@app_project.route('/delete/song/<album_id>', method='POST')
def delete_song_fun(album_id):
    cursor_project.execute('DELETE FROM song WHERE id = ?', (album_id,))
    conn_project.commit()
    redirect('/')

@app_project.route('/search/song', method='GET')
def search_song_fun():
    search_query_var= request.query.get('search_query', '').strip()
    cursor_project.execute('SELECT * FROM song WHERE title LIKE ?', ('%' + search_query_var + '%',))
    search_output = cursor_project.fetchall()
    return template('s_song', results=search_output)

# Running application:-
if __name__ == '__main__':
    run(app_project, host='localhost', port=8080)
