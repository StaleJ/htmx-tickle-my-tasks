CREATE TABLE TodoList(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    status INTEGER CHECK (status IN (0, 1)),
    due_date TEXT,
    priority TEXT
);
