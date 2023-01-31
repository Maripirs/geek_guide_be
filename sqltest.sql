
-- GET ROUTE FOR HOME PAGE
SELECT g.id, g.name, i.image FROM geeks_game g JOIN geeks_image i ON g.image_id = i.id;

--GET ROUTE FOR GAME PAGE
-- SELECT g.name, s.type, s.content FROM geeks_game g JOIN geeks_image i ON g.image_id = i.id JOIN geeks_section s ON  s.game_id = g.id;


-- --CONDITIONAL ROUTE FOR GAME PAGE IF GAME HAS LEGEND
-- SELECT l.name, i.image, l.description FROM geeks_legend l JOIN geeks_image i ON l.image_id = i.id ORDER BY l.order