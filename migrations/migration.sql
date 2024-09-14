CREATE DATABASE bairros_brasileiros;

CREATE TABLE locais (
    `id` INT UNSIGNED NOT NULL PRIMARY KEY,
    `local` VARCHAR(255),
    `parentalidade` INT UNSIGNED UNIQUE,
    `tipo_localidade` INT UNSIGNED UNIQUE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

ALTER TABLE locais ADD CONSTRAINT `parentalidade_id_constraint` FOREIGN KEY (`parentalidade`) REFERENCES locais (`id`);

CREATE TABLE tipos_locais (
    `id` INT UNSIGNED NOT NULL PRIMARY KEY,
    `tipo` VARCHAR(32)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;

ALTER TABLE `tipos_locais` ADD CONSTRAINT `tipos_locais_tipo_localidade_constraint` FOREIGN KEY (`tipo_localidade`) REFERENCES `locais` (`id`);
