-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 12, 2024 at 05:09 PM
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
-- Table structure for table `data_pemeriksaan_pasien`
--

CREATE TABLE `data_pemeriksaan_pasien` (
  `id` int(11) NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `tanggal_pemeriksaan` date NOT NULL,
  `keluhan` varchar(255) NOT NULL,
  `diagnosis` varchar(255) NOT NULL,
  `resep_obat` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_pemeriksaan_pasien`
--

INSERT INTO `data_pemeriksaan_pasien` (`id`, `nama_pasien`, `tanggal_pemeriksaan`, `keluhan`, `diagnosis`, `resep_obat`) VALUES
(1, 'Arfan', '2024-02-01', 'pusing, mual, lemas', 'Hipotensi (Darah Rendah)', 'amoxicillin 3*1\r\nFolavit 1*1'),
(2, 'Vania', '2024-02-01', 'sakit kepala, nyeri di dada/sesak nafas, mual', 'Hipertensi (Darah Tinggi)', 'catapres 3*1'),
(3, 'Niles', '2024-02-01', 'sakit perut, diare, gatal-gatal/ruam, mual', 'Alergi Makanan Tertentu', 'Alergine 1*1'),
(4, 'Anne', '2024-02-01', 'mual, mata berair, gatal-gatal/ruam', 'Alergi Obat', 'Triamcinolone 1*1');
(5, 'Sari', '2024-02-12', 'nyeri pada perut bagian atas, mual, panas di dada', 'Maag', 'amoxcillin 3*1 , biomag 3*1');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_pemeriksaan_pasien`
--
ALTER TABLE `data_pemeriksaan_pasien`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_pasien` (`nama_pasien`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_pemeriksaan_pasien`
--
ALTER TABLE `data_pemeriksaan_pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
