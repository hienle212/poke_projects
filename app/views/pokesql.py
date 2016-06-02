-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema retake_python
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema retake_python
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `retake_python` DEFAULT CHARACTER SET utf8 ;
USE `retake_python` ;

-- -----------------------------------------------------
-- Table `retake_python`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retake_python`.`users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(45) NULL DEFAULT NULL,
  `alias` VARCHAR(45) NULL DEFAULT NULL,
  `email` VARCHAR(45) NULL DEFAULT NULL,
  `birthday` VARCHAR(45) NULL DEFAULT NULL,
  `password` VARCHAR(200) NULL DEFAULT NULL,
  `created_at` DATETIME NULL DEFAULT NULL,
  `updated_at` DATETIME NULL DEFAULT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8;


-- -----------------------------------------------------
-- Table `retake_python`.`pokes`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `retake_python`.`pokes` (
  `id` INT(11) NOT NULL AUTO_INCREMENT,
  `user_id` INT(11) NOT NULL,
  `poster_id` INT(11) NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_pokes_users_idx` (`user_id` ASC),
  INDEX `fk_pokes_users1_idx` (`poster_id` ASC),
  CONSTRAINT `fk_pokes_users`
    FOREIGN KEY (`user_id`)
    REFERENCES `retake_python`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_pokes_users1`
    FOREIGN KEY (`poster_id`)
    REFERENCES `retake_python`.`users` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB
AUTO_INCREMENT = 48
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
