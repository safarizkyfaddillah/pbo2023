-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2024 at 05:10 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `dbperawatan_dokter`
--

-- --------------------------------------------------------

--
-- Table structure for table `data_obat`
--

CREATE TABLE `data_obat` (
  `id` int(11) NOT NULL,
  `nama_obat` varchar(255) NOT NULL,
  `jenis_obat` varchar(255) NOT NULL,
  `keterangan` text NOT NULL,
  `harga` varchar(100) NOT NULL,
  `stok` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_obat`
--

INSERT INTO `data_obat` (`id`, `nama_obat`, `jenis_obat`, `keterangan`, `harga`, `stok`) VALUES
(1, 'Catapres', 'Tablet', 'Menurunkan tekanan darah tinggi.', 'Rp. 85.000 per 1 strip', '30'),
(2, 'Amoxil (AMOXICILLIN)', 'Tablet', 'Antibiotik untuk mengobati infeksi bakteri yang disebabkan oleh mikroorganisme yang rentan.', 'Rp. 5000 per 1 strip', '50'),
(3, 'Folavit', 'Tablet', 'Folavit merupakan asam folat yang mampu membantu memelihara sistem saraf, dan membantu proses pembentukan sel darah merah.', 'Rp. 14.000 per 1 strip', '35'),
(4, 'Alergine', 'Tablet', 'Digunakan untuk mengatasi berbagai kondisi alergi (rhinitis perennial, rhinitis alergi musiman dan kronis atau urtikaria idiopatik).', 'Rp. 53.200 per 1 strip', '50'),
(5, 'Triamcinolone', 'Tablet', 'Obat alergi yang dapat mengurangi peradangan dan juga menekan sistem kekebalan tubuh.', 'Rp. 12.000 per 1 strip', '35');
(6, 'biomaag', 'Tablet', 'Mengatasi gejala yang terkait dengan asam lambung seperti mual, nyeri lambung & nyeri ulu hati.', 'Rp. 5.000 per 1 strip', '50');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_obat`
--
ALTER TABLE `data_obat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_obat` (`nama_obat`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_obat`
--
ALTER TABLE `data_obat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
