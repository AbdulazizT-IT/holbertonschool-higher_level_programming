-- lists all cities contained in the database

SELECT id, name, name
FROM states
INNER JOIN cities ON cities.state_id = states.id;