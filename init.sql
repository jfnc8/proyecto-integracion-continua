CREATE DATABASE IF NOT EXISTS mi_base;
USE mi_base;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL
);

INSERT INTO usuarios (nombre, correo) VALUES
('Juan Perez', 'juan@ejemplo.com'),
('Maria Gomez', 'maria@ejemplo.com'),
('Carlos Ruiz', 'carlos@ejemplo.com');
