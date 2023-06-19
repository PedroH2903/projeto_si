-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema trocatroca_db
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema trocatroca_db
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `trocatroca_db` ;
USE `trocatroca_db` ;

-- -----------------------------------------------------
-- Table `trocatroca_db`.`person`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`person` (
  `idpessoa` INT NOT NULL,
  `registration` VARCHAR(100) CHARACTER SET 'big5' NULL,
  `hash_passw` VARCHAR(9999) NULL,
  `name` VARCHAR(999) NULL,
  `hash_email` VARCHAR(999) NULL,
  PRIMARY KEY (`idpessoa`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`category`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`category` (
  `idcategory` INT NOT NULL,
  `name` VARCHAR(500) NULL,
  `desc` VARCHAR(500) NULL,
  PRIMARY KEY (`idcategory`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`item` (
  `idobject` INT NOT NULL,
  `name` VARCHAR(999) NULL,
  `model_color` VARCHAR(999) NULL,
  `brand_species` VARCHAR(450) NULL,
  `year_acquired` VARCHAR(4) NULL,
  `desc` VARCHAR(999) NULL,
  `category_idcategory` INT NOT NULL,
  `condition` VARCHAR(450) NULL,
  `vaccines` VARCHAR(999) NULL,
  `likes` VARCHAR(450) NULL,
  `dislikes` VARCHAR(450) NULL,
  PRIMARY KEY (`idobject`, `category_idcategory`),
  INDEX `fk_object_category1_idx` (`category_idcategory` ASC),
  CONSTRAINT `fk_object_category1`
    FOREIGN KEY (`category_idcategory`)
    REFERENCES `trocatroca_db`.`category` (`idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`person_adv_exch_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`person_adv_exch_item` (
  `person_idpessoa` INT NOT NULL,
  `object_idobject` INT NOT NULL,
  `object_category_idcategory` INT NOT NULL,
  `desc` VARCHAR(999) NULL,
  `delivery` VARCHAR(45) NULL,
  `reason` VARCHAR(450) NULL,
  `market_price` VARCHAR(25) NULL,
  `listed` VARCHAR(25) NULL,
  PRIMARY KEY (`person_idpessoa`, `object_idobject`, `object_category_idcategory`),
  INDEX `fk_person_has_object_object3_idx` (`object_idobject` ASC, `object_category_idcategory` ASC),
  INDEX `fk_person_has_object_person3_idx` (`person_idpessoa` ASC),
  CONSTRAINT `fk_person_has_object_person3`
    FOREIGN KEY (`person_idpessoa`)
    REFERENCES `trocatroca_db`.`person` (`idpessoa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_has_object_object3`
    FOREIGN KEY (`object_idobject` , `object_category_idcategory`)
    REFERENCES `trocatroca_db`.`item` (`idobject` , `category_idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`person_adv_donate_item`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`person_adv_donate_item` (
  `person_idpessoa` INT NOT NULL,
  `object_idobject` INT NOT NULL,
  `object_category_idcategory` INT NOT NULL,
  `desc` VARCHAR(999) NULL,
  `delivery` VARCHAR(25) NULL,
  `reason` VARCHAR(450) NULL,
  `listed` VARCHAR(25) NULL,
  PRIMARY KEY (`person_idpessoa`, `object_idobject`, `object_category_idcategory`),
  INDEX `fk_person_has_object_object4_idx` (`object_idobject` ASC, `object_category_idcategory` ASC),
  INDEX `fk_person_has_object_person4_idx` (`person_idpessoa` ASC),
  CONSTRAINT `fk_person_has_object_person4`
    FOREIGN KEY (`person_idpessoa`)
    REFERENCES `trocatroca_db`.`person` (`idpessoa`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_person_has_object_object4`
    FOREIGN KEY (`object_idobject` , `object_category_idcategory`)
    REFERENCES `trocatroca_db`.`item` (`idobject` , `category_idcategory`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`country`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`country` (
  `idcountry` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  PRIMARY KEY (`idcountry`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`FU`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`FU` (
  `idFU` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  `country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idFU`, `country_idcountry`),
  INDEX `fk_FU_country1_idx` (`country_idcountry` ASC),
  CONSTRAINT `fk_FU_country1`
    FOREIGN KEY (`country_idcountry`)
    REFERENCES `trocatroca_db`.`country` (`idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`city` (
  `idcity` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  `FU_idFU` INT NOT NULL,
  `FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idcity`, `FU_idFU`, `FU_country_idcountry`),
  INDEX `fk_city_FU2_idx` (`FU_idFU` ASC, `FU_country_idcountry` ASC),
  CONSTRAINT `fk_city_FU2`
    FOREIGN KEY (`FU_idFU` , `FU_country_idcountry`)
    REFERENCES `trocatroca_db`.`FU` (`idFU` , `country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`street`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`street` (
  `idstreet` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  `city_idcity` INT NOT NULL,
  `city_FU_idFU` INT NOT NULL,
  `city_FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idstreet`, `city_idcity`, `city_FU_idFU`, `city_FU_country_idcountry`),
  INDEX `fk_street_city2_idx` (`city_idcity` ASC, `city_FU_idFU` ASC, `city_FU_country_idcountry` ASC),
  CONSTRAINT `fk_street_city2`
    FOREIGN KEY (`city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    REFERENCES `trocatroca_db`.`city` (`idcity` , `FU_idFU` , `FU_country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`address`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`address` (
  `idaddress` INT NOT NULL,
  `number` VARCHAR(25) NULL,
  `desc` VARCHAR(450) NULL,
  `street_idstreet` INT NOT NULL,
  `street_city_idcity` INT NOT NULL,
  `street_city_FU_idFU` INT NOT NULL,
  `street_city_FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idaddress`, `street_idstreet`, `street_city_idcity`, `street_city_FU_idFU`, `street_city_FU_country_idcountry`),
  INDEX `fk_address_street1_idx` (`street_idstreet` ASC, `street_city_idcity` ASC, `street_city_FU_idFU` ASC, `street_city_FU_country_idcountry` ASC),
  CONSTRAINT `fk_address_street1`
    FOREIGN KEY (`street_idstreet` , `street_city_idcity` , `street_city_FU_idFU` , `street_city_FU_country_idcountry`)
    REFERENCES `trocatroca_db`.`street` (`idstreet` , `city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`city`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`city` (
  `idcity` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  `FU_idFU` INT NOT NULL,
  `FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idcity`, `FU_idFU`, `FU_country_idcountry`),
  INDEX `fk_city_FU2_idx` (`FU_idFU` ASC, `FU_country_idcountry` ASC),
  CONSTRAINT `fk_city_FU2`
    FOREIGN KEY (`FU_idFU` , `FU_country_idcountry`)
    REFERENCES `trocatroca_db`.`FU` (`idFU` , `country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `trocatroca_db`.`street`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `trocatroca_db`.`street` (
  `idstreet` INT NOT NULL,
  `name` VARCHAR(450) NULL,
  `city_idcity` INT NOT NULL,
  `city_FU_idFU` INT NOT NULL,
  `city_FU_country_idcountry` INT NOT NULL,
  PRIMARY KEY (`idstreet`, `city_idcity`, `city_FU_idFU`, `city_FU_country_idcountry`),
  INDEX `fk_street_city2_idx` (`city_idcity` ASC, `city_FU_idFU` ASC, `city_FU_country_idcountry` ASC),
  CONSTRAINT `fk_street_city2`
    FOREIGN KEY (`city_idcity` , `city_FU_idFU` , `city_FU_country_idcountry`)
    REFERENCES `trocatroca_db`.`city` (`idcity` , `FU_idFU` , `FU_country_idcountry`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;