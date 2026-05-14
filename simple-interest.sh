#!/bin/bash
# Script ini digunakan untuk menghitung bunga tetap (simple interest).
# Penulis: Vian
# Rumus: I = P * r * t

echo "Masukkan modal awal (principal):"
read p
echo "Masukkan tingkat bunga per tahun (rate):"
read r
echo "Masukkan jangka waktu dalam tahun (time):"
read t

# Menghitung bunga
s=$(echo "$p * $r * $t / 100" | bc -l)

echo "Bunga tetap yang dihasilkan adalah: $s"
