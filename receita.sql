-- MySQL dump 10.13  Distrib 8.0.39, for Linux (x86_64)
--
-- Host: 0.0.0.0    Database: bairros_brasileiros
-- ------------------------------------------------------
-- Server version	9.0.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `historico_buscas`
--

DROP TABLE IF EXISTS `historico_buscas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_buscas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `receita_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `historico_buscas_receitas` (`receita_id`),
  CONSTRAINT `historico_buscas_receitas` FOREIGN KEY (`receita_id`) REFERENCES `receitas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_buscas`
--

LOCK TABLES `historico_buscas` WRITE;
/*!40000 ALTER TABLE `historico_buscas` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_buscas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `historico_capturas`
--

DROP TABLE IF EXISTS `historico_capturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `historico_capturas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `data_captura` datetime(3) NOT NULL,
  `sucesso` tinyint NOT NULL,
  `historico_buscas_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `historico_capturas_historico_busca` (`historico_buscas_id`),
  CONSTRAINT `historico_capturas_historico_busca` FOREIGN KEY (`historico_buscas_id`) REFERENCES `historico_buscas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `historico_capturas`
--

LOCK TABLES `historico_capturas` WRITE;
/*!40000 ALTER TABLE `historico_capturas` DISABLE KEYS */;
/*!40000 ALTER TABLE `historico_capturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locais`
--

DROP TABLE IF EXISTS `locais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locais` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `local` varchar(255) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  `parentalidade` int unsigned DEFAULT NULL,
  `tipo_localidade` int unsigned DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `parentalidade_id_constraint` (`parentalidade`),
  KEY `tipos_locais_tipo_localidade_constraint` (`tipo_localidade`),
  CONSTRAINT `parentalidade_id_constraint` FOREIGN KEY (`parentalidade`) REFERENCES `locais` (`id`),
  CONSTRAINT `tipos_locais_tipo_localidade_constraint` FOREIGN KEY (`tipo_localidade`) REFERENCES `tipos_locais` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locais`
--

LOCK TABLES `locais` WRITE;
/*!40000 ALTER TABLE `locais` DISABLE KEYS */;
INSERT INTO `locais` VALUES (1,'São Paulo',NULL,3),(2,'Paraná',NULL,3),(3,'Rio Grande do Sul',NULL,3),(4,'Santa Catarina',NULL,3),(5,'Minas Gerais',NULL,3),(6,'Mato Grosso',NULL,3),(7,'Acre',NULL,3),(8,'Alagoas',NULL,3),(9,'Amapá',NULL,3),(10,'Amazonas',NULL,3),(11,'Bahia',NULL,3),(12,'Ceará',NULL,3),(13,'Distrito Federal',NULL,3),(14,'Espírito Santo',NULL,3),(15,'Goiás',NULL,3),(16,'Maranhão',NULL,3),(17,'Pará',NULL,3),(18,'Paraíba',NULL,3),(19,'Pernambuco',NULL,3),(20,'Piauí',NULL,3),(21,'Rio de Janeiro',NULL,3),(22,'Rio Grande do Norte',NULL,3),(23,'Rondônia',NULL,3),(24,'Roraima',NULL,3),(25,'Sergipe',NULL,3),(26,'Tocantins',NULL,3),(27,'Macapá',1,2),(28,'Santana',1,2),(29,'Laranjal do Jari',1,2),(30,'Oiapoque',1,2),(31,'Mazagão',1,2),(32,'Porto Grande',1,2),(33,'Tartarugalzinho',1,2),(34,'Pedra Branca do Amapari',1,2),(35,'Vitória do Jari',1,2),(36,'Calçoene',1,2),(37,'Amapá',1,2),(38,'Ferreira Gomes',1,2),(39,'Itaubal',1,2),(40,'Serra do Navio',1,2),(41,'Pracuúba',1,2);
/*!40000 ALTER TABLE `locais` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mensagens_erros_capturas`
--

DROP TABLE IF EXISTS `mensagens_erros_capturas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mensagens_erros_capturas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `mensagem` varchar(255) DEFAULT NULL,
  `historico_capturas_id` int unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `mensagens_erros_capturas_historico_capturas` (`historico_capturas_id`),
  CONSTRAINT `mensagens_erros_capturas_historico_capturas` FOREIGN KEY (`historico_capturas_id`) REFERENCES `historico_capturas` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mensagens_erros_capturas`
--

LOCK TABLES `mensagens_erros_capturas` WRITE;
/*!40000 ALTER TABLE `mensagens_erros_capturas` DISABLE KEYS */;
/*!40000 ALTER TABLE `mensagens_erros_capturas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `migration_versions`
--

DROP TABLE IF EXISTS `migration_versions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `migration_versions` (
  `version` varchar(191) NOT NULL,
  `executed_at` datetime DEFAULT NULL,
  `execution_time` int DEFAULT NULL,
  PRIMARY KEY (`version`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `migration_versions`
--

LOCK TABLES `migration_versions` WRITE;
/*!40000 ALTER TABLE `migration_versions` DISABLE KEYS */;
INSERT INTO `migration_versions` VALUES ('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241006202116','2024-10-19 23:09:57',170),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241008000406','2024-10-19 23:09:57',12),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241008115114','2024-10-19 23:09:57',94),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241012150945','2024-10-19 23:28:33',24),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241014085107','2024-10-19 23:28:33',76),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241014230557','2024-10-19 23:28:33',69),('Danilocgsilva\\BairrosBrasileirosLinhaDeComandos\\Version20241018094655','2024-10-19 23:28:34',69);
/*!40000 ALTER TABLE `migration_versions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `receitas`
--

DROP TABLE IF EXISTS `receitas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `receitas` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `nome` varchar(255) DEFAULT NULL,
  `seletor_tabela` char(192) DEFAULT NULL,
  `seletor_coluna` char(192) DEFAULT NULL,
  `endereco` varchar(255) DEFAULT NULL,
  `tipo_localidade` char(32) DEFAULT NULL,
  `nome_localidade_pai` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `receitas`
--

LOCK TABLES `receitas` WRITE;
/*!40000 ALTER TABLE `receitas` DISABLE KEYS */;
INSERT INTO `receitas` VALUES (1,'Busca de cidades do Amapá','table.wikitable.sortable tbody tr','td:nth-child(2) a','https://pt.wikipedia.org/wiki/Lista_de_munic%C3%ADpios_do_Amap%C3%A1_por_popula%C3%A7%C3%A3o','cidade','Amapá');
/*!40000 ALTER TABLE `receitas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tipos_locais`
--

DROP TABLE IF EXISTS `tipos_locais`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tipos_locais` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `tipo` varchar(32) COLLATE utf8mb3_unicode_ci DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tipos_locais`
--

LOCK TABLES `tipos_locais` WRITE;
/*!40000 ALTER TABLE `tipos_locais` DISABLE KEYS */;
INSERT INTO `tipos_locais` VALUES (1,'bairro'),(2,'cidade'),(3,'estado');
/*!40000 ALTER TABLE `tipos_locais` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-19 20:55:01
