-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: db
-- Tiempo de generación: 05-05-2020 a las 00:31:24
-- Versión del servidor: 10.1.41-MariaDB-1~bionic
-- Versión de PHP: 7.4.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `grupo16`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `assistance_student_workshop`
--

CREATE TABLE `assistance_student_workshop` (
  `id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL,
  `school_year_id` int(11) NOT NULL,
  `workshop_id` int(11) NOT NULL,
  `date` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `assistance_student_workshop`
--

INSERT INTO `assistance_student_workshop` (`id`, `student_id`, `school_year_id`, `workshop_id`, `date`) VALUES
(1, 3, 1, 2, '0000-00-00 00:00:00');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `configuration`
--

CREATE TABLE `configuration` (
  `field` varchar(255) NOT NULL,
  `value` varchar(255) NOT NULL,
  `title` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `configuration`
--

INSERT INTO `configuration` (`field`, `value`, `title`) VALUES
('description', 'Descripcion de la pagina web', 'Descripcion'),
('elementsCount', '2', 'Cantidad de elementos por pagina'),
('email', 'mail@mail.com', 'Correo electronico'),
('maintenance', '0', 'Mantenimiento'),
('title', 'Escuela Orquesta', 'titulo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `cores`
--

CREATE TABLE `cores` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `cores`
--

INSERT INTO `cores` (`id`, `name`, `address`, `phone`) VALUES
(1, 'Escuelas primarias', 'Calle 6 e/ 8 y 158', ''),
(2, 'Escuelas primarias', 'Calle 6 e/ 8 y 158', ''),
(3, '7', '151 8 y 9', ''),
(4, '8', '63 y 125 ', ''),
(5, '14', '96 y 126 ', ''),
(6, '17', '164 y 26 ', ''),
(7, '20', 'ruta 11 km 13- Pje La Hermosura ', ''),
(8, 'jardin 904', '164 30 y 31', ''),
(9, 'Esc 501', 'Pascual Ruberto e/ 168 y 169 ', ''),
(10, 'CIC', '169 y 33', ''),
(11, 'Parroquia San Miguel Arcángel', '63 y 124', '');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `days`
--

CREATE TABLE `days` (
  `id` int(11) NOT NULL,
  `name` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `days`
--

INSERT INTO `days` (`id`, `name`) VALUES
(1, 'lunes'),
(2, 'martes'),
(3, 'miércoles'),
(4, 'jueves'),
(5, 'viernes'),
(6, 'sábado'),
(7, 'domingo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `genders`
--

CREATE TABLE `genders` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `genders`
--

INSERT INTO `genders` (`id`, `name`) VALUES
(1, 'Masculino'),
(2, 'Femenino'),
(3, 'Otro');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instruments`
--

CREATE TABLE `instruments` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `type_id` int(11) NOT NULL,
  `photo` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `alt` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `instrument_types`
--

CREATE TABLE `instrument_types` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `instrument_types`
--

INSERT INTO `instrument_types` (`id`, `name`) VALUES
(1, 'Viento'),
(2, 'Cuerda'),
(3, 'Percusión'),
(4, 'Viento'),
(5, 'Cuerda'),
(6, 'Percusión'),
(7, 'Viento'),
(8, 'Cuerda'),
(9, 'Percusión'),
(10, 'Viento'),
(11, 'Cuerda'),
(12, 'Percusión'),
(13, 'Viento'),
(14, 'Cuerda'),
(15, 'Percusión');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `levels`
--

CREATE TABLE `levels` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `levels`
--

INSERT INTO `levels` (`id`, `name`) VALUES
(1, 'I'),
(2, 'II'),
(3, 'III'),
(4, 'IV'),
(5, 'V'),
(6, 'VI'),
(7, 'VII'),
(8, 'VIII'),
(9, 'IX'),
(10, 'X'),
(11, 'XI'),
(12, 'XII');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `map_points`
--

CREATE TABLE `map_points` (
  `name` varchar(255) NOT NULL,
  `latitude` varchar(255) NOT NULL,
  `longitude` varchar(255) NOT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `map_points`
--

INSERT INTO `map_points` (`name`, `latitude`, `longitude`, `id`) VALUES
('Orquesta Escuela Berisso', '-34.925968', '-57.8957427', 1),
('Orquesta Escuela Berisso (Esc 6)', '-34.876211', '-57.8935132', 2),
('Orquesta Escuela Berisso (Esc 22)', '-34.8777566', '-57.8559195', 3),
('Orquesta Escuela Berisso (Esc 17)', '-34.880934', '-57.8720587', 4),
('Orquesta Escuela Berisso (Esc 19)', '-34.889561', '-57.9083765', 5),
('Orquesta Escuela Berisso (Esc 7)', '-34.88443', '-57.8997836', 6),
('Orquesta Escuela Berisso (Parroquia)', '-34.9074764', '-57.9230819', 7),
('Orquesta Escuela Berisso (CIC)', '-34.8819123', '-57.8599027', 8),
('Orquesta Escuela Berisso (Club V.R)', '-34.884226', '-57.8694407', 9),
('Orquesta Escuela Berisso (Club Español)', '-34.915493', '-57.9482335', 10),
('Orquesta Escuela Berisso (Esc 20)', '-34.957968', '-57.8186752', 11);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `permissions`
--

CREATE TABLE `permissions` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `permissions`
--

INSERT INTO `permissions` (`id`, `name`) VALUES
(1, 'config_index'),
(2, 'student_index'),
(3, 'student_new'),
(4, 'student_destroy'),
(5, 'student_update'),
(6, 'student_show'),
(7, 'config_update'),
(8, 'users_show'),
(9, 'user_update'),
(10, 'users_destroy'),
(11, 'users_index'),
(13, 'users_new'),
(14, 'school_year_index'),
(15, 'school_year_new'),
(16, 'school_year_destroy'),
(17, 'school_year_update'),
(18, 'school_year_show'),
(19, 'teacher_new'),
(20, 'teacher_index'),
(21, 'teacher_destroy'),
(22, 'teacher_show'),
(23, 'teacher_update'),
(24, 'workshop_index'),
(25, 'workshop_show'),
(26, 'workshop_new'),
(27, 'workshop_update'),
(28, 'workshop_destroy'),
(29, 'schedules_index'),
(30, 'schedules_new'),
(31, 'schedules_destroy'),
(32, 'schedules_show'),
(33, 'schedules_update'),
(34, 'instrument_new'),
(35, 'instrument_show'),
(36, 'instrument_index'),
(37, 'instrument_update'),
(38, 'instrument_destroy'),
(39, 'assistace_list'),
(40, 'assistace_update');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preceptors`
--

CREATE TABLE `preceptors` (
  `id` int(11) NOT NULL,
  `last_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `preceptor_core`
--

CREATE TABLE `preceptor_core` (
  `preceptor_id` int(11) NOT NULL,
  `core_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsables`
--

CREATE TABLE `responsables` (
  `id` int(11) NOT NULL,
  `last_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `birth_date` date NOT NULL,
  `location_id` int(11) NOT NULL,
  `home` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `gender_id` int(11) NOT NULL,
  `document_type_id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `responsable_student`
--

CREATE TABLE `responsable_student` (
  `responsable_id` int(11) NOT NULL,
  `student_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_bin NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id`, `name`) VALUES
(1, 'Administrador'),
(2, 'Profesor'),
(3, 'Preceptor');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `role_has_permission`
--

CREATE TABLE `role_has_permission` (
  `id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `role_has_permission`
--

INSERT INTO `role_has_permission` (`id`, `role_id`, `permission_id`) VALUES
(1, 1, 1),
(2, 2, 2),
(3, 1, 3),
(4, 1, 4),
(5, 1, 5),
(6, 1, 6),
(7, 1, 7),
(8, 1, 8),
(9, 1, 9),
(10, 1, 10),
(11, 1, 11),
(13, 1, 13),
(15, 1, 14),
(16, 1, 15),
(17, 1, 16),
(18, 1, 17),
(19, 1, 18),
(20, 1, 23),
(21, 1, 22),
(22, 1, 21),
(23, 1, 20),
(24, 1, 19),
(25, 1, 21),
(26, 1, 22),
(27, 1, 23),
(28, 1, 24),
(29, 1, 25),
(30, 1, 26),
(31, 1, 27),
(32, 1, 28),
(33, 2, 11),
(34, 2, 12),
(35, 2, 6),
(36, 2, 20),
(37, 2, 22),
(38, 2, 24),
(39, 2, 25),
(40, 2, 14),
(41, 2, 18),
(42, 2, 14),
(43, 2, 18),
(45, 2, 2),
(46, 2, 5),
(47, 2, 6),
(48, 2, 2),
(49, 2, 5),
(50, 2, 6),
(51, 2, 2),
(53, 2, 5),
(54, 3, 2),
(55, 3, 4),
(56, 3, 5),
(57, 1, 29),
(58, 1, 30),
(59, 1, 31),
(60, 1, 32),
(61, 1, 33),
(62, 1, 34),
(63, 1, 35),
(64, 1, 36),
(65, 1, 37),
(66, 1, 38),
(67, 1, 39),
(68, 1, 40);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `schedules`
--

CREATE TABLE `schedules` (
  `id` int(11) NOT NULL,
  `day_id` varchar(11) NOT NULL,
  `school_year_workshop_id` varchar(11) NOT NULL,
  `core_id` varchar(11) NOT NULL,
  `start_time` varchar(255) NOT NULL,
  `finish_time` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `schedules`
--

INSERT INTO `schedules` (`id`, `day_id`, `school_year_workshop_id`, `core_id`, `start_time`, `finish_time`) VALUES
(33, '2', '2', '1', '13:34', '13:33'),
(34, '1', '2', '1', '00:12', '00:25'),
(35, '2', '2', '1', '00:32', '00:33'),
(36, '1', '2', '1', '11:11', '23:12'),
(37, '4', '4', '1', '03:00', '03:59');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `schools`
--

CREATE TABLE `schools` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `address` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `schools`
--

INSERT INTO `schools` (`id`, `name`, `address`, `phone`) VALUES
(1, '502', NULL, NULL),
(2, 'Albert Thomas', NULL, NULL),
(3, 'Anexa', NULL, NULL),
(4, 'Anexo T. Speroni', NULL, NULL),
(5, 'Basiliana', NULL, NULL),
(6, 'Basiliano', NULL, NULL),
(7, 'Bellas Artes', NULL, NULL),
(8, 'Canossiano', NULL, NULL),
(9, 'Castañeda', NULL, NULL),
(10, 'Col. Nacional', NULL, NULL),
(11, 'Conquista Cristiana', NULL, NULL),
(12, 'Dardo Rocha N° 24', NULL, NULL),
(13, 'E.E.M.N° 2', NULL, NULL),
(14, 'E.M. N°26', NULL, NULL),
(15, 'E.P. Municipal N° 2', NULL, NULL),
(16, 'EE N° 2', NULL, NULL),
(17, 'EEE N° 501', NULL, NULL),
(18, 'EEE N°501', NULL, NULL),
(19, 'EEM N° 1', NULL, NULL),
(20, 'EEM N° 26 L.P', NULL, NULL),
(21, 'EEM N°128', NULL, NULL),
(22, 'EEM N°2', NULL, NULL),
(23, 'EES N° 10', NULL, NULL),
(24, 'EES N° 14', NULL, NULL),
(25, 'EES N° 4', NULL, NULL),
(26, 'EES N° 4 Berisso', NULL, NULL),
(27, 'EES N° 4 El Pino', NULL, NULL),
(28, 'EEST N° 1 bsso', NULL, NULL),
(29, 'EET Nº 1', NULL, NULL),
(30, 'EET Nº1', NULL, NULL),
(31, 'EGB N°25', NULL, NULL),
(32, 'EM N° 2', NULL, NULL),
(33, 'EMM N° 3', NULL, NULL),
(34, 'EP N° 1 L.P-', NULL, NULL),
(35, 'EP N° 11', NULL, NULL),
(36, 'EP N° 129', NULL, NULL),
(37, 'EP N° 14', NULL, NULL),
(38, 'EP N° 15', NULL, NULL),
(39, 'EP N° 17', NULL, NULL),
(40, 'EP N° 18', NULL, NULL),
(41, 'EP N° 19', NULL, NULL),
(42, 'EP N° 2', NULL, NULL),
(43, 'EP N° 20', NULL, NULL),
(44, 'EP N° 22', NULL, NULL),
(45, 'EP N° 25', NULL, NULL),
(46, 'EP N° 27', NULL, NULL),
(47, 'EP N° 3', NULL, NULL),
(48, 'EP N° 37 LP', NULL, NULL),
(49, 'EP N° 43', NULL, NULL),
(50, 'EP N° 45', NULL, NULL),
(51, 'EP N° 5', NULL, NULL),
(52, 'EP N° 6', NULL, NULL),
(53, 'EP N° 65 La Plata', NULL, NULL),
(54, 'EP N° 7', NULL, NULL),
(55, 'EPB N° 10', NULL, NULL),
(56, 'EPB N° 14', NULL, NULL),
(57, 'EPB N° 15', NULL, NULL),
(58, 'EPB N° 19', NULL, NULL),
(59, 'EPB N° 2', NULL, NULL),
(60, 'EPB N° 20', NULL, NULL),
(61, 'EPB N° 24', NULL, NULL),
(62, 'EPB N° 25', NULL, NULL),
(63, 'EPB N° 45', NULL, NULL),
(64, 'EPB N° 5', NULL, NULL),
(65, 'EPB N° 55', NULL, NULL),
(66, 'EPB N° 6', NULL, NULL),
(67, 'EPB N° 65', NULL, NULL),
(68, 'EPB N° 8', NULL, NULL),
(69, 'ESB N° 10', NULL, NULL),
(70, 'ESB N° 11', NULL, NULL),
(71, 'ESB N° 14', NULL, NULL),
(72, 'ESB N° 3', NULL, NULL),
(73, 'ESB N° 61', NULL, NULL),
(74, 'ESB N° 66', NULL, NULL),
(75, 'ESB N° 8', NULL, NULL),
(76, 'ESB N° 9', NULL, NULL),
(77, 'ESC N° 10', NULL, NULL),
(78, 'ESC N° 13', NULL, NULL),
(79, 'ESC N° 19', NULL, NULL),
(80, 'ESC N° 2', NULL, NULL),
(81, 'ESC N° 20', NULL, NULL),
(82, 'ESC N° 22', NULL, NULL),
(83, 'ESC N° 23', NULL, NULL),
(84, 'ESC N° 24', NULL, NULL),
(85, 'ESC N° 25', NULL, NULL),
(86, 'ESC N° 27', NULL, NULL),
(87, 'ESC N° 3', NULL, NULL),
(88, 'ESC N° 43', NULL, NULL),
(89, 'ESC N° 45', NULL, NULL),
(90, 'ESC N° 5', NULL, NULL),
(91, 'ESC N° 501', NULL, NULL),
(92, 'ESC N° 6', NULL, NULL),
(93, 'ESC N° 66', NULL, NULL),
(94, 'ESC N° 7', NULL, NULL),
(95, 'ESC N° 8', NULL, NULL),
(96, 'ESC N°11', NULL, NULL),
(97, 'ESC N°17', NULL, NULL),
(98, 'ESC N°19', NULL, NULL),
(99, 'ESC N°3', NULL, NULL),
(100, 'ESC N°7', NULL, NULL),
(101, 'ESC de Arte', NULL, NULL),
(102, 'ESS N° 4', NULL, NULL),
(103, 'Enseñanza Media', NULL, NULL),
(104, 'Especial N° 502', NULL, NULL),
(105, 'Estrada', NULL, NULL),
(106, 'FACULTAD', NULL, NULL),
(107, 'INDUSTRIAL', NULL, NULL),
(108, 'Italiana', NULL, NULL),
(109, 'J 904', NULL, NULL),
(110, 'J. Manuel Strada', NULL, NULL),
(111, 'Jacarandá', NULL, NULL),
(112, 'Jardín Euforion', NULL, NULL),
(113, 'Jardín N° 903', NULL, NULL),
(114, 'Jardín N° 907', NULL, NULL),
(115, 'JoaquinV.Gonzalez', NULL, NULL),
(116, 'Lola Mora sec', NULL, NULL),
(117, 'Lujan Sierra', NULL, NULL),
(118, 'MUNICIOAL 11', NULL, NULL),
(119, 'María Auxiliadora', NULL, NULL),
(120, 'María Reina', NULL, NULL),
(121, 'Media 2 España', NULL, NULL),
(122, 'Media N 1', NULL, NULL),
(123, 'Mercedita de S.Martin', NULL, NULL),
(124, 'Monseñor Alberti', NULL, NULL),
(125, 'Mtro Luis MKEY', NULL, NULL),
(126, 'Mñor. Rasore', NULL, NULL),
(127, 'N1 Francisco', NULL, NULL),
(128, 'Normal 2', NULL, NULL),
(129, 'Normal 3 LP', NULL, NULL),
(130, 'Normal n 2', NULL, NULL),
(131, 'Ntra Sra Lourdes', NULL, NULL),
(132, 'Ntra. Sra. del Valle', NULL, NULL),
(133, 'PSICOLOGIA', NULL, NULL),
(134, 'Parroquial', NULL, NULL),
(135, 'Pasos del Libertedor', NULL, NULL),
(136, 'Ped 61', NULL, NULL),
(137, 'Pedagogica', NULL, NULL),
(138, 'SEC N° 8', NULL, NULL),
(139, 'SEC N°17', NULL, NULL),
(140, 'San Simón', NULL, NULL),
(141, 'Santa Rosa', NULL, NULL),
(142, 'Sra de Fátima', NULL, NULL),
(143, 'Sta Margarita', NULL, NULL),
(144, 'Sta Ro. de Lima', NULL, NULL),
(145, 'Sta Rosa', NULL, NULL),
(146, 'Sta Rosa Lima', NULL, NULL),
(147, 'Sta. R. de Lima', NULL, NULL),
(148, 'Sta. Rosa de lima', NULL, NULL),
(149, 'Técnica N° 1', NULL, NULL),
(150, 'Técnica N° 1 Berisso', NULL, NULL),
(151, 'Técnica N° 5', NULL, NULL),
(152, 'Técnica N° 7', NULL, NULL),
(153, 'UCALP', NULL, NULL),
(154, 'UNLP', NULL, NULL),
(155, 'UTN', NULL, NULL),
(156, 'Universitas', NULL, NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `school_years`
--

CREATE TABLE `school_years` (
  `id` int(11) NOT NULL,
  `start_date` datetime DEFAULT NULL,
  `ending_date` datetime DEFAULT NULL,
  `semester` tinyint(1) NOT NULL DEFAULT '1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `school_years`
--

INSERT INTO `school_years` (`id`, `start_date`, `ending_date`, `semester`) VALUES
(7, '2019-01-01 00:00:00', '2019-11-29 00:00:00', 1),
(8, '2020-05-24 00:00:00', '2020-12-16 00:00:00', 1),
(9, '2021-02-03 00:00:00', '2021-05-19 00:00:00', 1),
(10, '2019-12-01 00:00:00', '2019-12-31 00:00:00', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `school_year_workshop`
--

CREATE TABLE `school_year_workshop` (
  `id` int(11) NOT NULL,
  `workshop_id` int(11) NOT NULL,
  `school_year_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `school_year_workshop`
--

INSERT INTO `school_year_workshop` (`id`, `workshop_id`, `school_year_id`) VALUES
(2, 1, 7),
(3, 2, 7),
(4, 1, 9);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `students`
--

CREATE TABLE `students` (
  `id` int(11) NOT NULL,
  `last_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `birth_date` date NOT NULL,
  `location_id` int(11) NOT NULL,
  `level_id` int(11) NOT NULL,
  `home` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `gender_id` int(11) NOT NULL,
  `school_id` int(11) NOT NULL,
  `document_type_id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `town_down_id` int(11) NOT NULL,
  `place_of_birth` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `responsable` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `students`
--

INSERT INTO `students` (`id`, `last_name`, `first_name`, `birth_date`, `location_id`, `level_id`, `home`, `gender_id`, `school_id`, `document_type_id`, `number`, `phone`, `town_down_id`, `place_of_birth`, `responsable`) VALUES
(4, 'qweqwe', 'qweqwe', '2019-11-07', 5, 6, 'qweqwe', 1, 5, 1, 123123, 'qweqw', 5, 'qweqwe', 'qweqweqwe'),
(5, '123123', '123123', '2019-11-09', 4, 5, 'asdasd', 1, 5, 1, 12312, 'asdasd', 6, '123123', 'asdasd');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `student_workshop`
--

CREATE TABLE `student_workshop` (
  `student_id` int(11) NOT NULL,
  `school_year_id` int(11) NOT NULL,
  `workshop_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `student_workshop`
--

INSERT INTO `student_workshop` (`student_id`, `school_year_id`, `workshop_id`) VALUES
(1, 8, 1),
(4, 7, 1),
(1, 8, 1),
(4, 7, 1),
(1, 8, 1),
(4, 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `teachers`
--

CREATE TABLE `teachers` (
  `id` int(11) NOT NULL,
  `last_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `first_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `birth_date` date NOT NULL,
  `location_id` int(11) NOT NULL,
  `home` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `gender_id` int(11) NOT NULL,
  `document_type_id` int(11) NOT NULL,
  `number` int(11) NOT NULL,
  `phone` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `teachers`
--

INSERT INTO `teachers` (`id`, `last_name`, `first_name`, `birth_date`, `location_id`, `home`, `gender_id`, `document_type_id`, `number`, `phone`) VALUES
(3, 'alvarez', 'graciela', '1980-03-21', 5, 'veracruz', 2, 1, 34987362, '221987253'),
(4, 'test', 'test', '2019-11-04', 2, 'asdasd', 3, 1, 123123, '123123');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `teacher_responsable_workshop`
--

CREATE TABLE `teacher_responsable_workshop` (
  `teacher_id` int(11) NOT NULL,
  `school_year_id` int(11) NOT NULL,
  `workshop_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `teacher_responsable_workshop`
--

INSERT INTO `teacher_responsable_workshop` (`teacher_id`, `school_year_id`, `workshop_id`) VALUES
(3, 7, 1),
(4, 7, 1),
(3, 7, 1),
(4, 7, 1),
(3, 7, 1),
(4, 7, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `town_down`
--

CREATE TABLE `town_down` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `town_down`
--

INSERT INTO `town_down` (`id`, `name`) VALUES
(1, 'Barrio Náutico'),
(2, 'Barrio Obrero'),
(3, 'Berisso'),
(4, 'Barrio Solidaridad'),
(5, 'Barrio Obrero'),
(6, 'Barrio Bco. Pcia.'),
(7, 'Barrio J.B. Justo'),
(8, 'Barrio Obrero'),
(9, 'El Carmen'),
(10, 'El Labrador'),
(11, 'Ensenada'),
(12, 'La Hermosura'),
(13, 'La PLata'),
(14, 'Los Talas'),
(15, 'Ringuelet'),
(16, 'Tolosa'),
(17, 'Villa Alba'),
(18, 'Villa Arguello'),
(19, 'Villa B. C'),
(20, 'Villa Elvira'),
(21, 'Villa Nueva'),
(22, 'Villa Paula'),
(23, 'Villa Progreso'),
(24, 'Villa San Carlos'),
(25, 'Villa Zula');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) COLLATE utf8_bin NOT NULL,
  `username` varchar(255) COLLATE utf8_bin NOT NULL,
  `password` varchar(255) COLLATE utf8_bin NOT NULL,
  `active` tinyint(1) NOT NULL DEFAULT '1',
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(255) COLLATE utf8_bin NOT NULL,
  `last_name` varchar(255) COLLATE utf8_bin NOT NULL,
  `is_social` int(11) NOT NULL DEFAULT '0'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `email`, `username`, `password`, `active`, `updated_at`, `created_at`, `first_name`, `last_name`, `is_social`) VALUES
(1, 'fede@mail.com', 'fede', '87e477fe76565d7d19101e66e71344aa813557ec', 1, '2019-10-24 15:05:48', '2019-10-21 00:00:00', 'Federico', 'Gasquez', 0),
(2, 'agustin@mail.com', 'agustin', '5f0647500b3a8e716aa982c1c51b36c9168e0f8f', 1, '2019-10-30 11:37:23', '2019-10-21 00:00:00', 'agustin', 'agustin', 0),
(3, 'jorge@mail.com', 'jorge', '546adbb44a0479b320635e0452ca06a4de041ccd', 0, '2019-10-24 15:05:53', '2019-10-21 00:00:00', 'jorge', 'agustin', 0),
(4, 'matias@mail.com', 'matias', 'dbc6bbe3b711e3f58f25638428fdfc12e34c8c38', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'matias', 'agustin', 0),
(5, 'lautaro@mail.com', 'lautaro', '75006e9292109a67f31f726a9f0390c42bf83478', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'lautaro', 'agustin', 0),
(6, 'federicogasquez@gmail.com', 'fede_2', 'd6f9d5f47ad277927a5896470307e6f68499a3b4', 1, '2019-10-24 14:52:00', '2019-10-21 00:00:00', 'fede', '2', 0),
(7, 'ayelen@mail.com', 'ayelen', '70849a111ee2b68345c570e67f4a1f2e583206f3', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'ayelen', 'agustin', 0),
(8, 'maria@mail.com', 'maria', 'e21fc56c1a272b630e0d1439079d0598cf8b8329', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'maria', 'agustin', 0),
(9, 'federico@mail.com', 'federico', '4999915a961edfd7686112c2935288e1266eae14', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'federico', 'agustin', 0),
(10, 'camila@mail.com', 'camila', 'c5c8066d458ef32d2d9d6c641cd90b1f5259ebed', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'camila', 'agustin', 0),
(11, 'celesten@mail.com', 'celeste', '964a37eade1ceb3d67b0dbee7a1807f8f0715197', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'celeste', 'agustin', 0),
(12, 'julieta@mail.com', 'julieta', '8c842b01aa3358b20822e0f8dd711f9a4fa4c80a', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'julieta', 'agustin', 0),
(13, 'rocio@mail.com', 'rocio', 'ef86ee7ce0fdb135eb95199be0bc0d8e48a5e023', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'rocio', 'agustin', 0),
(14, 'juan@mail.com', 'juan', 'a681645520394247d592ae4a15c9778328a2f121', 0, '2019-10-24 16:31:43', '2019-10-21 00:00:00', 'juan', 'agustin', 0),
(15, 'nahuel@mail.com', 'nahuel', '538d2d442e1e867715aae58bda5fc207640a8f88', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'nahuel', 'agustin', 0),
(16, 'milagros@mail.com', 'milagros', '3c5d9566525c9638fb34a90b33e0fed6f6d378af', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'milagros', 'agustin', 0),
(17, 'roberto@mail.com', 'roberto', '9d500263e1a3252bc63faaca4e2bd9b72da439c3', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'roberto', 'agustin', 0),
(18, 'carlos@mail.com', 'carlos', 'ab5e2bca84933118bbc9d48ffaccce3bac4eeb64', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'carlos', 'agustin', 0),
(19, 'alicia@mail.com', 'alicia', '5ef025eb503bfce26fe6734d085174abf3b9a6a2', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'alicia', 'agustin', 0),
(20, 'mariela@mail.com', 'mariela', '06300743b84744b6ddab09cce692b01e86c30094', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'mariela', 'agustin', 0),
(22, 'agustin@mail.com', 'agustin', '5f0647500b3a8e716aa982c1c51b36c9168e0f8f', 1, '2019-10-21 00:00:00', '2019-10-21 00:00:00', 'agustin', 'agustin', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user_has_role`
--

CREATE TABLE `user_has_role` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

--
-- Volcado de datos para la tabla `user_has_role`
--

INSERT INTO `user_has_role` (`id`, `user_id`, `role_id`) VALUES
(1, 1, 1),
(2, 1, 2),
(7, 2, 2),
(8, 4, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `workshops`
--

CREATE TABLE `workshops` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `short_name` varchar(255) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `workshops`
--

INSERT INTO `workshops` (`id`, `name`, `short_name`) VALUES
(1, 'Canto coral', 'coro'),
(2, 'Dirección orquestal', 'Dirección');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `assistance_student_workshop`
--
ALTER TABLE `assistance_student_workshop`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_assistance_student_id` (`student_id`),
  ADD KEY `FK_assistance_school_year_id` (`school_year_id`),
  ADD KEY `FK_assistance_workshop_id` (`workshop_id`);

--
-- Indices de la tabla `configuration`
--
ALTER TABLE `configuration`
  ADD PRIMARY KEY (`field`);

--
-- Indices de la tabla `cores`
--
ALTER TABLE `cores`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `days`
--
ALTER TABLE `days`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `genders`
--
ALTER TABLE `genders`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `instruments`
--
ALTER TABLE `instruments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `FK_instrument_type_id` (`type_id`);

--
-- Indices de la tabla `instrument_types`
--
ALTER TABLE `instrument_types`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `levels`
--
ALTER TABLE `levels`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `map_points`
--
ALTER TABLE `map_points`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `permissions`
--
ALTER TABLE `permissions`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `preceptors`
--
ALTER TABLE `preceptors`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `responsables`
--
ALTER TABLE `responsables`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `role_has_permission`
--
ALTER TABLE `role_has_permission`
  ADD PRIMARY KEY (`id`),
  ADD KEY `permiso` (`permission_id`),
  ADD KEY `rol_id` (`role_id`);

--
-- Indices de la tabla `schedules`
--
ALTER TABLE `schedules`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `id` (`id`,`day_id`);

--
-- Indices de la tabla `schools`
--
ALTER TABLE `schools`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `school_years`
--
ALTER TABLE `school_years`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `school_year_workshop`
--
ALTER TABLE `school_year_workshop`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `teachers`
--
ALTER TABLE `teachers`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `town_down`
--
ALTER TABLE `town_down`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `user_has_role`
--
ALTER TABLE `user_has_role`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user` (`user_id`),
  ADD KEY `rol` (`role_id`);

--
-- Indices de la tabla `workshops`
--
ALTER TABLE `workshops`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `assistance_student_workshop`
--
ALTER TABLE `assistance_student_workshop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `cores`
--
ALTER TABLE `cores`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `days`
--
ALTER TABLE `days`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `instruments`
--
ALTER TABLE `instruments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `instrument_types`
--
ALTER TABLE `instrument_types`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `levels`
--
ALTER TABLE `levels`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de la tabla `map_points`
--
ALTER TABLE `map_points`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- AUTO_INCREMENT de la tabla `permissions`
--
ALTER TABLE `permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de la tabla `preceptors`
--
ALTER TABLE `preceptors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `responsables`
--
ALTER TABLE `responsables`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `role_has_permission`
--
ALTER TABLE `role_has_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=69;

--
-- AUTO_INCREMENT de la tabla `schedules`
--
ALTER TABLE `schedules`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `schools`
--
ALTER TABLE `schools`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=157;

--
-- AUTO_INCREMENT de la tabla `school_years`
--
ALTER TABLE `school_years`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de la tabla `school_year_workshop`
--
ALTER TABLE `school_year_workshop`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `students`
--
ALTER TABLE `students`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `teachers`
--
ALTER TABLE `teachers`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `town_down`
--
ALTER TABLE `town_down`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=28;

--
-- AUTO_INCREMENT de la tabla `user_has_role`
--
ALTER TABLE `user_has_role`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `workshops`
--
ALTER TABLE `workshops`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
