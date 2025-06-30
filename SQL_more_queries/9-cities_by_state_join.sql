-- lists all cities contained in the database

SELECT id, name, name
FROM states
INNER JOIN cities ON states.state_id = cities.id;