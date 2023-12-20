-- lists all genres of the show Dexter
-- DEXTER
SELECT tg.name AS name
  FROM tv_genres AS tg
       INNER JOIN tv_show_genres AS tsg
       ON tg.id = tsg.genre_id
       INNER JOIN tv_shows AS ts
       ON ts.id = tsg.show_id
 WHERE ts.title LIKE "DEXTER"
 ORDER BY name;

