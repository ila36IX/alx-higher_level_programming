-- lists all genres and there titles
-- List shows and genres
SELECT ts.title AS title, tg.name AS name
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
       RIGHT JOIN tv_shows AS ts
       ON ts.id = tsg.show_id
 ORDER BY title, name;

