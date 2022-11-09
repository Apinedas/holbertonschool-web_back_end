-- Glam rock
SELECT band_name, IF(split, split - formed, year(curdate()) - formed) AS lifespan FROM metal_bands WHERE style LIKE '%Glam rock%' ORDER BY lifespan DESC;