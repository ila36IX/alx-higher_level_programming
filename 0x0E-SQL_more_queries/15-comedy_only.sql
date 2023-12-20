-- lists all comedy series
-- Only Comedy
SELECT ts.title AS title
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
       INNER JOIN tv_shows AS ts
       ON ts.id = tsg.show_id
 WHERE tg.name LIKE "Comedy"
 ORDER BY title;

