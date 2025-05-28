CREATE TABLE tasks (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    subject TEXT NOT NULL,
    description TEXT,
    address TEXT,
    lat REAL NOT NULL,
    lng REAL NOT NULL,
    budget TEXT,
    deadline TEXT,
    status TEXT DEFAULT 'Open',
    posted_by TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);



INSERT INTO tasks (id, title, subject, description, address, lat, lng, budget, deadline, status, posted_by, user_id)
VALUES 
(1, 'Smart City Sensor Integration', 'History', 'A task related to history involving smart city sensor integration...', '165 Random St, Strathfield NSW 2032', -33.87248, 151.096679, '91-258', '4 days', 'Open', 'User1', 1),
(2, 'Gene Data Annotation', 'English', 'A task related to english involving gene data annotation...', '153 Random St, Rhodes NSW 2032', -33.828534, 151.089403, '150-340', '9 days', 'Open', 'User2', 2),
(3, 'Literature Review Automation', 'English', 'A task related to english involving literature review automation...', '106 Random St, Strathfield NSW 2032', -33.872552, 151.094384, '93-251', '9 days', 'Open', 'User3', 3),
(4, 'Math Proof Checker', 'Biology', 'A task related to biology involving math proof checker...', '235 Random St, Strathfield NSW 2032', -33.874807, 151.094675, '140-213', '5 days', 'Open', 'User4', 4);

SELECT * from tasks;