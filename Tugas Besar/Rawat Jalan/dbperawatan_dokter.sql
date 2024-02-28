-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Feb 17, 2024 at 10:35 AM
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
(4, 'Anne', '004', '2024-02-01', '16:15:00', 'Selesai'),
(5, 'Sari', '005', '2024-02-12', '16:30:00', 'Selesai');

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
(3, 'Folavit', 'Tablet', 'Folavit merupakan asam folat untuk membantu memelihara sistem saraf, dan membantu proses pembentukan sel darah merah.', 'Rp. 14.000 per 1 strip', '35'),
(4, 'Alergine', 'Tablet', 'Untuk mengatasi berbagai kondisi alergi (rhinitis perennial, rhinitis alergi musiman & kronis/urtikaria idiopatik).', 'Rp. 53.200 per 1 strip', '50'),
(5, 'Triamcinolone', 'Tablet', 'Dapat mengurangi peradangan dan juga menekan sistem kekebalan tubuh.', 'Rp. 12.000 per 1 strip', '35'),
(6, 'biomaag', 'Tablet', 'Mengatasi gejala yang terkait dengan asam lambung seperti mual, nyeri lambung & nyeri ulu hati.', 'Rp. 5000 per 1 strip', '50');

-- --------------------------------------------------------

--
-- Table structure for table `data_pasien`
--

CREATE TABLE `data_pasien` (
  `id` int(11) NOT NULL,
  `nama_pasien` varchar(255) NOT NULL,
  `alamat` varchar(255) NOT NULL,
  `tanggal_lahir` date NOT NULL,
  `jenis_kelamin` enum('Laki-Laki','Perempuan') NOT NULL,
  `nomor_telepon` varchar(20) NOT NULL,
  `riwayat_medis` varchar(1000) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `data_pasien`
--

INSERT INTO `data_pasien` (`id`, `nama_pasien`, `alamat`, `tanggal_lahir`, `jenis_kelamin`, `nomor_telepon`, `riwayat_medis`) VALUES
(1, 'Arfan', 'A1 Regency', '1999-09-09', 'Laki-Laki', '021111111111', 'Hipotensi'),
(2, 'Vania', 'Grand 31', '1995-01-02', 'Perempuan', '031222222222', 'Hipertensi'),
(3, 'Niles', 'Kolonel Regency', '2000-02-02', 'Laki-Laki', '085000000000', 'Alergi Makanan Tertentu'),
(4, 'Anne', 'Jl. Kusuma Bangsa', '1998-03-05', 'Perempuan', '089555555555', 'Alergi Obat'),
(5, 'Sari', 'Jl. Manis', '2000-02-14', 'Perempuan', '02316666666666', 'Maag');

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
(4, 'Anne', '2024-02-01', 'mual, mata berair, gatal-gatal/ruam', 'Alergi Obat', 'Triamcinolone 1*1'),
(5, 'Sari', '2024-02-12', 'nyeri pada perut bagian atas, mual, panas di dada', 'Maag', 'amoxcillin 3*1 , biomag 3*1');

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `email` varchar(255) NOT NULL,
  `nama` varchar(50) NOT NULL,
  `password` varchar(255) NOT NULL,
  `level` enum('admin','dokter','apoteker') NOT NULL DEFAULT 'apoteker'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`id`, `email`, `nama`, `password`, `level`) VALUES
(1, 'nurul@gmail.com', 'Nurul', '$2y$10$C.V5KYaVkPWzLM0yPqcvk.yj/qYkXGz6IWgnlMpVI/OHXcwQUCLsG', 'apoteker'),
(2, 'rahman@gmail.com', 'Dr. Rahman', '$2y$10$20fmDPukZxTItptm1E1snutkXdGLPLjLUMc28On0o5CUnzgF9sLju', 'dokter'),
(3, 'safarizkyfaddillah09@gmail.com', 'Safa', '$2y$10$XA2dgDsn0xpVU9unJdAHSeUKWT3KNc7HtZ/mJxKuHZF0Vhf0SXfNS', 'admin');

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
-- Indexes for table `data_obat`
--
ALTER TABLE `data_obat`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_obat` (`nama_obat`);

--
-- Indexes for table `data_pasien`
--
ALTER TABLE `data_pasien`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_pasien` (`nama_pasien`);

--
-- Indexes for table `data_pemeriksaan_pasien`
--
ALTER TABLE `data_pemeriksaan_pasien`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `nama_pasien` (`nama_pasien`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `data_antrian`
--
ALTER TABLE `data_antrian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `data_obat`
--
ALTER TABLE `data_obat`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `data_pasien`
--
ALTER TABLE `data_pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT for table `data_pemeriksaan_pasien`
--
ALTER TABLE `data_pemeriksaan_pasien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
