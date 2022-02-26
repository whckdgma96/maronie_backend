-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema Liquor_dev
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema Liquor_dev
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `Liquor_dev` DEFAULT CHARACTER SET utf8 ;
USE `Liquor_dev` ;

-- -----------------------------------------------------
-- Table `Liquor_dev`.`user`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`user` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `email` VARCHAR(100) NOT NULL,
  `password` VARCHAR(256) NOT NULL,
  `nickname` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `email_UNIQUE` (`email` ASC))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`classification`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`classification` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `classification` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `liquor_name` VARCHAR(100) NOT NULL,
  `classification_id` INT NOT NULL,
  `alcohol` FLOAT NULL,
  `price` INT NULL,
  `image_path` VARCHAR(256) NULL,
  `description` VARCHAR(500) NOT NULL,
  `vendor` VARCHAR(256) NULL,
  `rating` FLOAT NOT NULL DEFAULT 0,
  PRIMARY KEY (`id`),
  INDEX `fk_classification_idx` (`classification_id` ASC) VISIBLE,
  CONSTRAINT `fk_liquor_classification`
    FOREIGN KEY (`classification_id`)
    REFERENCES `Liquor_dev`.`classification` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cocktail_name` VARCHAR(100) NOT NULL,
  `alcohol` FLOAT NULL,
  `ingredients` VARCHAR(100) NOT NULL,
  `recipe` VARCHAR(500) NOT NULL,
  `heart` INT NOT NULL DEFAULT 0,
  `image_path` VARCHAR(256) NULL,
  `level` FLOAT NOT NULL,
  `description` VARCHAR(500) NOT NULL,
  `author_id` INT NOT NULL DEFAULT 1,
  PRIMARY KEY (`id`),
  INDEX `fk_cocktail_user_idx` (`author_id` ASC) VISIBLE,
  CONSTRAINT `fk_cocktail_user`
    FOREIGN KEY (`author_id`)
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;

-- -----------------------------------------------------
-- Table `Liquor_dev`.`review`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`review` (
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
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_review_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor_dev`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`menu`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`menu` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `menu_name` VARCHAR(50) NOT NULL,
  `image_path` VARCHAR(256) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`by_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`by_liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `classification_id` INT NOT NULL,
  `cocktail_id` INT NOT NULL,
  INDEX `fk_by_l_classification_idx` (`classification_id` ASC),
  INDEX `fk_by_l_cocktail_idx` (`cocktail_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_by_l_cocktail`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor_dev`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_by_l_classification`
    FOREIGN KEY (`classification_id`)
    REFERENCES `Liquor_dev`.`classification` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`paring`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`paring` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `menu_id` INT NOT NULL,
  `classification_id` INT NOT NULL,
  INDEX `fk_paring_classification_idx` (`classification_id` ASC),
  INDEX `fk_paring_menu_idx` (`menu_id` ASC),
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_paring_menu`
    FOREIGN KEY (`menu_id`)
    REFERENCES `Liquor_dev`.`menu` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_paring_classification`
    FOREIGN KEY (`classification_id`)
    REFERENCES `Liquor_dev`.`classification` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`wishlist_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`wishlist_liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `liquor_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_wishlist_l_liquor_idx` (`liquor_id` ASC),
  INDEX `fk_wishlist_l_user_idx` (`user_id` ASC),
  CONSTRAINT `fk_wishlist_l_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor_dev`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wishlist_l_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`donelist_liquor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`donelist_liquor` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `liquor_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_donelist_l_user_idx` (`user_id` ASC),
  INDEX `fk_donelist_l_liquor_idx` (`liquor_id` ASC),
  CONSTRAINT `fk_donelist_l_liquor`
    FOREIGN KEY (`liquor_id`)
    REFERENCES `Liquor_dev`.`liquor` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_donelist_l_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`donelist_cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`donelist_cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cocktail_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_donelist_c_user_idx` (`user_id` ASC),
  INDEX `fk_donelist_c_cocktail_idx` (`cocktail_id` ASC),
  CONSTRAINT `fk_donelist_c_cocktail`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor_dev`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_donelist_c_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `Liquor_dev`.`wishlist_cocktail`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `Liquor_dev`.`wishlist_cocktail` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cocktail_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_wishlist_c_user_idx` (`user_id` ASC),
  INDEX `fk_wishlist_c_cocktail_idx` (`cocktail_id` ASC),
  CONSTRAINT `fk_wishlist_c_user`
    FOREIGN KEY (`user_id`)
    REFERENCES `Liquor_dev`.`user` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_wishlist_c_cocktail`
    FOREIGN KEY (`cocktail_id`)
    REFERENCES `Liquor_dev`.`cocktail` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
