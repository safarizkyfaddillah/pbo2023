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
-- Table structure for table `data_antrian`
--

CREATE TABLE `data_antrian` (
  `id` int(11) NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `nomor_antrian_pasien` enum('001','002','003','004','005','006','007','008','009','010','011','012','013','014','015','016','017','018','019','020','021','022','023','024','025','026','027','028','029','030','031','032','033','034','035','036','037','038','039','040','041','042','043','044','045','046','047','048','049','050') NOT NULL,
  `tanggal_antri` date NOT NULL,
  `jam_antri` time NOT NULL,
  `status` enum('Menunggu','Diproses','Selesai') NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_antrian`
--

INSERT INTO `data_antrian` (`id`, `nama_pasien`, `nomor_antrian_pasien`, `tanggal_antri`, `jam_antri`, `status`) VALUES
(1, 'Arfan', '001', '2024-02-01', '16:00:00', 'Selesai'),
(2, 'Vania', '002', '2024-02-01', '16:05:00', 'Selesai'),
(3, 'Niles', '003', '2024-02-01', '16:10:00', 'Selesai'),
(4, 'Anne', '004', '2024-02-01', '16:15:00', 'Selesai');
(5, 'Sari', '005', '2024-02-12', '16:30:00', 'Selesai');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `data_antrian`
--
ALTER TABLE `data_antrian`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_pasien` (`nama_pasien`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_antrian`
--
ALTER TABLE `data_antrian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
