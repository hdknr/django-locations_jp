--
TRUNCATE TABLE {{ city_import }};
INSERT {{ city_import }}
(jiscode, name, kana, prefecture_id)
SELECT DISTINCT
  SRC.jiscode,
  SRC.city_name,
  SRC.city_kana,
  PREF.id
FROM {{ jpaddress_import }} AS SRC INNER JOIN {{ prefecture }} as PREF
ON SRC.pref_name = PREF.name;
