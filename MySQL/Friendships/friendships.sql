SELECT u.first_name AS first_name, u.last_name AS last_name, user2.first_name AS friend_first_name, user2.last_name AS friend_last_name 
FROM users AS u
LEFT JOIN friendships AS f 
ON u.id = f.friend_id
LEFT JOIN users AS user2 
ON user2.id = f.user_id
ORDER BY friend_last_name DESC;