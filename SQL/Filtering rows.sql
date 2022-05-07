/*USING BETWEEN */
SELECT title, release_year
FROM films
WHERE release_year BETWEEN 1990 AND 2000
AND budget > 100000000
AND (language = 'Spanish' OR language = 'French');

/*WHERE IN
As you've seen, WHERE is very useful for filtering results. However, 
if you want to filter based on many conditions, 
WHERE can get unwieldy. For example:*/

SELECT title, release_year
FROM films
WHERE release_year in (1990, 2000)
AND duration > 120;

SELECT title, language
FROM films
WHERE language IN ('English', 'Spanish', 'French');

SELECT title, certification
FROM films
WHERE certification IN ('NC-17', 'R')
