
-- lists all genres and there titles
-- List shows and genres
SELECT title
  FROM tv_shows
 WHERE tv_shows.title not in
       (SELECT ts.title
          FROM tv_genres AS tg
         INNER JOIN tv_show_genres AS tsg
            ON tg.id = tsg.genre_id
         RIGHT JOIN tv_shows AS ts
            ON ts.id = tsg.show_id
         WHERE tg.name LIKE "Comedy")
 ORDER BY title;

