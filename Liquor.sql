-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Liquor
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Liquor
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Liquor` DEFAULT CHARACTER SET utf8 ;
USE `Liquor` ;

-- -----------------------------------------------------
-- Table `Liquor`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `nickname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `liquor_name` VARCHAR(100) NOT NULL,
  `alcohol` FLOAT NULL,
  `price` INT NULL,
  `image_path` VARCHAR(100) NULL,
  `description` VARCHAR(500) NOT NULL,
  `vendor` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cocktail_name` VARCHAR(100) NOT NULL,
  `alcohol` FLOAT NULL,
  `ingredients` VARCHAR(100) NOT NULL,
  `recipe` VARCHAR(500) NOT NULL,
  `heart` INT NOT NULL DEFAULT 0,
  `image_path` VARCHAR(100) NULL,
  `level` FLOAT NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`review` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `liquor_id` INT NOT NULL,
  `rating` FLOAT NOT NULL,
  `content` VARCHAR(200) NOT NULL,
  `review_date` DATE NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_review_user_idx` (`user_id` ASC),
  INDEX `fk_review_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_review_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_review_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`by_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`by_liquor` (
  `cocktail_id` INT NOT NULL AUTO_INCREMENT,
  `liquor_id` INT NOT NULL,
  PRIMARY KEY (`cocktail_id`, `liquor_id`),
  INDEX `fk_by_liquor_cocktail_idx` (`cocktail_id` ASC),
  INDEX `fk_by_liquor_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_by_liquor_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_by_liquor_cocktail`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`menu` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `menu_name` VARCHAR(50) NOT NULL,
  `image_path` VARCHAR(100) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`paring`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`paring` (
  `liquor_id` INT NOT NULL,
  `menu_id` INT NOT NULL,
  PRIMARY KEY (`liquor_id`, `menu_id`),
  INDEX `fk_paring_menu_idx` (`menu_id` ASC),
  INDEX `fk_paring_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_paring_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_paring_menu`
    FOREIGN KEY (`menu_id`)
    REFERENCES `Liquor`.`menu` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`wishlist_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`wishlist_liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `liquor_id` INT NOT NULL,
  INDEX `fk_wishlist_liquor_user_idx` (`user_id` ASC),
  PRIMARY KEY (`id`),
  INDEX `fk_wishlist_liquor_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_wishlist_l_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wishlist_l_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor`.`liquor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`done_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`done_liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `liquor_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_done_liquor_user_idx` (`user_id` ASC),
  INDEX `fk_doen_liquor_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_done_l_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor`.`user` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_done_l_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor`.`liquor` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`wishlist_cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`wishlist_cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `cocktail_id` INT NOT NULL,
  INDEX `fk_wishlist_cocktail_user_idx` (`user_id` ASC),
  PRIMARY KEY (`id`),
  INDEX `fk_wishlist_cocktail_cocktail_idx` (`cocktail_id` ASC),
  CONSTRAINT `fk_wishlist_c_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wishlist_c_liquor`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor`.`done_cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor`.`done_cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `user_id` INT NOT NULL,
  `cocktail_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_done_cocktail_user_idx` (`user_id` ASC),
  INDEX `fk_done_cocktail_cocktail_idx` (`cocktail_id` ASC),
  CONSTRAINT `fk_done_c_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_done_c_liquor`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
