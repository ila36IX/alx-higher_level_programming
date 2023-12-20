-- ists all genres from hbtn_0d_tvshows..
-- and displays the number of shows linked to each
 SELECT tg.name        AS genre, 
        count(tg.name) AS number_of_shows
   FROM tv_show_genres AS tsg 
        INNER JOIN tv_genres AS tg
        ON tsg.genre_id = tg.id
  GROUP BY tg.name
 HAVING number_of_shows != 0
  ORDER BY number_of_shows DESC;
