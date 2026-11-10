
CREATE DATABASE IF NOT EXISTS proyecto;

USE proyecto;

CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(150) NOT NULL
);

INSERT INTO usuarios (nombre, correo)
VALUES
('Usuario Prueba 1', 'usuario1@example.com'),
('Usuario Prueba 2', 'usuario2@example.com');

